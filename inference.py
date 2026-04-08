import os
import sys
import requests
from pydantic import BaseModel
from openai import OpenAI

# Ensure local imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from server.models import CyberGuardAction
except ImportError:
    from models import CyberGuardAction


class CyberGuardObservation(BaseModel):
    message: str
    message_type: str
    difficulty: str
    done: bool
    reward: float = 0.0
    last_action_error: str | None = None


class CyberGuardEnv:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def reset(self):
        resp = requests.post(f"{self.base_url}/reset", timeout=60)
        resp.raise_for_status()
        return CyberGuardObservation(**resp.json())

    def step(self, action):
        payload = action.model_dump() if hasattr(action, "model_dump") else action.dict()
        resp = requests.post(f"{self.base_url}/step", json=payload, timeout=60)
        resp.raise_for_status()
        return CyberGuardObservation(**resp.json())

    def close(self):
        try:
            requests.post(f"{self.base_url}/close", timeout=10)
        except Exception:
            pass


API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")
if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

ENV_URL = os.getenv("ENV_URL", "http://localhost:7860")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

SYSTEM_PROMPT = (
    "You are a cyber security expert. "
    "Classify the message as one of: safe, suspicious, highly_suspicious, scam. "
    "Reply with ONLY the label."
)


def fmt_bool(v: bool) -> str:
    return "true" if v else "false"


def run_task(task_name: str):
    env = CyberGuardEnv(base_url=ENV_URL)
    rewards = []
    steps = 0
    success = False
    obs = None

    print(f"[START] task={task_name} env=cyberguard model={MODEL_NAME}")

    try:
        obs = env.reset()

        while not obs.done:
            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {
                            "role": "user",
                            "content": f"Message: {obs.message}\nType: {obs.message_type}",
                        },
                    ],
                )
                label = response.choices[0].message.content.strip().lower()
            except Exception:
                label = "suspicious"

            if label not in {"safe", "suspicious", "highly_suspicious", "scam"}:
                label = "suspicious"

            action = CyberGuardAction(label=label)
            obs = env.step(action)

            steps += 1
            reward_val = float(getattr(obs, "reward", 0.0) or 0.0)
            rewards.append(reward_val)

            error_val = getattr(obs, "last_action_error", None)
            error_str = error_val if error_val else "null"
            print(
                f"[STEP] step={steps} action={label} "
                f"reward={reward_val:.2f} done={fmt_bool(obs.done)} error={error_str}"
            )

        success = True if obs and obs.done else False

    except Exception as e:
        success = False
        error_str = str(getattr(obs, "last_action_error", None) or e)
        print(
            f"[STEP] step={steps + 1} action=error reward=0.00 done=false error={error_str}"
        )

    finally:
        try:
            env.close()
        except Exception:
            pass

        rewards_str = ",".join(f"{r:.2f}" for r in rewards)
        print(f"[END] success={fmt_bool(success)} steps={steps} rewards={rewards_str}")


if __name__ == "__main__":
    run_task("cyberguard")
