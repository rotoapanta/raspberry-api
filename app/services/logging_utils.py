"""
logging_utils.py - Utilities for connection log recording and reading.

Provides functions to record the connection status (online/offline) and read the latest recorded events.
Uses the centralized logger defined in app.core.logging_config.
"""

import os
from datetime import datetime
from typing import List, Dict
from app.core.logging_config import logger, LOG_DIR

CONNECTION_LOG_FILE = os.path.join(LOG_DIR, "connection.log")

def log_status(is_online: bool) -> None:
    """
    Records the connection status (ONLINE/OFFLINE) in the log file and in the main logger.

    :param is_online: True if the system is online, False if it is offline.
    """
    os.makedirs(os.path.dirname(CONNECTION_LOG_FILE), exist_ok=True)
    status = "ONLINE" if is_online else "OFFLINE"
    log_entry = f"{datetime.now().isoformat()} - {status}"
    try:
        with open(CONNECTION_LOG_FILE, "a") as f:
            f.write(log_entry + "\n")
        logger.info(f"Connection status recorded: {status}")
    except Exception as e:
        logger.error(f"Error writing to connection log: {e}")

def read_logs() -> List[Dict[str, str]]:
    """
    Reads the last 50 records from the connection log file.

    :return: List of dictionaries with 'timestamp' and 'status'.
    """
    if not os.path.exists(CONNECTION_LOG_FILE):
        logger.warning(f"Connection log file does not exist: {CONNECTION_LOG_FILE}")
        return []
    try:
        with open(CONNECTION_LOG_FILE, "r") as f:
            lines = f.readlines()
        return [
            {"timestamp": line.split(" - ")[0], "status": line.split(" - ")[1].strip()}
            for line in lines[-50:]
            if " - " in line
        ]
    except Exception as e:
        logger.error(f"Error reading connection log: {e}")
        return []
