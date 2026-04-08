import os
import sys
import requests
from openai import OpenAI

# 1. Pathing Fix: Ensure the root is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import your Action model from the server folder
try:
    from server.models import CyberGuardAction
except ImportError:
    from models import CyberGuardAction

# --- CUSTOM CLIENT CLASS ---
# This replaces the missing 'server.client' and talks to your FastAPI server
class CyberGuardEnv:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def reset(self):
        resp = requests.post(f"{self.base_url}/reset")
        resp.raise_for_status()
        return CyberGuardObservation(**resp.json())

    def step(self, action):
        resp = requests.post(f"{self.base_url}/step", json=action.dict())
        resp.raise_for_status()
        return CyberGuardObservation(**resp.json())

# Helper to handle observations
from pydantic import BaseModel
class CyberGuardObservation(BaseModel):
    message: str
    message_type: str
    difficulty: str
    done: bool
    reward: float = 0.0

# --- CONFIGURATION ---
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1")
API_KEY = os.getenv("API_KEY") or os.getenv("HF_TOKEN") or ""
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")
# On Hugging Face, the server runs on port 7860
ENV_URL = os.getenv("ENV_URL", "http://localhost:7860")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

SYSTEM_PROMPT = """You are a cyber security expert.
Analyze the given message and classify it as one of:
- safe
- suspicious
- highly_suspicious
- scam

Reply with ONLY the label, nothing else."""

def run_task(difficulty: str, num_episodes: int = 1):
    print(f"[START] task={difficulty}_tier env=cyberguard model={MODEL_NAME}")
    
    scores = []
    for _ in range(num_episodes):
        env = CyberGuardEnv(base_url=ENV_URL)
        obs = env.reset()
        episode_rewards = []
        steps = 0
        
        while not obs.done:
            # Skip messages not matching the current task difficulty
            if obs.difficulty != difficulty:
                obs = env.step(CyberGuardAction(label="safe"))
                continue
            
            # AI Inference
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
            
            # Environment Step
            obs = env.step(CyberGuardAction(label=label))
            
            steps += 1
            reward_val = obs.reward if obs.reward is not None else 0.0
            episode_rewards.append(reward_val)
            
            print(f"[STEP] step={steps} action={label} reward={reward_val:.2f} done={obs.done} error=null")

        if episode_rewards:
            ep_score = sum(episode_rewards) / len(episode_rewards)
            scores.append(ep_score)
            success = ep_score > 0
            print(f"[END] success={success} steps={steps} score={ep_score:.3f} rewards={episode_rewards}")
        elif steps > 0:
            scores.append(0.0)
            print(f"[END] success=false steps={steps} score=0.000 rewards=[]")
            
    return sum(scores) / len(scores) if scores else 0.0

if __name__ == "__main__":
    # Ensure environment is ready
    try:
        easy_score = run_task("easy")
        medium_score = run_task("medium")
        hard_score = run_task("hard")
        
        overall = (easy_score + medium_score + hard_score) / 3
        print("-" * 40)
        print(f"Final Summary Score: {overall:.3f}")
    except Exception as e:
        print(f"Execution Error: {e}")
        sys.exit(1)
