#!/bin/bash

# Development Server Script for openLMS
# This script launches the Django development server with proper configuration

set -e  # Exit on any error

echo "🚀 Starting openLMS Development Server..."

# Check if we're in the correct directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: manage.py not found. Please run this script from the project root directory."
    exit 1
fi

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ] && [ -d ".venv" ]; then
    echo "📦 Activating virtual environment..."
    source .venv/bin/activate
fi

# Check if uv is available and use it if possible
if command -v uv &> /dev/null; then
    echo "🔧 Using uv for dependency management..."
    # Ensure dependencies are installed
    uv sync
else
    echo "⚠️  uv not found, using pip..."
    # Check if requirements are installed
    if ! python -c "import django" &> /dev/null; then
        echo "📦 Installing dependencies..."
        pip install -r requirements.txt
    fi
fi

# Set default environment variables
export DEBUG=True
export DJANGO_SETTINGS_MODULE=openLMS.settings

# Check if .env file exists, if not create a basic one
if [ ! -f ".env" ]; then
    echo "📝 Creating basic .env file..."
    cat > .env << EOF
# Django Settings
SECRET_KEY=django-insecure-dev-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (using SQLite for development)
DATABASE_URL=sqlite:///db.sqlite3

# Email (console backend for development)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Static files
STATIC_URL=/static/
STATIC_ROOT=staticfiles/

# Media files
MEDIA_URL=/media/
MEDIA_ROOT=media/
EOF
    echo "✅ Created .env file with development settings"
fi

# Run database migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

# Create superuser if it doesn't exist (optional)
echo "👤 Checking for superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    print('No superuser found. You can create one with: python manage.py createsuperuser')
else:
    print('Superuser exists')
" 2>/dev/null || echo "⚠️  Could not check for superuser"

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "🌐 Starting development server..."
echo "📍 Server will be available at: http://127.0.0.1:8000"
echo "🔧 Django Admin: http://127.0.0.1:8000/admin"
echo "📊 Debug Toolbar: Available in DEBUG mode"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

source .venv/bin/activate
# Start the development server
python manage.py runserver 0.0.0.0:8000