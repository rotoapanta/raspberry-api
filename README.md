# Raspberry API

API for monitoring and logging the status of a Raspberry Pi, developed with FastAPI. It allows you to query system information, log events, and periodically communicate with a backend.

## Features
- Query system status: CPU, RAM, disk, USBs, temperature, hostname, IP, uptime, and battery.
- Read system logs.
- Extensible and professional architecture.
- Flexible configuration via environment variables and `.env` file.
- Ready for deployment with Docker.
- Automatic linting and formatting with black and flake8.
- Automatic log rotation to prevent large log files.

## Requirements
- Python 3.8+
- FastAPI
- psutil
- requests
- python-dotenv
- black, flake8 (for development)

Install dependencies with:
```bash
pip install -r requirements.txt
```

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

## Deployment

You can deploy this project on any Raspberry Pi using either a Python virtual environment or Docker/Docker Compose.

### Option A: Python Virtual Environment (recommended for development)

1. Clone the repository:
   ```bash
   git clone https://github.com/rotoapanta/raspberry-api.git
   cd raspberry-api
   ```
2. Create and edit the environment file:
   ```bash
   cp .env.example .env  # Or create .env manually
   # Edit .env as needed
   ```
3. Create and activate the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the API:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Option B: Docker/Docker Compose (recommended for production)

1. Clone the repository:
   ```bash
   git clone https://github.com/rotoapanta/raspberry-api.git
   cd raspberry-api
   ```
2. Create and edit the environment file:
   ```bash
   cp .env.example .env  # Or create .env manually
   # Edit .env as needed
   ```
3. Deploy only the API with Docker:
   ```bash
   docker build -t raspberry-api .
   docker run -d -p 8000:8000 --env-file .env --name raspberry-api raspberry-api
   ```
4. Deploy multi-service with Docker Compose (API + PostgreSQL):
   ```bash
   docker-compose up -d
   ```

## Linting and Automatic Formatting
To keep the code clean and consistent:

- Format with black:
  ```bash
  black .
  ```
- Lint with flake8:
  ```bash
  flake8 .
  ```

## Automatic Log Rotation
- Logs are stored in the directory defined by `LOG_DIR` (default `logs/`).
- The main log file (`app.log`) is automatically rotated at 5 MB, keeping up to 5 backup files.

## Main Endpoints
- `GET /api/v1/status` — Returns the current system status.
- `GET /api/v1/log` — Returns the content of the registered logs.

Interactive API documentation is available at `/docs` (Swagger UI) and `/redoc`.

## Project Structure
```
raspberry-api/
├── app/
│   ├── main.py                # API entry point
│   ├── api/
│   │   └── v1/
│   │       └── status.py      # Versioned status endpoints
│   ├── services/
│   │   └── logging_utils.py   # Logging utilities
│   ├── core/
│   │   ├── config.py          # Flexible configuration
│   │   └── logging_config.py  # Professional logging configuration
│   ├── models/                # Pydantic/data models (if used)
├── tests/                     # Unit and integration tests
├── logs/                      # Log files
├── requirements.txt           # Dependencies
├── README.md                  # Main documentation
├── .env.example               # Example configuration
├── .env                       # Real environment configuration (not committed)
├── Dockerfile                 # Dockerization
├── docker-compose.yml         # Multi-service orchestration
├── DEPLOY.md                  # Deployment guide
├── pyproject.toml             # black and flake8 config
├── LICENSE                    # License
└── systemd/                   # systemd integration files
```

## Contributing
Contributions are welcome! Please open an issue or pull request for suggestions or improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, contact: [your-email@example.com]
