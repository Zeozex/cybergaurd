import os
import sys
sys.path.append(os.path.dirname(__file__))

from openai import OpenAI
from client import CyberGuardEnv, CyberGuardAction

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1")
API_KEY = os.getenv("API_KEY") or os.getenv("HF_TOKEN") or ""
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")
ENV_URL = os.getenv("ENV_URL", "http://localhost:8000")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

SYSTEM_PROMPT = """You are a cyber security expert.
Analyze the given message and classify it as one of:
- safe
- suspicious
- highly_suspicious
- scam

Reply with ONLY the label, nothing else."""

def run_task(difficulty: str, num_episodes: int = 1):
    scores = []
    for _ in range(num_episodes):
        env = CyberGuardEnv(base_url=ENV_URL)
        obs = env.reset()
        episode_rewards = []
        steps = 0
        while not obs.done:
            if obs.difficulty != difficulty:
                obs = env.step(CyberGuardAction(label="safe"))
                continue
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Message: {obs.message}\nType: {obs.message_type}"}
                ],
                max_tokens=10,
                temperature=0.1,
            )
            label = response.choices[0].message.content.strip().lower()
            if label not in ["safe", "suspicious", "highly_suspicious", "scam"]:
                label = "suspicious"
            obs = env.step(CyberGuardAction(label=label))
            if obs.reward is not None:
                episode_rewards.append(obs.reward)
            steps += 1
        if episode_rewards:
            scores.append(sum(episode_rewards) / len(episode_rewards))
        elif steps > 0:
            scores.append(0.0)
    return sum(scores) / len(scores) if scores else 0.0

if __name__ == "__main__":
    print("Running CyberGuard Baseline Inference...")
    print("-" * 40)
    easy_score = run_task("easy")
    print(f"Easy Task Score:   {easy_score:.3f}")
    medium_score = run_task("medium")
    print(f"Medium Task Score: {medium_score:.3f}")
    hard_score = run_task("hard")
    print(f"Hard Task Score:   {hard_score:.3f}")
    print("-" * 40)
    overall = (easy_score + medium_score + hard_score) / 3
    print(f"Overall Score:     {overall:.3f}")
