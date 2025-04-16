#!/bin/bash

SRC_FOLDER="./src"
CONTAINER_NAME="postgres"
DEST_FOLDER="/ex01"

docker exec "$CONTAINER_NAME" mkdir -p "$DEST_FOLDER"

for file in "$SRC_FOLDER"/*; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")
    echo "Copying $filename to $CONTAINER_NAME:$DEST_FOLDER"
    docker cp "$file" "$CONTAINER_NAME:$DEST_FOLDER"
  fi
done

echo "All files have been copied."