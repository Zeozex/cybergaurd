import sys
import os
import uvicorn
from openenv.core.env_server import create_fastapi_app

# Ensure local imports work
sys.path.insert(0, os.path.dirname(__file__))

from environment import CyberGuardEnvironment
from models import CyberGuardAction, CyberGuardObservation

# This is the app object for the entry-point
app = create_fastapi_app(CyberGuardEnvironment, CyberGuardAction, CyberGuardObservation)

def main():
    """The entry point that the validator is looking for."""
    import uvicorn
    # This tells uvicorn to run the 'app' object defined in this file
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
