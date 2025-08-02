#!/bin/bash
set -e

docker-compose up -d --build

echo "Waiting for PostgreSQL to be ready..."
until docker exec $(docker-compose ps -q db) pg_isready -U inventory_user -d inventory_db; do
  sleep 2
done

docker exec -i $(docker-compose ps -q db) psql -U inventory_user -d inventory_db < schema.sql
if [ -f data/sample_data.sql ]; then
  docker exec -i $(docker-compose ps -q db) psql -U inventory_user -d inventory_db < data/sample_data.sql
fi

echo "Database and FastAPI app initialized at http://localhost:8000."
