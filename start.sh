#!/bin/bash
set -e

echo "Running docker compose from /home/ec2-user/app"

cd /home/ec2-user/app

# Debug: list files
ls -la

# Start the container
sudo docker compose up -d
