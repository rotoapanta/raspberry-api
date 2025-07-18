"""
config.py - Loads and centralizes application configuration using environment variables and .env
"""

import os
from dotenv import load_dotenv

# Load variables from .env if it exists
load_dotenv()

BACKEND_IP = os.getenv("BACKEND_IP", "192.168.1.100")
BACKEND_PORT = os.getenv("BACKEND_PORT", "8001")
REGISTER_INTERVAL = int(os.getenv("REGISTER_INTERVAL", 60))
LOG_INTERVAL = int(os.getenv("LOG_INTERVAL", 10))
LOG_DIR = os.getenv("LOG_DIR", "logs")
