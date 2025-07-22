Project Architecture
===================

The project follows a modular and professional architecture based on FastAPI:

- **app/**: Main source code.
  - **main.py**: Entry point and app configuration.
  - **api/v1/**: Versioned endpoints.
  - **services/**: Business logic and utilities.
  - **core/**: Global configuration and utilities (including centralized logging).
  - **models/**: Data models (Pydantic, DB, etc).
- **tests/**: Unit and integration tests.
- **docs/**: Advanced technical documentation (Sphinx).
- **docker-compose.yml**: Service orchestration (API, DB, etc).
- **DEPLOY.md**: Multi-environment deployment guide.

Logging
-------
- All important events, including connection status, are recorded in the centralized log file: `raspberry-api.log` (with automatic rotation).
- The old `connection.log` file is no longer used.
- Logging configuration is centralized in `app/core/logging_config.py` and can be customized via environment variables (e.g., `LOG_DIR`).

API versioning allows for compatibility and easier future improvements.
