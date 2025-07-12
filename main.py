from fastapi import FastAPI
import psutil
import socket
import os
import requests
import threading
import time
from services.logging_utils import log_status, read_logs

app = FastAPI()

BACKEND_IP = os.getenv("BACKEND_IP", "192.168.1.100")  # Cambia según sea necesario
BACKEND_PORT = os.getenv("BACKEND_PORT", "8001")
REGISTER_INTERVAL = 60  # segundos
LOG_INTERVAL = 10  # segundos

@app.get("/status")
def get_status():
    disk = psutil.disk_usage('/')

    # Buscar todas las unidades USB montadas bajo /media/pi
    usb_mount_prefix = "/media/pi"
    usb_disks = []
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
                continue  # Ignorar si no se puede acceder a la unidad

    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": round(disk.percent, 2),
        "disk_info": {
            "total": round(disk.total / (1024 ** 3), 2),
            "used": round(disk.used / (1024 ** 3), 2),
            "free": round(disk.free / (1024 ** 3), 2)
        },
        "usb": usb_disks,  # Lista con todas las memorias detectadas
        "temp": get_cpu_temp(),
        "hostname": socket.gethostname(),
        "ip": get_local_ip(),
        "battery": {
            "voltage": 3.7,
            "status": "NORMAL"
        }
    }


@app.get("/log")
def get_log():
    return read_logs()

@app.post("/reboot")
def reboot():
    os.system("reboot")
    return {"status": "Rebooting..."}

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return round(int(f.read()) / 1000, 1)
    except:
        return None

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def register_with_backend():
    while True:
        try:
            payload = {
                "hostname": socket.gethostname(),
                "ip": get_local_ip()
            }
            url = f"http://{BACKEND_IP}:{BACKEND_PORT}/register"
            requests.post(url, json=payload, timeout=5)
        except Exception as e:
            print(f"[!] Error registering with backend: {e}")
        time.sleep(REGISTER_INTERVAL)

def monitor():
    while True:
        log_status(True)
        time.sleep(LOG_INTERVAL)

threading.Thread(target=register_with_backend, daemon=True).start()
threading.Thread(target=monitor, daemon=True).start()
