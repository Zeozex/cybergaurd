import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Server'))
sys.path.insert(0, os.path.dirname(__file__))

from openenv.core.env_server import create_fastapi_app
from environment import CyberGuardEnvironment
from models import CyberGuardAction, CyberGuardObservation

app = create_fastapi_app(CyberGuardEnvironment, CyberGuardAction, CyberGuardObservation)