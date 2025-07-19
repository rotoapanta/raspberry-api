# raspberry-api Deployment Guide

This document describes how to deploy the API on a Raspberry Pi using a Python virtual environment (recommended for real hardware monitoring).

---

## Prerequisites
- `git` installed on the target Raspberry Pi.
- Python 3.8+ and `pip` installed.

---

## Environment Configuration

The application uses a `.env` file for configuration. Example:

```
# .env - Environment configuration for raspberry-api
#
# This file contains environment variables used to configure the application.
# Do NOT commit your real .env file with sensitive data to version control.
#
# Variables:
#   LOG_INTERVAL - Interval (in seconds) for logging system status
#   LOG_DIR      - Directory where log files will be stored

LOG_INTERVAL=10
LOG_DIR=logs
```

Edit `.env` as needed for your environment.

---

## Deployment (Python Virtual Environment)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rotoapanta/raspberry-api.git
   cd raspberry-api
   ```

2. **Create and edit the environment file:**
   ```bash
   cp .env.example .env  # Or create .env manually
   # Edit .env as needed for your configuration
   ```

3. **Create and activate the virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Start the API:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

---

## Deployment (Conda Environment + systemd Service)

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/rotoapanta/raspberry-api.git
   cd raspberry-api
   ```

2. **Ejecuta el script de setup:**
   ```bash
   bash setup.sh
   ```
   - Si es la primera vez que usas conda en este dispositivo, cierra y vuelve a abrir la terminal (o ejecuta `source ~/.bashrc`) después del setup.

3. **Edita el archivo `.env`** (si es necesario):
   ```bash
   nano .env
   ```
   - Ajusta la configuración según tu entorno.

4. **(Opcional) Prueba la API manualmente:**
   ```bash
   conda activate raspberry-api-env
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   - Accede a `http://<IP_RASPBERRY>:8000/api/v1/status` para verificar que funciona.

5. **Instala el servicio systemd:**
   ```bash
   sudo cp systemd/raspberry-api.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable raspberry-api.service
   sudo systemctl start raspberry-api.service
   sudo systemctl status raspberry-api.service
   ```
   - El servicio arrancará automáticamente en cada reinicio.

---

## Notes
- Ambos métodos aseguran que la API pueda acceder a la información real del hardware de la Raspberry Pi (CPU, RAM, disco, hostname, IP, USBs, etc.).
- Para logging y monitoreo, los logs se almacenan en el directorio definido por `LOG_DIR`.
