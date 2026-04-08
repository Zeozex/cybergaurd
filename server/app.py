import sys
import os
import uvicorn
from openenv.core.env_server import create_fastapi_app

# This makes sure Python can see the 'server' package from the root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # Try importing as a package member (Standard for the validator)
    from server.environment import CyberGuardEnvironment
    from server.models import CyberGuardAction, CyberGuardObservation
except ImportError:
    # Fallback to local import (Standard for direct execution)
    from environment import CyberGuardEnvironment
    from models import CyberGuardAction, CyberGuardObservation

# Create the app instance
app = create_fastapi_app(CyberGuardEnvironment, CyberGuardAction, CyberGuardObservation)

def main():
    """The entry point that the Scaler AI validator is looking for."""
    # We use the string "server.app:app" so uvicorn can find the object
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
