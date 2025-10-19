# Core Framework
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0

# Database
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
alembic==1.13.0
pymongo==4.6.0
motor==3.3.2  # Async MongoDB driver
redis==5.0.1
hiredis==2.2.3  # Redis performance boost

# Authentication & Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
bcrypt==4.1.1

# Email
aiosmtplib==3.0.1
email-validator==2.1.0
jinja2==3.1.2

# HTTP Client
httpx==0.25.2
aiohttp==3.9.1

# Templates & Static Files
jinja2==3.1.2
aiofiles==23.2.1

# AI & Translation
anthropic==0.8.1
openai==1.6.1  # For Whisper transcription

# Celery (Background Tasks)
celery==5.3.4
kombu==5.3.4

# PDF Processing
PyPDF2==3.0.1
pdfplumber==0.10.3
reportlab==4.0.7  # For PDF generation

# Image Processing
Pillow==10.1.0

# Audio/Video
ffmpeg-python==0.2.0

# Utilities
python-dotenv==1.0.0
python-dateutil==2.8.2
pytz==2023.3.post1
validators==0.22.0

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
pytest-mock==3.12.0
httpx==0.25.2  # For API testing
faker==20.1.0  # Test data generation

# Code Quality
black==23.12.0
flake8==6.1.0
isort==5.13.2
mypy==1.7.1

# Development
watchdog==3.0.0  # File watching for hot reload
ipython==8.18.1
rich==13.7.0  # Beautiful console output

# Monitoring & Logging
loguru==0.7.2
sentry-sdk[fastapi]==1.39.1  # Error tracking (optional)

# Data Validation & Parsing
python-slugify==8.0.1
bleach==6.1.0  # HTML sanitization
markdown==3.5.1

# Calendar & Date Utilities
hijri-converter==2.3.1  # For Pascha calculation
convertdate==2.4.0
holidays==0.38  # Holiday calculations

# Web Scraping (for content import)
beautifulsoup4==4.12.2
lxml==4.9.3

# Rate Limiting
slowapi==0.1.9

# CORS
# (built into FastAPI, no separate package needed)

# Pagination
fastapi-pagination==0.12.13

# File Upload
python-magic==0.4.27

# Search
# (PostgreSQL full-text search built-in)

# Caching
cachetools==5.3.2

# Configuration
pyyaml==6.0.1

# CLI Tools
click==8.1.7
typer==0.9.0

# Performance
orjson==3.9.10  # Fast JSON