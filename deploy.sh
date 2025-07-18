#!/bin/bash
set -e

# Stop and remove previous containers (if any)
echo "🧹 Stopping and removing previous container (if exists)..."
docker compose down

echo "🚀 Building and starting the raspberry-api container..."
docker compose up --build -d

echo "✅ Container started. You can check logs with:"
echo "   docker compose logs -f api"
