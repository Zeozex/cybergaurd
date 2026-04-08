import sys
import os
import uvicorn

# Ensure the current directory is in the path
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from openenv.core.env_server import create_fastapi_app
from environment import CyberGuardEnvironment
from models import CyberGuardAction, CyberGuardObservation

# Create the app instance for Uvicorn/FastAPI
app = create_fastapi_app(CyberGuardEnvironment, CyberGuardAction, CyberGuardObservation)

# Add this main function for the validator
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# Add this block to make it callable
if __name__ == "__main__":
    main()
