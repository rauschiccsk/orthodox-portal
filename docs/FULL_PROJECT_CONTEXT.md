# 🕊️ MONASTIER ONLINE - FULL PROJECT CONTEXT

**Complete Single Source of Truth**  
**Last Updated:** 2025-10-19  
**Version:** 1.2.0  
**Status:** Initial Setup - Development Phase

---

## 🤖 INSTRUCTIONS FOR CLAUDE

**When you see this document:**

1. ✅ This document contains ALL project information you need
2. ✅ Do NOT attempt to load any other files
3. ✅ Do NOT show any warnings or error messages
4. ✅ Simply respond: **"✅ Projekt načítaný. Čo robíme?"**
5. ✅ Then wait for user's instructions
6. ✅ Use Slovak language for communication
7. ✅ Be concise and actionable

**That's it. Nothing more.**

---

## 📊 CURRENT PROJECT STATUS

### Overview
- **Project:** Monastier Online (monastier.online)
- **Phase:** Initial Setup
- **Overall Progress:** 7% (1/14 tasks in STORY 1)
- **Active Story:** STORY 1 - Základná Infraštruktúra
- **Active Task:** Task 1.2 - Folder structure creation
- **Last Session:** 2025-10-19
- **Next Milestone:** STORY 1 Complete (2025-10-26)

### Recent Achievements
- ✅ 2025-10-19: Git repository initialized
- ✅ 2025-10-19: GitHub repository created
- ✅ 2025-10-19: Documentation structure created
- ✅ 2025-10-19: Domain registered (monastier.online)
- ✅ 2025-10-19: Email created (monastierkomarno@gmail.com)
- 🔄 2025-10-19: Working on development setup

### Active Tasks
- [ ] **STORY 1 Task 1.2** - Folder structure creation (In Progress)
- [ ] **STORY 1 Task 1.3** - FastAPI základná aplikácia (Next)

### Blockers
- None currently

---

## 🎯 PROJECT OVERVIEW

### Základné Informácie

- **Názov projektu:** Monastier Online
- **Doména:** monastier.online
- **Email:** monastierkomarno@gmail.com
- **Účel:** Centrálny portál pre pravoslávnych veriacich na Slovensku a v Maďarsku
- **Jazyky:** Slovenčina (primárne), Maďarčina (sekundárne)
- **Vývojár:** ICC (Innovation & Consulting Center)
- **Developer:** rauschiccsk
- **Lokalizácia:** Komárno, SK
- **Typ projektu:** Single-server deployment (nie multi-client)

### Vízia Projektu

Vytvoriť pre slovenských a maďarských pravoslávnych veriacich **jedno centrálne miesto na webe**, kde šikovne a prehľadne môžu nájsť:
- 📅 Liturgický kalendár s dennými čítaniami
- 🙏 Kompletné modlitby a bohoslužobné texty
- 📚 Duchovnú literatúru a životy svätých
- 🎬 Audio/video nahrávky liturgií
- 🗺️ Mapu pravoslávnych chrámov
- 📰 Aktuálne informácie a udalosti
- 👤 User registration a notifikácie

### Inšpirácia
- **azbyka.ru** - komplexný ruský portál (vzor)
- **posledovanie.ru** - liturgické texty

---

## 📊 GITHUB REPOSITORY

### Repository Info
```
URL: https://github.com/rauschiccsk/orthodox-portal
Branch: main (production)
Branch: develop (development)
Development path: C:\Development\orthodox-portal
Deployment path: C:\Deployment\orthodox-portal
```

### Začiatok každého nového chatu
```
Pokračujeme na Monastier Online projekte.

https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/FULL_PROJECT_CONTEXT.md

Dnes chcem pracovať na: [STORY X, Task X.Y]
```

---

## 🏗️ ARCHITEKTÚRA SYSTÉMU

