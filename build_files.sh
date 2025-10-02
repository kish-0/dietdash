#!/bin/bash
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Building static files..."
# Create necessary directories if they don't exist
mkdir -p static/css
mkdir -p static/js
mkdir -p templates

echo "Build complete!"