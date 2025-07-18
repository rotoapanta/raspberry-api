#!/bin/bash
set -e

ENV_NAME=raspberry-api-env

# [1/6] Check for conda/miniforge3
if ! command -v conda &> /dev/null; then
    echo "ERROR: Conda/Miniforge3 is not installed or not in PATH. Please install Miniforge3 first."
    exit 1
fi

# [2/6] Check for conda environment
if conda info --envs | grep -q "$ENV_NAME"; then
    echo "Conda environment '$ENV_NAME' already exists."
else
    echo "Creating conda environment '$ENV_NAME' with Python 3.11..."
    conda create -n "$ENV_NAME" python=3.11 -y
fi

# [3/6] Activate conda environment
# shellcheck disable=SC1091
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

# [4/6] Copy .env.example to .env if not present
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Please edit .env with your real configuration before starting the API."
fi

# [5/6] Install/update pip and requirements
pip install --upgrade pip
pip install -r requirements.txt

# [6/6] Setup complete
echo "\nSetup complete!"
echo "To start the API, run:"
echo "conda activate $ENV_NAME"
echo "uvicorn app.main:app --host 0.0.0.0 --port 8000"
