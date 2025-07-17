Project Architecture
===================

The project follows a modular and professional architecture based on FastAPI:

- **app/**: Main source code.
  - **main.py**: Entry point and app configuration.
  - **api/v1/**: Versioned endpoints.
  - **services/**: Business logic and utilities.
  - **core/**: Global configuration and utilities.
  - **models/**: Data models (Pydantic, DB, etc).
- **tests/**: Unit and integration tests.
- **docs/**: Advanced technical documentation (Sphinx).
- **docker-compose.yml**: Service orchestration (API, DB, etc).
- **DEPLOY.md**: Multi-environment deployment guide.

API versioning allows for compatibility and easier future improvements.
