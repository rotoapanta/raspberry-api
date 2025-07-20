"""
config.py - Loads and centralizes application configuration using environment variables and .env
"""

import os
from dotenv import load_dotenv

# Load variables from .env if it exists
load_dotenv()

REGISTER_INTERVAL = int(os.getenv("REGISTER_INTERVAL", 60))
LOG_INTERVAL = int(os.getenv("LOG_INTERVAL", 10))
LOG_DIR = os.getenv("LOG_DIR", "logs")
API_VERSION = "1.0.0"
AUTHOR = "Roberto Toapanta"
