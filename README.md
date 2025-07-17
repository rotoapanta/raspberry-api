# Raspberry API

API for monitoring and logging the status of a Raspberry Pi, developed with FastAPI. It allows you to query system information, log events, and periodically communicate with a backend.

## Features
- Query system status: CPU, RAM, disk, USBs, temperature, hostname, IP, uptime, and battery.
- Read system logs.
- Periodic registration with a remote backend.
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

## Flexible Configuration
You can define configuration in a `.env` file at the project root. Example:

```
BACKEND_IP=192.168.1.100
BACKEND_PORT=8001
REGISTER_INTERVAL=60
LOG_INTERVAL=10
LOG_DIR=logs
```

Copy the example file:
```bash
cp .env.example .env
```

## Local Usage
1. Clone the repository:
   ```bash
   git clone <REPO_URL>
   cd raspberry-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## Dockerization
You can build and run the API in a Docker container:

```bash
docker build -t raspberry-api .
docker run -d -p 8000:8000 --env-file .env --name raspberry-api raspberry-api
```

Or use Docker Compose for multi-service deployment (API + PostgreSQL):

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