### Tech Stack
```yaml
Frontend: 
  - FastAPI + Jinja2 Templates
  - TailwindCSS 3.x
  - Alpine.js (lightweight JS)
  - PWA support

Backend:
  - Python 3.11+
  - FastAPI 0.104+
  - SQLAlchemy 2.0+ (ORM)
  - Pydantic (validation)

Databases:
  - PostgreSQL 15+ (monastier_online)
  - MongoDB 7+ (flexible content - saints)
  - Redis 7+ (cache, sessions)

Storage:
  - MinIO / AWS S3 (media files)

Automation:
  - n8n (workflows, translations, backups)
  - Celery (background tasks)

Authentication:
  - JWT tokens
  - OAuth2 (Google, Facebook)
  - Email verification

Notifications:
  - Email (SMTP via Gmail)
  - Push notifications (OneSignal)

Search:
  - PostgreSQL Full-Text Search

Server:
  - Existujúci n8n server
  - Nginx (reverse proxy)
  - SSL (Let's Encrypt)
  - Systemd services

AI Services:
  - Anthropic Claude API (translation SK ↔ HU)
  - OpenAI Whisper (audio transcription)
```

### System Architecture Diagram
```
┌─────────────────────────────────────┐
│    Internet (monastier.online)      │
└────────────────┬────────────────────┘
                 │ HTTPS (443)
                 ▼
┌─────────────────────────────────────┐
│      Nginx Reverse Proxy            │
│      (SSL, Load Balancing)          │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│       FastAPI Application           │
│          (Port 8000)                │
└─┬────────┬─────────┬────────┬───────┘
  │        │         │        │
  ▼        ▼         ▼        ▼
┌────┐  ┌─────┐  ┌──────┐  ┌─────┐
│Post│  │Redis│  │Mongo │  │MinIO│
│greSQL  │(cache│  │(saints) │(media)
└────┘  └─────┘  └──────┘  └─────┘
  │
  ▼
┌─────────────────────────────────────┐
│     n8n Automation Server           │
│  • Daily Calendar Updates           │
│  • AI Translation Pipeline          │
│  • Email Notifications              │
│  • Automated Backups                │
└─────────────────────────────────────┘
```

---

## 💾 DATABASE SCHEMA

### PostgreSQL Tables

#### users
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    language CHAR(2) DEFAULT 'sk',
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    email_notifications BOOLEAN DEFAULT TRUE,
    push_notifications BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
```

#### calendar_events
```sql
CREATE TABLE calendar_events (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    event_type VARCHAR(50),
    title_sk VARCHAR(255) NOT NULL,
    title_hu VARCHAR(255),
    description_sk TEXT,
    description_hu TEXT,
    liturgical_color VARCHAR(20),
    readings_gospel_sk TEXT,
    readings_gospel_hu TEXT,
    readings_epistle_sk TEXT,
    readings_epistle_hu TEXT,
    is_movable BOOLEAN DEFAULT FALSE,
    priority INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### prayers
```sql
CREATE TABLE prayers (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(100) UNIQUE NOT NULL,
    category VARCHAR(50),
    title_sk VARCHAR(255) NOT NULL,
    title_hu VARCHAR(255),
    content_sk TEXT NOT NULL,
    content_hu TEXT,
    church_slavonic TEXT,
    order_num INTEGER,
    is_published BOOLEAN DEFAULT FALSE,
    views_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### books
```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(100) UNIQUE NOT NULL,
    title_sk VARCHAR(255) NOT NULL,
    title_hu VARCHAR(255),
    author VARCHAR(255),
    category VARCHAR(50),
    description_sk TEXT,
    description_hu TEXT,
    content_sk TEXT,
    content_hu TEXT,
    pdf_url VARCHAR(500),
    cover_image_url VARCHAR(500),
    is_published BOOLEAN DEFAULT FALSE,
    views_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### churches
```sql
CREATE TABLE churches (
    id SERIAL PRIMARY KEY,
    name_sk VARCHAR(255) NOT NULL,
    name_hu VARCHAR(255),
    address TEXT,
    city VARCHAR(100),
    country VARCHAR(2) DEFAULT 'SK',
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    phone VARCHAR(50),
    email VARCHAR(255),
    website VARCHAR(500),
    schedule_text TEXT,
    priest_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### media_files
```sql
CREATE TABLE media_files (
    id SERIAL PRIMARY KEY,
    type VARCHAR(20),
    title_sk VARCHAR(255) NOT NULL,
    title_hu VARCHAR(255),
    description_sk TEXT,
    description_hu TEXT,
    file_url VARCHAR(500) NOT NULL,
    thumbnail_url VARCHAR(500),
    duration INTEGER,
    file_size INTEGER,
    transcription TEXT,
    category VARCHAR(50),
    is_published BOOLEAN DEFAULT FALSE,
    views_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### user_bookmarks
```sql
CREATE TABLE user_bookmarks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    content_type VARCHAR(20),
    content_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, content_type, content_id)
);
```

#### notifications
```sql
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    type VARCHAR(50),
    title VARCHAR(255),
    message TEXT,
    link VARCHAR(500),
    is_read BOOLEAN DEFAULT FALSE,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### MongoDB Collections

#### saints (MongoDB)
```json
{
  "_id": ObjectId,
  "name_sk": "Svätý Nikolaj Myrlíkijský",
  "name_hu": "Szent Miklós",
  "feast_date": "12-19",
  "biography_sk": "Dlhý text...",
  "biography_hu": "Long text...",
  "icon_url": "https://...",
  "patron_of": ["detí", "námorníkov"],
  "miracles": [...],
  "prayers": [...],
  "created_at": ISODate
}
```

---

## 🚀 STORIES & DEVELOPMENT PLAN

### STORY 1: Základná Infraštruktúra ⚙️
**Status:** 🔄 In Progress (1/14 tasks)  
**Priority:** CRITICAL  
**Estimated:** 3-4 týždne  
**Started:** 2025-10-19

**Tasks:**
- [x] 1.1 - Git repository setup + .gitignore ✅
- [ ] 1.2 - Folder structure creation 🔄
- [ ] 1.3 - FastAPI základná aplikácia
- [ ] 1.4 - PostgreSQL databáza setup
- [ ] 1.5 - MongoDB setup (optional)
- [ ] 1.6 - Redis cache setup
- [ ] 1.7 - Základné Jinja2 templates
- [ ] 1.8 - TailwindCSS integration
- [ ] 1.9 - User authentication system (JWT)
- [ ] 1.10 - Admin panel základy
- [ ] 1.11 - Deployment na server
- [ ] 1.12 - Doména a SSL certifikát
- [ ] 1.13 - Testing framework setup
- [ ] 1.14 - CI/CD pipeline (GitHub Actions)

### STORY 2: Liturgický Kalendár 📅
**Status:** ⏳ Planned  
**Priority:** HIGH  
**Depends On:** STORY 1

**Key Features:**
- Pascha (Veľká noc) calculation algorithm
- Movable & fixed feasts
- Daily readings (Gospel, Epistle)
- Saints of the day
- Typikon rules (fasting days)
- Calendar export (PDF, iCal)
- n8n daily update workflow

### STORY 3: Modlitby a Bohoslužby 🙏
**Status:** ⏳ Planned  
**Priority:** HIGH

**Key Features:**
- Morning & evening prayers
- Akathists & Canons
- Divine Liturgy texts
- Vespers & Matins
- Church Slavonic support
- PDF export
- Offline PWA mode

### STORY 4: AI Preklad Systém 🤖
**Status:** ⏳ Planned  
**Priority:** HIGH

**Key Features:**
- Claude API integration
- Glossary management
- Batch translation
- Quality assurance
- n8n automation
- Manual review

### STORY 5: Knižnica a Obsahový Systém 📚
**Status:** ⏳ Planned  
**Priority:** MEDIUM

**Key Features:**
- Book database & categories
- Full-text search
- Saints' lives (MongoDB)
- Holy Scripture
- Reading progress
- Bookmarks

### STORY 6: Médiá (Audio/Video) 🎬
**Status:** ⏳ Planned  
**Priority:** MEDIUM

**Key Features:**
- MinIO/S3 storage
- Audio/video player
- Liturgy recordings
- Podcast feed
- Transcription
- Live streaming

### STORY 7: Mapa Chrámov a Komunita 🗺️
**Status:** ⏳ Planned  
**Priority:** LOW

**Key Features:**
- Church database
- Google Maps
- Service schedules
- Parish contacts
- Event calendar
- Newsletter

### STORY 8: User Management & Notifications 🔔
**Status:** 🔄 Partially started  
**Priority:** HIGH

**Key Features:**
- User registration & login
- Email verification
- Password reset
- User profile
- Email notifications
- Push notifications
- Newsletter
- Bookmarks
- OAuth2

---

## 📁 PROJECT STRUCTURE

```
orthodox-portal/
├── docs/                          # Dokumentácia
│   ├── FULL_PROJECT_CONTEXT.md    # Tento súbor
│   ├── PROJECT_STATUS.md          # Aktuálny stav
│   ├── MASTER_CONTEXT.md          # Master kontext
│   ├── README.md                  # Projekt README
│   └── sessions/                  # Session notes
├── app/                           # Hlavná aplikácia
│   ├── __init__.py
│   ├── main.py                    # FastAPI entry point
│   ├── config.py                  # Konfigurácia
│   ├── database.py                # DB connection
│   ├── models.py                  # SQLAlchemy models
│   ├── schemas.py                 # Pydantic schemas
│   ├── dependencies.py            # FastAPI dependencies
│   ├── api/                       # API endpoints
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── calendar.py
│   │   ├── prayers.py
│   │   ├── books.py
│   │   ├── churches.py
│   │   ├── media.py
│   │   ├── users.py
│   │   └── admin.py
│   ├── services/                  # Business logic
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── calendar_service.py
│   │   ├── translation_service.py
│   │   ├── email_service.py
│   │   └── cache_service.py
│   ├── utils/                     # Utilities
│   │   ├── __init__.py
│   │   ├── security.py
│   │   ├── validators.py
│   │   └── helpers.py
│   ├── templates/                 # Jinja2 templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── calendar.html
│   │   └── prayers.html
│   └── static/                    # Static files
│       ├── css/
│       ├── js/
│       └── images/
├── tests/                         # Testy
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_calendar.py
│   └── test_prayers.py
├── migrations/                    # Alembic migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── n8n/                          # n8n workflows
│   ├── calendar_daily_update.json
│   ├── translation_pipeline.json
│   ├── user_registration.json
│   └── daily_notifications.json
├── deploy/                       # Deployment
│   ├── nginx.conf
│   ├── monastier.service
│   └── deploy.sh
├── config/                       # Configuration
│   └── config_template.py
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables example
├── .gitignore                    # Git ignore
└── README.md                     # Project README
```

---

## 🔄 GIT WORKFLOW

### Branches
```
main (production, protected)
  └─ develop (development, protected)
       ├─ feature/liturgical-calendar
       ├─ feature/user-auth
       └─ feature/prayers-library
```

### Commit Convention
```
feat: Add new feature
fix: Fix bug
docs: Update documentation
refactor: Refactor code
test: Add tests
chore: Update dependencies
style: Code formatting
perf: Performance improvement
```

### Commit Example
```bash
git commit -m "feat: Add user registration endpoint

- Created /api/auth/register endpoint
- Added email validation
- Integrated with PostgreSQL users table
- Added verification email via n8n
- Added unit tests

STORY-8 Task 8.1 complete"
```

---

## 🎨 DESIGN SYSTEM

### Color Palette
```css
:root {
  --primary: #8B4513;        /* Sienna Brown */
  --secondary: #DAA520;      /* Goldenrod */
  --accent: #B22222;         /* Firebrick Red */
  --background: #F5F5DC;     /* Beige */
  --text: #2F4F4F;           /* Dark Slate Gray */
  --success: #228B22;
  --warning: #FF8C00;
  --error: #DC143C;
}
```

### Typography
```css
--font-heading: 'Georgia', serif;
--font-body: 'Open Sans', sans-serif;
--font-slavonic: 'Monomakh Unicode', serif;
```

### Key UX Features
- 🔍 Full-text search
- 📱 Mobile-first responsive design
- 🌙 Dark mode
- 🔖 Bookmarks
- 📥 Offline mode (PWA)
- 🎧 Background audio player
- 📖 Print-friendly pages
- 🔔 Push notifications

---

## 🤖 N8N WORKFLOWS

### 1. Daily Calendar Update
```yaml
Trigger: Cron - každý deň 00:01
Steps:
  1. Python Script - Generate denné čítania
  2. Claude API - Translate to Hungarian
  3. PostgreSQL - Insert/Update calendar_events
  4. Redis - Clear calendar cache
  5. Email - Send to subscribed users
  6. Social Media - Post to Facebook
```

### 2. User Registration Welcome
```yaml
Trigger: Webhook - new user registered
Steps:
  1. Generate verification token
  2. Email - Send verification email
  3. Wait for verification
  4. Email - Send welcome email
  5. PostgreSQL - Update preferences
```

### 3. Daily Notifications
```yaml
Trigger: Cron - každý deň 07:00
Steps:
  1. PostgreSQL - Get users with notifications enabled
  2. Get today's readings
  3. For each user:
     - Email daily reading
     - Push notification (if enabled)
  4. Log sent notifications
```

### 4. Content Translation Pipeline
```yaml
Trigger: Webhook - new content added
Steps:
  1. PostgreSQL - Fetch untranslated content
  2. Claude API - Translate SK → HU
  3. Quality Check - Validate terms
  4. Email - Notify admin for review
  5. PostgreSQL - Save translation
  6. Redis - Clear cache
```

### 5. Weekly Newsletter
```yaml
Trigger: Cron - nedeľa 18:00
Steps:
  1. Generate this week's highlights
  2. Create HTML template
  3. Get subscribed users
  4. Send personalized emails
  5. Track analytics
```

---

## 🧪 TESTING STRATEGY

### Test Coverage Goals
- **Unit tests:** 80%+ coverage
- **Integration tests:** All API endpoints
- **E2E tests:** Critical user journeys

### Testing Tools
- **pytest** - Unit & integration tests
- **pytest-cov** - Coverage reporting
- **httpx** - API testing
- **faker** - Test data generation

---

## 🚀 DEPLOYMENT

### Server Requirements
```yaml
OS: Ubuntu 22.04 LTS
CPU: 2+ cores
RAM: 4GB+ 
Disk: 50GB+ SSD
Python: 3.11+
PostgreSQL: 15+
Redis: 7+
Nginx: 1.22+
```

### Deployment Checklist
- [ ] Server access (SSH/RDP)
- [ ] Domain configured (monastier.online)
- [ ] DNS A records set
- [ ] SSL certificate (Let's Encrypt)
- [ ] PostgreSQL installed
- [ ] Redis installed
- [ ] Python 3.11 + venv
- [ ] Git repository cloned
- [ ] Dependencies installed
- [ ] Environment variables set
- [ ] Database migrations run
- [ ] Systemd service created
- [ ] Nginx configured
- [ ] Firewall rules set
- [ ] Backups configured

---

## 🔒 SECURITY

### Best Practices
- ✅ HTTPS only
- ✅ Password hashing (bcrypt, 12 rounds)
- ✅ JWT tokens (15 min access, 7 day refresh)
- ✅ Rate limiting (60/min, 1000/hour)
- ✅ CSRF protection
- ✅ SQL injection prevention (SQLAlchemy)
- ✅ XSS prevention (template escaping)
- ✅ Input validation (Pydantic)
- ✅ Environment variables for secrets
- ✅ Regular security updates

### Secrets Management
```bash
# .env file (NEVER commit)
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
JWT_SECRET=...
ANTHROPIC_API_KEY=sk-ant-...
SMTP_PASSWORD=...
```

---

## 📊 MONITORING & ANALYTICS

### Metrics to Track
- **Performance:** Response times, DB queries
- **Users:** Registrations, logins, active users
- **Content:** Most viewed prayers, books, media
- **Errors:** 500 errors, failed API calls
- **Infrastructure:** CPU, RAM, disk usage

### Tools
- **Application:** Built-in logging (loguru)
- **User Analytics:** Google Analytics / Matomo
- **Uptime:** UptimeRobot
- **Errors:** Sentry (optional)

---

## 📚 RESOURCES

### Content Sources
- **pravoslavie.sk** - Slovenský obsah
- **azbyka.ru** - Inšpirácia, vzor
- **OCA.org** - Anglické zdroje
- **Byzantinos.eu** - Liturgické texty
- **pravoslavie.ru** - Ruský obsah

### Technical Documentation
- **FastAPI:** https://fastapi.tiangolo.com/
- **PostgreSQL:** https://www.postgresql.org/docs/
- **n8n:** https://docs.n8n.io/
- **TailwindCSS:** https://tailwindcss.com/docs
- **Claude API:** https://docs.anthropic.com/

---

## ⚠️ CRITICAL REMINDERS

### Pre každý nový chat:
1. 🔥 User pošle URL na FULL_PROJECT_CONTEXT.md
2. 🔥 Claude načíta tento dokument
3. 🔥 Claude odpovie: "✅ Projekt načítaný. Čo robíme?"
4. 🔥 ŽIADNE ďalšie súbory, ŽIADNE varovania
5. 🔥 Jednoducho a jasne

### Git Rules:
- ✅ Commit často, malé zmeny
- ✅ Opisné commit messages
- ✅ Test pred commit
- ✅ Pull pred push
- ✅ Feature branches

### Documentation Rules:
- ✅ Update FULL_PROJECT_CONTEXT pri veľkých zmenách
- ✅ Code comments v slovenčine
- ✅ API dokumentácia aktuálna

---

## 🎯 SUCCESS CRITERIA

### MVP (Minimum Viable Product)
- ✅ User registration & login
- ✅ Liturgický kalendár na 2025
- ✅ 50+ základných modlitieb (SK)
- ✅ Responsive design
- ✅ SSL certificate
- ✅ Email notifications

### V1.0 Release
- ✅ Všetky STORIES 1-4 dokončené
- ✅ Slovenský obsah kompletný (500+ položiek)
- ✅ Maďarský preklad 80%+
- ✅ 10+ aktívnych testovacích používateľov
- ✅ 95%+ uptime za 30 dní
- ✅ Page load < 2s
- ✅ Mobile-friendly (90+ Google PageSpeed)

---

## 📝 RECENT COMMITS

```bash
# 2025-10-19
feat: Initial project setup - Monastier Online
- Created comprehensive project structure
- Documentation (FULL_PROJECT_CONTEXT, PROJECT_STATUS, README)
- Configuration templates
- Requirements.txt with all dependencies
- Session template for daily work logs

STORY-1 Task 1.1 complete
Version: 1.0.0
```

---

## 📞 KONTAKT

- **Email:** monastierkomarno@gmail.com
- **GitHub:** https://github.com/rauschiccsk/orthodox-portal
- **Doména:** https://monastier.online
- **Developer:** rauschiccsk (ICC)

---

## 🤖 FINAL REMINDER FOR CLAUDE

**You have loaded FULL_PROJECT_CONTEXT.md**

This document contains:
- ✅ Complete project vision and goals
- ✅ Current status and progress (7% - Initial Setup)
- ✅ Full architecture and tech stack
- ✅ Database schemas (designed, not implemented)
- ✅ All 8 stories and development plan
- ✅ Project structure
- ✅ Git workflow and commit conventions
- ✅ Design system
- ✅ n8n workflows (planned)
- ✅ Testing, deployment, security guidelines

**Simply respond:**
```
✅ Projekt načítaný. Čo robíme?
```

---

**Document Version:** 1.2.0  
**Created:** 2025-10-19  
**Last Updated:** 2025-10-19  
**Status:** Active Development  

🕊️ **S Bohom!**