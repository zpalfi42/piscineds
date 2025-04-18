#!/bin/bash

DB_NAME="piscineds"
DB_USER="zpalfi"
DB_HOST="localhost"
SQL_FILE1="/ex03/clean_items_sql.sql"
SQL_FILE2="/ex03/fusion_sql.sql"

if [ ! -f "$SQL_FILE1" ]; then
  echo "Error: SQL file '$SQL_FILE1' not found!"
  exit 1
fi

if [ ! -f "$SQL_FILE2" ]; then
  echo "Error: SQL file '$SQL_FILE2' not found!"
  exit 1
fi

psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -f "$SQL_FILE1"
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -f "$SQL_FILE2"

if [ $? -eq 0 ]; then
  echo "SQL file executed successfully."
else
  echo "Error: Failed to execute the SQL file."
  exit 1
fi