"""
logging_utils.py - Utilities for connection log recording and reading.

Provides functions to record the connection status (online/offline) and read the latest recorded events.
Uses the centralized logger defined in app.core.logging_config.
"""

from datetime import datetime
from typing import List, Dict
import os
import re
from app.core.logging_config import logger, LOG_DIR


def log_status(is_online: bool) -> None:
    """
    Records the connection status (ONLINE/OFFLINE) in the centralized logger.

    :param is_online: True if the system is online, False if it is offline.
    """
    status = "ONLINE" if is_online else "OFFLINE"
    logger.info(f"Connection status: {status}")


def read_logs() -> List[Dict[str, str]]:
    """
    Reads the last 50 connection status records from the centralized log file (raspberry-api.log and rotated logs).

    :return: List of dictionaries with 'timestamp' and 'status'.
    """
    log_dir = LOG_DIR
    log_files = [
        os.path.join(log_dir, f) for f in os.listdir(log_dir)
        if f.startswith("raspberry-api.log")
    ]
    log_files.sort(reverse=True)  # Most recent first
    pattern = re.compile(r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[INFO\] [^:]+: Connection status: (?P<status>ONLINE|OFFLINE)")
    records = []
    for log_file in log_files:
        try:
            with open(log_file, "r") as f:
                for line in reversed(f.readlines()):
                    match = pattern.match(line)
                    if match:
                        records.append({
                            "timestamp": match.group("timestamp"),
                            "status": match.group("status")
                        })
                        if len(records) >= 50:
                            return records
        except Exception as e:
            logger.error(f"Error reading log file {log_file}: {e}")
    return records
