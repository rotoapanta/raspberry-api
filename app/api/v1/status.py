"""
status.py - Status endpoints and system utilities for the Raspberry Pi API
"""

from fastapi import APIRouter
import psutil
import socket
import time
from typing import Any, Dict, List, Optional
from app.services.logging_utils import read_logs

router = APIRouter()

@router.get("/status")
def get_status() -> Dict[str, Any]:
    """
    Returns the current system status: CPU, RAM, disk, USBs, temperature, hostname, IP, uptime, and battery.
    """
    disk = psutil.disk_usage('/')

    # Find all USB drives mounted under /media/pi
    usb_mount_prefix = "/media/pi"
    usb_disks: List[Dict[str, Any]] = []
    for part in psutil.disk_partitions(all=False):
        if part.mountpoint.startswith(usb_mount_prefix):
            try:
                usage = psutil.disk_usage(part.mountpoint)
                usb_disks.append({
                    "mount": part.mountpoint,
                    "device": part.device,
                    "total": round(usage.total / (1024 ** 3), 2),
                    "used": round(usage.used / (1024 ** 3), 2),
                    "free": round(usage.free / (1024 ** 3), 2),
                    "percent": round(usage.percent, 2)
                })
            except PermissionError:
                continue  # Ignore if the drive cannot be accessed

    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": round(disk.percent, 2),
        "disk_info": {
            "total": round(disk.total / (1024 ** 3), 2),
            "used": round(disk.used / (1024 ** 3), 2),
            "free": round(disk.free / (1024 ** 3), 2)
        },
        "usb": usb_disks,  # List of all detected USB drives
        "temp": get_cpu_temp(),
        "hostname": socket.gethostname(),
        "ip": get_local_ip(),
        "uptime": int(time.time() - psutil.boot_time()),
        "battery": {
            "voltage": 3.7,
            "status": "NORMAL"
        }
    }

@router.get("/log")
def get_log() -> Any:
    """
    Returns the content of the system logs.
    """
    return read_logs()

def get_cpu_temp() -> Optional[float]:
    """
    Reads the CPU temperature from the file system.
    :return: Temperature in Celsius or None if not available.
    """
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return round(int(f.read()) / 1000, 1)
    except Exception:
        return None

def get_local_ip() -> str:
    """
    Gets the device's local IP address using a UDP socket.
    :return: Local IP as a string.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip: str = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip
