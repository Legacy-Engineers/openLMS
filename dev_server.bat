@echo off
REM Development Server Script for openLMS (Windows)
REM This script launches the Django development server with proper configuration

echo 🚀 Starting openLMS Development Server...

REM Check if we're in the correct directory
if not exist "manage.py" (
    echo ❌ Error: manage.py not found. Please run this script from the project root directory.
    pause
    exit /b 1
)

REM Check if virtual environment is activated
if not defined VIRTUAL_ENV (
    if exist ".venv\Scripts\activate.bat" (
        echo 📦 Activating virtual environment...
        call .venv\Scripts\activate.bat
    )
)

REM Set environment variables
set DEBUG=True
set DJANGO_SETTINGS_MODULE=openLMS.settings

REM Check if .env file exists, if not create a basic one
if not exist ".env" (
    echo 📝 Creating basic .env file...
    (
        echo # Django Settings
        echo SECRET_KEY=django-insecure-dev-key-change-in-production
        echo DEBUG=True
        echo ALLOWED_HOSTS=localhost,127.0.0.1
        echo.
        echo # Database ^(using SQLite for development^)
        echo DATABASE_URL=sqlite:///db.sqlite3
        echo.
        echo # Email ^(console backend for development^)
        echo EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
        echo.
        echo # Static files
        echo STATIC_URL=/static/
        echo STATIC_ROOT=staticfiles/
        echo.
        echo # Media files
        echo MEDIA_URL=/media/
        echo MEDIA_ROOT=media/
    ) > .env
    echo ✅ Created .env file with development settings
)

REM Run database migrations
echo 🗄️  Running database migrations...
python manage.py migrate

REM Collect static files
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

echo.
echo 🌐 Starting development server...
echo 📍 Server will be available at: http://127.0.0.1:8000
echo 🔧 Django Admin: http://127.0.0.1:8000/admin
echo 📊 Debug Toolbar: Available in DEBUG mode
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the development server
python manage.py runserver 0.0.0.0:8000

pause 