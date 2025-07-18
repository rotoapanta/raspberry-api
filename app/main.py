"""
main.py - Entry point for the Raspberry Pi monitoring and logging API

Initializes the FastAPI application, registers routers, and starts the background thread for monitoring.
"""

from fastapi import FastAPI
import socket
import threading
import time
from app.services.logging_utils import log_status
from app.api.v1.status import router as status_router

app = FastAPI()

# Logging interval (seconds)
LOG_INTERVAL: int = 10

# Register API routers under versioned prefix
app.include_router(status_router, prefix="/api/v1")

def get_local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip: str = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def monitor() -> None:
    """
    Background thread that periodically logs the system status.
    """
    while True:
        log_status(True)
        time.sleep(LOG_INTERVAL)

# Start background thread for monitoring
threading.Thread(target=monitor, daemon=True).start()
