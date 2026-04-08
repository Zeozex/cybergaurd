import sys
import os
sys.path.append(os.path.dirname(__file__))

from models import CyberGuardAction, CyberGuardObservation, CyberGuardState
import requests

class CyberGuardEnv:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url

    def reset(self) -> CyberGuardObservation:
        response = requests.post(f"{self.base_url}/reset")
        payload = response.json()
        if "observation" in payload:
            obs_data = payload["observation"]
            obs_data["done"] = payload.get("done", False)
            obs_data["reward"] = payload.get("reward", None)
            return CyberGuardObservation(**obs_data)
        payload.setdefault("done", False)
        payload.setdefault("reward", None)
        return CyberGuardObservation(**payload)

    def step(self, action: CyberGuardAction) -> CyberGuardObservation:
        response = requests.post(
            f"{self.base_url}/step",
            json={"action": {"label": action.label}}
        )
        payload = response.json()
        reward = payload.get("reward", None)
        done = payload.get("done", False)
        if "observation" in payload:
            obs_data = payload["observation"]
            obs_data["done"] = done
            obs_data["reward"] = reward
            return CyberGuardObservation(**obs_data)
        payload.setdefault("done", False)
        payload.setdefault("reward", None)
        return CyberGuardObservation(**payload)

    def state(self) -> CyberGuardState:
        response = requests.get(f"{self.base_url}/state")
        payload = response.json()
        return CyberGuardState(**payload)
    