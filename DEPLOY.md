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

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rotoapanta/raspberry-api.git
   cd raspberry-api
   ```

2. **Run the setup script:**
   ```bash
   bash setup.sh
   ```
   - If this is your first time using conda on this device, close and reopen the terminal (or run `source ~/.bashrc`) after setup.

3. **Edit the `.env` file** (if needed):
   ```bash
   nano .env
   ```
   - Adjust the configuration as needed for your environment.

4. **(Optional) Test the API manually:**
   ```bash
   conda activate raspberry-api-env
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   - Access `http://<RASPBERRY_IP>:8000/api/v1/status` to verify it works.

5. **Install the systemd service:**
   ```bash
   sudo cp systemd/raspberry-api.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable raspberry-api.service
   sudo systemctl start raspberry-api.service
   sudo systemctl status raspberry-api.service
   ```
   - The service will start automatically on every reboot.

---

## Notes
- Both methods ensure the API can access real Raspberry Pi hardware information (CPU, RAM, disk, hostname, IP, USBs, etc.).
- For logging and monitoring, logs are stored in the directory defined by `LOG_DIR` (default is `logs/`).
- The main log file is `raspberry-api.log` and is automatically rotated at 5 MB (up to 5 backup files are kept).
- Logging configuration is centralized in `app/core/logging_config.py`.
