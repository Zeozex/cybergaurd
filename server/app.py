import sys
import os
import uvicorn
from openenv.core.env_server import create_fastapi_app

# This adds the root directory to the path so it can find things correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Change these lines to remove "server."
from environment import CyberGuardEnvironment
from models import CyberGuardAction, CyberGuardObservation

app = create_fastapi_app(CyberGuardEnvironment, CyberGuardAction, CyberGuardObservation)

def main():
    """The entry point that the validator is looking for."""
    # When running via the entry point, we refer to the module path
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
