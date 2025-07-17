"""
main.py - Entry point for the Raspberry Pi monitoring and logging API

Initializes the FastAPI application, registers routers, and starts background threads for registration and monitoring.
"""

from fastapi import FastAPI
import os
import requests
import socket
import threading
import time
from typing import Dict
from app.services.logging_utils import log_status
from app.api.v1.status import router as status_router

app = FastAPI()

# Backend configuration and registration/logging intervals
BACKEND_IP: str = os.getenv("BACKEND_IP", "192.168.1.100")  # Backend IP
BACKEND_PORT: str = os.getenv("BACKEND_PORT", "8001")       # Backend port
REGISTER_INTERVAL: int = 60  # Backend registration interval (seconds)
LOG_INTERVAL: int = 10       # Log registration interval (seconds)

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

def register_with_backend() -> None:
    """
    Background thread that periodically registers the device with the backend.
    """
    while True:
        try:
            payload: Dict[str, str] = {
                "hostname": socket.gethostname(),
                "ip": get_local_ip()
            }
            url: str = f"http://{BACKEND_IP}:{BACKEND_PORT}/register"
            requests.post(url, json=payload, timeout=5)
        except Exception as e:
            print(f"[!] Error registering with backend: {e}")
        time.sleep(REGISTER_INTERVAL)

def monitor() -> None:
    """
    Background thread that periodically logs the system status.
    """
    while True:
        log_status(True)
        time.sleep(LOG_INTERVAL)

# Start background threads for registration and monitoring
threading.Thread(target=register_with_backend, daemon=True).start()
threading.Thread(target=monitor, daemon=True).start()
