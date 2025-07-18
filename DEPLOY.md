# raspberry-api Deployment Guide

This document describes how to deploy the API on another Raspberry Pi using either a Python virtual environment or Docker/Docker Compose.

---

## Prerequisites
- `git` installed on the target Raspberry Pi.
- For virtual environment: Python 3.8+ and `pip` installed.
- For Docker: Docker and (optionally) Docker Compose installed.

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

## Option A: Deploy with Python Virtual Environment (recommended for development)

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
   pip install -r requirements.txt
   ```

5. **Start the API:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

---

## Option B: Deploy with Docker/Docker Compose (recommended for production)

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

3. **Deploy only the API with Docker:**
   ```bash
   docker build -t raspberry-api .
   docker run -d -p 8000:8000 --env-file .env --name raspberry-api raspberry-api
   ```

4. **Deploy multi-service with Docker Compose (API + PostgreSQL):**
   ```bash
   docker-compose up -d
   ```

---

## Notes
- You can scale services, add load balancers, or use orchestrators like Kubernetes as the project grows.
- For logging and monitoring, you can mount volumes or integrate external tools.
