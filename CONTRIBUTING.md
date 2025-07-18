# Contributing Guide

Thank you for your interest in contributing to this project!

## How to contribute

1. **Fork** the repository and create a branch for your feature or fix.
2. **Make your changes** following the project's best practices:
   - Use static typing (type hints) throughout the Python code.
   - Follow the professional folder structure.
   - Write clear docstrings and comments.
   - Use black and flake8 to format and check your code.
   - Add or update tests if necessary.
3. **Open a Pull Request** clearly describing your changes.
4. Wait for review and respond to maintainers' comments.

## Development setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Linting and formatting

- Format your code with black:
  ```bash
  black .
  ```
- Check your code with flake8:
  ```bash
  flake8 .
  ```

## Testing

- Add your tests in the `tests/` folder.
- Run tests with pytest:
  ```bash
  pytest
  ```

## Commit style

- Use clear and descriptive commit messages.
- Example: `fix: fix error in /status endpoint`

## Code of conduct

- Be respectful and professional in all interactions.

Thank you for helping improve this project!
