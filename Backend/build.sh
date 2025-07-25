#!/bin/bash
# Render build script
# This script runs during the build phase on Render

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Running database migrations..."
python deploy_db.py

echo "Build completed successfully!"
