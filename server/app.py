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
    """Function called by the 'cyberguard-server' script."""
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=False)

if __name__ == "__main__":
    main()
