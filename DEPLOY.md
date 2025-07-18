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

## Notes
- This method ensures the API can access real hardware information from the Raspberry Pi (CPU, RAM, disk, hostname, IP, USBs, etc.).
- For production, you can use systemd to run the API as a service if desired.
- For logging and monitoring, logs are stored in the directory defined by `LOG_DIR`.
