"""
Configuration Template for Monastier Online

IMPORTANT:
1. Copy this file to config.py
2. Fill in your actual values
3. NEVER commit config.py to Git!
"""

import os
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================================
# APPLICATION SETTINGS
# =============================================================================

APP_NAME = "Monastier Online"
APP_VERSION = "1.0.0"
DEBUG = True  # Set to False in production
TESTING = False

# Server
HOST = "0.0.0.0"
PORT = 8000

# Domain
DOMAIN = "monastier.online"
BASE_URL = f"https://{DOMAIN}"

# =============================================================================
# DATABASE SETTINGS
# =============================================================================

# PostgreSQL (Primary Database)
DATABASE_URL = "postgresql://portal_user:your_password_here@localhost:5432/monastier_online"

# Connection Pool Settings
DB_POOL_SIZE = 5
DB_MAX_OVERFLOW = 10
DB_POOL_TIMEOUT = 30
DB_POOL_RECYCLE = 3600

# MongoDB (For flexible content like Saints)
MONGODB_URL = "mongodb://localhost:27017"
MONGODB_DB_NAME = "monastier_online"

# Redis (Cache & Sessions)
REDIS_URL = "redis://localhost:6379/0"
REDIS_CACHE_TTL = 3600  # seconds (1 hour)

# =============================================================================
# SECURITY SETTINGS
# =============================================================================

# JWT Authentication
JWT_SECRET_KEY = "your-super-secret-jwt-key-change-this-in-production"
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 15  # 15 minutes
JWT_REFRESH_TOKEN_EXPIRE_DAYS = 7  # 7 days

# Password Hashing
PASSWORD_MIN_LENGTH = 8
BCRYPT_ROUNDS = 12  # Higher = more secure but slower

# CORS Settings
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    f"https://{DOMAIN}",
    f"https://www.{DOMAIN}",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["*"]
CORS_ALLOW_HEADERS = ["*"]

# Rate Limiting
RATE_LIMIT_ENABLED = True
RATE_LIMIT_PER_MINUTE = 60
RATE_LIMIT_PER_HOUR = 1000

# =============================================================================
# EMAIL SETTINGS
# =============================================================================

# SMTP Configuration
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_TLS = True
SMTP_USER = "monastierkomarno@gmail.com"
SMTP_PASSWORD = "your-gmail-app-password"  # Gmail App Password, not regular password

# Email Sender
EMAIL_FROM = "noreply@monastier.online"
EMAIL_FROM_NAME = "Monastier Online"

# Email Templates
EMAIL_VERIFY_SUBJECT = "Overte váš účet - Monastier Online"
EMAIL_RESET_PASSWORD_SUBJECT = "Reset hesla - Monastier Online"
EMAIL_WELCOME_SUBJECT = "Vitajte na Monastier Online"
EMAIL_DAILY_READING_SUBJECT = "Denné čítania - {date}"

# Verification Token Expiry
EMAIL_VERIFY_TOKEN_EXPIRE_HOURS = 24

# =============================================================================
# AI & TRANSLATION SETTINGS
# =============================================================================

# Anthropic Claude API
ANTHROPIC_API_KEY = "sk-ant-your-api-key-here"
ANTHROPIC_MODEL = "claude-sonnet-4-5-20250929"  # or claude-opus-4.1
ANTHROPIC_MAX_TOKENS = 4096

# OpenAI API (for Whisper transcription)
OPENAI_API_KEY = "sk-your-openai-api-key-here"

# Translation Settings
DEFAULT_LANGUAGE = "sk"
SUPPORTED_LANGUAGES = ["sk", "hu"]
TRANSLATION_GLOSSARY = {
    "Liturgia": "Liturgia",
    "Bohorodička": "Istenszülő",
    "Sviatosť": "Szentség",
    # Add more terms...
}

# =============================================================================
# FILE STORAGE SETTINGS
# =============================================================================

# Local Storage
UPLOAD_DIR = BASE_DIR / "media" / "uploads"
STATIC_DIR = BASE_DIR / "app" / "static"
TEMPLATE_DIR = BASE_DIR / "app" / "templates"

# Max File Sizes (bytes)
MAX_UPLOAD_SIZE_MB = 50
MAX_UPLOAD_SIZE = MAX_UPLOAD_SIZE_MB * 1024 * 1024

# Allowed File Extensions
ALLOWED_EXTENSIONS = {
    "image": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "audio": {".mp3", ".wav", ".ogg", ".m4a"},
    "video": {".mp4", ".webm", ".mov"},
    "document": {".pdf", ".doc", ".docx", ".txt"},
}

# MinIO / S3 (Cloud Storage)
USE_CLOUD_STORAGE = False
MINIO_ENDPOINT = "localhost:9000"
MINIO_ACCESS_KEY = "your-minio-access-key"
MINIO_SECRET_KEY = "your-minio-secret-key"
MINIO_BUCKET = "monastier-online"
MINIO_SECURE = False  # Use True with SSL

