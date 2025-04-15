#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to start..."
until pg_isready -h localhost -p 5432 -U "$POSTGRES_USER"; do
  sleep 1
done
echo "PostgreSQL is ready!"

# Run Python scripts
echo "Executing Python scripts..."
python3 /docker-entrypoint-initdb.d/automatic_table.py
python3 /docker-entrypoint-initdb.d/items_table.py
python3 /docker-entrypoint-initdb.d/customers_table.py

# Start PostgreSQL
echo "Starting PostgreSQL..."
exec docker-entrypoint.sh "$@"