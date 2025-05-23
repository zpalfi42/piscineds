#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to start..."
until pg_isready -h localhost -p 5432 -U "$POSTGRES_USER"; do
  sleep 1
done
echo "PostgreSQL is ready!"

# Run Python scripts
echo "Executing Python scripts..."
python3 /scripts/python/customers.py
python3 /scripts/python/items.py

# Start PostgreSQL
echo "Starting PostgreSQL..."
exec docker-entrypoint.sh "$@"