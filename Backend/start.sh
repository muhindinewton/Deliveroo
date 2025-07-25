#!/bin/bash
# Render start script
# This script runs to start your application on Render

echo "Starting Deliveroo API server..."
uvicorn main:app --host 0.0.0.0 --port $PORT