# =============================================================================
# CELERY SETTINGS (Background Tasks)
# =============================================================================

CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Europe/Bratislava"
CELERY_ENABLE_UTC = False

# =============================================================================
# NOTIFICATION SETTINGS
# =============================================================================

# Push Notifications (OneSignal)
ONESIGNAL_APP_ID = "your-onesignal-app-id"
ONESIGNAL_API_KEY = "your-onesignal-api-key"
PUSH_NOTIFICATIONS_ENABLED = False

# Notification Schedule
DAILY_READING_TIME = "07:00"  # Send daily readings at 7:00 AM
FEAST_REMINDER_HOURS = 24  # Remind 24 hours before feast

# =============================================================================
# LOGGING SETTINGS
# =============================================================================

LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = BASE_DIR / "logs" / "app.log"
LOG_MAX_BYTES = 10_000_000  # 10 MB
LOG_BACKUP_COUNT = 5

# =============================================================================
# CACHE SETTINGS
# =============================================================================

# Cache TTL (Time To Live) in seconds
CACHE_TTL = {
    "calendar": 3600,  # 1 hour
    "prayers": 86400,  # 24 hours
    "books": 86400,  # 24 hours
    "churches": 43200,  # 12 hours
    "media": 3600,  # 1 hour
}

# =============================================================================
# PAGINATION SETTINGS
# =============================================================================

DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# =============================================================================
# SEARCH SETTINGS
# =============================================================================

SEARCH_MIN_QUERY_LENGTH = 3
SEARCH_MAX_RESULTS = 50

# =============================================================================
# SESSION SETTINGS
# =============================================================================

SESSION_LIFETIME_HOURS = 24
SESSION_COOKIE_NAME = "monastier_online_session"
SESSION_COOKIE_SECURE = True  # HTTPS only
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "lax"

# =============================================================================
# ANALYTICS & MONITORING
# =============================================================================

# Google Analytics
GA_TRACKING_ID = "G-XXXXXXXXXX"

# Sentry (Error Tracking)
SENTRY_DSN = "https://your-sentry-dsn@sentry.io/project-id"
SENTRY_ENABLED = False

# =============================================================================
# FEATURE FLAGS
# =============================================================================

FEATURES = {
    "user_registration": True,
    "email_verification": True,
    "social_login": False,  # OAuth2 (Google, Facebook)
    "push_notifications": False,
    "live_streaming": False,
    "donations": False,
    "mobile_app": False,
}

# =============================================================================
# CALENDAR SETTINGS
# =============================================================================

# Liturgical Calendar
CALENDAR_START_YEAR = 2025
CALENDAR_END_YEAR = 2030

# Julian vs Gregorian Calendar
USE_JULIAN_CALENDAR = False  # Most Orthodox in SK use Gregorian

# =============================================================================
# n8n WEBHOOK SETTINGS
# =============================================================================

# n8n Server
N8N_WEBHOOK_URL = "https://your-n8n-server.com/webhook"
N8N_API_KEY = "your-n8n-api-key"

# Webhook Endpoints
N8N_WEBHOOKS = {
    "user_registered": f"{N8N_WEBHOOK_URL}/user-registered",
    "content_translated": f"{N8N_WEBHOOK_URL}/content-translated",
    "backup_requested": f"{N8N_WEBHOOK_URL}/backup",
}

# =============================================================================
# DEVELOPMENT SETTINGS
# =============================================================================

# Auto-reload templates in development
TEMPLATE_AUTO_RELOAD = DEBUG

# Show detailed error pages
SHOW_ERROR_DETAILS = DEBUG

# Mock external services in development
MOCK_EMAIL = DEBUG
MOCK_AI_TRANSLATION = False

# =============================================================================
# PRODUCTION OVERRIDES
# =============================================================================

if not DEBUG:
    # Production-specific settings
    LOG_LEVEL = "WARNING"
    RATE_LIMIT_PER_MINUTE = 30
    SESSION_COOKIE_SECURE = True
    SHOW_ERROR_DETAILS = False
    MOCK_EMAIL = False


# =============================================================================
# VALIDATION
# =============================================================================

def validate_config():
    """Validate critical configuration values"""
    errors = []

    if JWT_SECRET_KEY == "your-super-secret-jwt-key-change-this-in-production":
        errors.append("JWT_SECRET_KEY must be changed!")

    if "your_password_here" in DATABASE_URL:
        errors.append("DATABASE_URL must be configured!")

    if ANTHROPIC_API_KEY == "sk-ant-your-api-key-here":
        errors.append("ANTHROPIC_API_KEY must be configured!")

    if SMTP_USER == "monastierkomarno@gmail.com" and SMTP_PASSWORD == "your-gmail-app-password":
        errors.append("SMTP_PASSWORD must be configured with Gmail App Password!")

    if errors:
        error_msg = "\n".join(f"  - {e}" for e in errors)
        raise ValueError(f"Configuration errors:\n{error_msg}")

# Run validation on import (comment out for initial setup)
# validate_config()