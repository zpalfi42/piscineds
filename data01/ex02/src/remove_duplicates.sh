#!/bin/bash

DB_NAME="piscineds"
DB_USER="zpalfi"
DB_HOST="localhost"
SQL_FILE="/ex02/remove_duplicates_sql.sql"

if [ ! -f "$SQL_FILE" ]; then
  echo "Error: SQL file '$SQL_FILE' not found!"
  exit 1
fi

psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -f "$SQL_FILE"

if [ $? -eq 0 ]; then
  echo "SQL file executed successfully."
else
  echo "Error: Failed to execute the SQL file."
  exit 1
fi