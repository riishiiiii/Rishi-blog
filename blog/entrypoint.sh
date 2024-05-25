#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start the Django development server with autoreload
echo "Starting Django development server with autoreload..."
python manage.py runserver 0.0.0.0:8000 
