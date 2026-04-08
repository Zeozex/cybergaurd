import sys
import os
import uvicorn
from openenv.core.env_server import create_fastapi_app

# This ensures the 'server' directory is recognizable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Use absolute imports from the server package
from server.environment import CyberGuardEnvironment
from server.models import CyberGuardAction, CyberGuardObservation

app = create_fastapi_app(CyberGuardEnvironment, CyberGuardAction, CyberGuardObservation)

def main():
    """The entry point that the validator is looking for."""
    # We use the string path so uvicorn can find the app correctly
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
