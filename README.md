# <p align="center">Raspberry API

[![Python](https://img.shields.io/badge/Python-3.11-brightgreen)](https://www.python.org/)
![GitHub issues](https://img.shields.io/github/issues/rotoapanta/raspberry-api)
![GitHub repo size](https://img.shields.io/github/repo-size/rotoapanta/raspberry-api)
![GitHub last commit](https://img.shields.io/github/last-commit/rotoapanta/raspberry-api)
[![Discord Invite](https://img.shields.io/badge/discord-join%20now-green)](https://discord.gg/bf6rWDbJ)
[![Docker](https://img.shields.io/badge/Docker-No-brightgreen)](https://www.docker.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Project-brightgreen)](https://github.com/rotoapanta/raspberry-api)
[![Linux](https://img.shields.io/badge/Linux-Supported-brightgreen)](https://www.linux.org/)
[![Author](https://img.shields.io/badge/Roberto%20-Toapanta-brightgreen)](https://www.linkedin.com/in/roberto-carlos-toapanta-g/)
[![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen)](#change-log)
![GitHub forks](https://img.shields.io/github/forks/rotoapanta/raspberry-api?style=social)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

API for monitoring and logging the status of a Raspberry Pi, developed with FastAPI. It allows you to query system information, log events, and monitor your device in real time.

## Features
- Query system status: CPU, RAM, disk, USBs, temperature, hostname, IP, uptime, and battery.
- Read system logs.
- Extensible and professional architecture.
- Flexible configuration via environment variables and `.env` file.
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

## Deployment (Recommended: Python Virtual Environment)

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
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
5. Start the API:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
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

### API Response Metadata
The `/api/v1/status` endpoint returns a JSON object with two main keys:
- `meta`: Contains metadata about the response, including:
  - `timestamp`: Date and time of the response (UTC)
  - `api_version`: API version (from `config.py`)
  - `status`: Response status (e.g., "success")
  - `author`: Project author (from `config.py`)
- `data`: Contains the actual system status information.

The author and API version are configured in `app/core/config.py` as `AUTHOR` and `API_VERSION`.

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
For questions or support, contact: [robertocarlos.toapanta@gmail.com]
