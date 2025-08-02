#!/bin/bash
set -e

# Rebuild and restart containers
docker-compose down -v
docker-compose up -d --build

# Wait until the Postgres container is healthy
echo "Waiting for PostgreSQL to be ready..."
until docker-compose exec db pg_isready -U inventory_user -d inventory_db; do
  sleep 2
done

echo "PostgreSQL is ready. FastAPI app should be running at http://localhost:8000"
