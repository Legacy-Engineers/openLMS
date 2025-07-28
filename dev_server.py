#!/usr/bin/env python3
"""
Development Server Script for openLMS
This script launches the Django development server with proper configuration
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, check=True, capture_output=False):
    """Run a command and return the result"""
    try:
        result = subprocess.run(
            command, shell=True, check=check, capture_output=capture_output, text=True
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {command}")
        print(f"Error: {e}")
        return None


def check_file_exists(filename):
    """Check if a file exists"""
    return Path(filename).exists()


def create_env_file():
    """Create a basic .env file if it doesn't exist"""
    env_content = """# Django Settings
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
"""

    with open(".env", "w") as f:
        f.write(env_content)
    print("✅ Created .env file with development settings")


def main():
    print("🚀 Starting openLMS Development Server...")

    # Check if we're in the correct directory
    if not check_file_exists("manage.py"):
        print(
            "❌ Error: manage.py not found. Please run this script from the project root directory."
        )
        sys.exit(1)

    # Set environment variables
    os.environ.setdefault("DEBUG", "True")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openLMS.settings")

    # Check if .env file exists, if not create a basic one
    if not check_file_exists(".env"):
        print("📝 Creating basic .env file...")
        create_env_file()

    # Check if uv is available and use it if possible
    uv_available = run_command("which uv", check=False, capture_output=True)
    if uv_available and uv_available.returncode == 0:
        print("🔧 Using uv for dependency management...")
        run_command("uv sync")
    else:
        print("⚠️  uv not found, using pip...")
        # Check if Django is installed
        django_check = run_command(
            "python -c 'import django'", check=False, capture_output=True
        )
        if django_check and django_check.returncode != 0:
            print("📦 Installing dependencies...")
            run_command("pip install -r requirements.txt")

    # Run database migrations
    print("🗄️  Running database migrations...")
    run_command("python manage.py migrate")

    # Check for superuser
    print("👤 Checking for superuser...")
    superuser_check = """
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    print('No superuser found. You can create one with: python manage.py createsuperuser')
else:
    print('Superuser exists')
"""
    run_command(f'python manage.py shell -c "{superuser_check}"', check=False)

    # Collect static files
    print("📁 Collecting static files...")
    run_command("python manage.py collectstatic --noinput")

    print("")
    print("🌐 Starting development server...")
    print("📍 Server will be available at: http://127.0.0.1:8000")
    print("🔧 Django Admin: http://127.0.0.1:8000/admin")
    print("📊 Debug Toolbar: Available in DEBUG mode")
    print("")
    print("Press Ctrl+C to stop the server")
    print("")

    # Start the development server
    run_command("python manage.py runserver 0.0.0.0:8000")


if __name__ == "__main__":
    main()
