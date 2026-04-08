
from typing import Optional, List
from openenv.core.env_server import Action, Observation, State
 
class CyberGuardAction(Action):
    label: str

class CyberGuardObservation(Observation):
    message: str
    message_type: str
    difficulty: str
    done: bool
    reward: Optional[float] = None

class CyberGuardState(State):
    episode_id: Optional[str] = None
    step_count: int = 0
    current_score: float = 0
    difficulty: str = "easy"


