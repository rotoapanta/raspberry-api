#!/bin/bash
set -e

ENV_NAME="raspberry-api-env"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Color codes
GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[1;33m"
NC="\033[0m" # No Color

print_step() {
    echo -e "${YELLOW}[${1}] ${2}${NC}"
}

print_success() {
    echo -e "${GREEN}${1}${NC}"
}

print_error() {
    echo -e "${RED}${1}${NC}"
}

echo -e "${GREEN}Welcome ${USER}! Starting setup...${NC}"

print_step "1/7" "Checking architecture and OS"
ARCH=$(uname -m)
OS=$(lsb_release -ds || cat /etc/os-release || uname -a)
echo "Detected OS: $OS"
echo "Architecture: $ARCH"

print_step "2/7" "Checking for conda/Miniforge3"
if ! command -v conda &> /dev/null; then
    print_error "ERROR: Conda/Miniforge3 is not installed or not in PATH."
    echo "Please install Miniforge3 from:"
    echo "https://github.com/conda-forge/miniforge"
    exit 1
fi

print_step "3/7" "Checking for conda environment '$ENV_NAME'"
if conda info --envs | grep -q "$ENV_NAME"; then
    print_success "Conda environment '$ENV_NAME' already exists."
else
    echo "Creating conda environment '$ENV_NAME' with Python 3.11..."
    conda create -n "$ENV_NAME" python=3.11 -y
fi

print_step "4/7" "Activating conda environment"
# Activación segura sin depender de .bashrc
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

print_step "5/7" "Copying .env.example to .env (if not exists)"
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
    echo "⚠️  Please edit .env with your actual configuration before starting the API."
fi

print_step "6/7" "Installing/updating pip and project requirements"
pip install --upgrade pip
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    pip install -r "$SCRIPT_DIR/requirements.txt"
else
    print_error "requirements.txt not found in $SCRIPT_DIR"
    exit 1
fi

print_step "7/7" "Setup complete"
print_success "✅ Setup completed successfully!"
echo -e "To start the API, run:\n"
echo -e "  ${YELLOW}conda activate $ENV_NAME${NC}"
echo -e "  ${YELLOW}uvicorn app.main:app --host 0.0.0.0 --port 8000${NC}"
