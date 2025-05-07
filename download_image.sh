#!/bin/bash
set -e
cd /home/ec2-user/app

echo "Downloading Docker image from S3..."
aws s3 cp s3://your-bucket-name/docker-images/my_first_app.tar .

echo "Loading Docker image..."
docker load -i my_first_app.tar
