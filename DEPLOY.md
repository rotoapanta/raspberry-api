# raspberry-api Deployment Guide

This document describes how to deploy the API in different environments using Docker and Docker Compose.

## Development environment (dev)

- Use a local virtual environment and run the API with Uvicorn:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```
- You can use the local database from Docker Compose:
  ```bash
  docker-compose up db
  ```

## Production environment (prod)

- Use Docker Compose to launch the entire infrastructure:
  ```bash
  docker-compose up -d
  ```
- This will start the API and the PostgreSQL database in separate containers.
- Set environment variables in `.env` for production (e.g., secure credentials, IPs, etc).

## Notes
- You can scale services, add load balancers, or use orchestrators like Kubernetes as the project grows.
- For logging and monitoring, you can mount volumes or integrate external tools.
