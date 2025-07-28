# Development Server Scripts

This directory contains scripts to easily launch the openLMS development server with proper configuration.

## Available Scripts

### 1. `dev_server.sh` (Linux/macOS)

Bash script for Unix-like systems.

**Usage:**

```bash
./dev_server.sh
```

### 2. `dev_server.py` (Cross-platform)

Python script that works on all platforms.

**Usage:**

```bash
python dev_server.py
# or
./dev_server.py
```

### 3. `dev_server.bat` (Windows)

Batch file for Windows systems.

**Usage:**

```cmd
dev_server.bat
```

## What These Scripts Do

1. **Environment Setup:**

   - Checks if you're in the correct directory
   - Activates virtual environment if available
   - Sets up environment variables
   - Creates a basic `.env` file if it doesn't exist

2. **Dependency Management:**

   - Uses `uv` if available, falls back to `pip`
   - Ensures all dependencies are installed

3. **Database Setup:**

   - Runs database migrations
   - Checks for existing superuser

4. **Static Files:**

   - Collects static files for development

5. **Server Launch:**
   - Starts the Django development server on `http://127.0.0.1:8000`

## Prerequisites

- Python 3.8+
- Django project dependencies (installed via `uv` or `pip`)
- Virtual environment (recommended)

## Environment Configuration

The scripts will create a basic `.env` file with the following settings:

```env
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
```

## Access Points

Once the server is running, you can access:

- **Main Application:** http://127.0.0.1:8000
- **Django Admin:** http://127.0.0.1:8000/admin
- **Debug Toolbar:** Available in DEBUG mode

## Troubleshooting

### Common Issues

1. **Permission Denied:**

   ```bash
   chmod +x dev_server.sh
   chmod +x dev_server.py
   ```

2. **Virtual Environment Not Found:**

   - Create a virtual environment: `python -m venv .venv`
   - Activate it manually before running the script

3. **Dependencies Not Installed:**

   - Run: `uv sync` or `pip install -r requirements.txt`

4. **Database Issues:**
   - Delete `db.sqlite3` and run migrations again
   - Check your `.env` file configuration

### Manual Setup

If the scripts don't work, you can manually run:

```bash
# Set environment
export DEBUG=True
export DJANGO_SETTINGS_MODULE=openLMS.settings

# Install dependencies
uv sync  # or pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start server
python manage.py runserver 0.0.0.0:8000
```

## Notes

- The scripts use `openLMS.settings` as the Django settings module
- SQLite is used as the default database for development
- Debug mode is enabled by default
- Static files are collected to the `staticfiles/` directory
- Media files are served from the `media/` directory
