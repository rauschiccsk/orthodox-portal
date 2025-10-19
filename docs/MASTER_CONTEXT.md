# 🕊️ MONASTIER ONLINE - MASTER CONTEXT

**Single Source of Truth pre celý projekt**  
**Verzia:** 1.0  
**Posledná aktualizácia:** 2025-10-19  
**Status:** Initial Setup

---

## 🎯 PROJECT OVERVIEW

### Základné Informácie

- **Názov projektu:** Monastier Online (monastier.online)
- **Účel:** Centrálny portál pre pravoslávnych veriacich na Slovensku a v Maďarsku
- **Jazyky:** Slovenčina (primárne), Maďarčina (sekundárne)
- **Vývojár:** ICC (monastierkomarno@gmail.com)
- **Lokalizácia:** Komárno, SK
- **Typ projektu:** Single-server deployment (nie multi-client)

### Vízia Projektu

Vytvoriť pre slovenských a maďarských pravoslávnych veriacich **jedno centrálne miesto na webe**, kde šikovne a prehľadne môžu nájsť:
- Liturgický kalendár s dennými čítaniami
- Kompletné modlitby a bohoslužobné texty
- Duchovnú literatúru a životy svätých
- Audio/video nahrávky liturgií
- Mapu pravoslávnych chrámov
- Aktuálne informácie a udalosti

### Inšpirácia

- **azbyka.ru** - komplexný ruský portál (knižnica, kalendár, modlitby, médiá)
- **posledovanie.ru** - liturgické texty a bohoslužby

---

## 📊 GITHUB REPOSITORY

### Repository Info

```
URL: https://github.com/rauschiccsk/pravoslavny-portal
Branch: main (production)
Branch: develop (development)
Lokálna cesta: C:\Development\pravoslavny-portal
```

### Prístup k súborom

```
Project File Access:
https://raw.githubusercontent.com/rauschiccsk/pravoslavny-portal/main/docs/project_file_access.json

Kritické súbory:
https://raw.githubusercontent.com/rauschiccsk/pravoslavny-portal/main/docs/MASTER_CONTEXT.md
https://raw.githubusercontent.com/rauschiccsk/pravoslavny-portal/main/docs/PROJECT_STATUS.md
https://raw.githubusercontent.com/rauschiccsk/pravoslavny-portal/main/config/config_template.py
https://raw.githubusercontent.com/rauschiccsk/pravoslavny-portal/main/requirements.txt
```

### Začiatok každého nového chatu

```markdown
Pokračujeme na Monastier Online projekte.

KRITICKÉ - Najprv načítaj GitHub súbory:
1. https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/project_file_access.json
2. https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/MASTER_CONTEXT.md
3. https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/PROJECT_STATUS.md

GitHub: https://github.com/rauschiccsk/orthodox-portal
Aktuálny stav: [pozri PROJECT_STATUS.md]

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
  - PostgreSQL 15+ (štruktúrovaný obsah, users)
  - MongoDB 7+ (flexibilný obsah - životy svätých)
  - Redis 7+ (cache, sessions, queue)

Storage:
  - MinIO / AWS S3 (PDF, audio, video súbory)

Automation:
  - n8n (workflows, preklady, backups)
  - Celery (background tasks)

Authentication:
  - JWT tokens
  - OAuth2 (Google, Facebook)
  - Email verification

Notifications:
  - Email (SMTP)
  - Push notifications (OneSignal / Firebase)
  - In-app notifications

Search:
  - PostgreSQL Full-Text Search
  - ElasticSearch (optional, budúcnosť)

Server:
  - Existujúci n8n server (Ubuntu/Debian)
  - Nginx (reverse proxy)
  - SSL (Let's Encrypt)
  - Systemd services

AI Services:
  - Anthropic Claude API (preklad SK ↔ HU)
  - OpenAI Whisper (audio transcription)
```

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│              Internet (pravoslavie.sk)               │
└────────────────────┬────────────────────────────────┘
                     │ HTTPS (443)
                     ▼
┌─────────────────────────────────────────────────────┐
│                 Nginx Reverse Proxy                  │
│              (SSL, Load Balancing)                   │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│              FastAPI Application                     │
│                  (Port 8000)                         │
│  ┌──────────────────────────────────────────┐      │
│  │  Routes  │  Services  │  Background Jobs │      │
│  └──────────────────────────────────────────┘      │
└────┬─────────┬──────────┬───────────┬──────────────┘
     │         │          │           │
     ▼         ▼          ▼           ▼
┌─────────┐ ┌──────┐ ┌────────┐ ┌─────────┐
│PostgreSQL│ │Redis │ │MongoDB │ │  MinIO  │
│  (main  │ │(cache│ │(saints)│ │ (media) │
│   DB)   │ │ session│ │        │ │         │
└─────────┘ └──────┘ └────────┘ └─────────┘
     │
     ▼
┌─────────────────────────────────────────────────────┐
│              n8n Automation Server                   │
│  ┌───────────────────────────────────────────┐     │
│  │ • Daily Calendar Updates                   │     │
│  │ • AI Translation Pipeline (SK ↔ HU)       │     │
│  │ • Automated Backups                        │     │
│  │ • Email Notifications                      │     │
│  │ • Social Media Posts                       │     │
│  │ • Media Processing                         │     │
│  └───────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────┘
```

### Data Flow Examples

**1. User Registration Flow:**
```
User submits registration
  ↓
FastAPI validates data
  ↓
Hash password (bcrypt)
  ↓
Save to PostgreSQL (users table)
  ↓
Generate verification token
  ↓
n8n sends verification email
  ↓
User clicks link
  ↓
Account activated
  ↓
Welcome email sent
```

**2. Daily Calendar Update Flow:**
```
n8n triggers at 00:01
  ↓
Python script generates daily readings
  ↓
Claude API translates to Hungarian
  ↓
Save to PostgreSQL (calendar_events)
  ↓
Invalidate Redis cache
  ↓
Send newsletter to subscribed users
  ↓
Post to social media
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

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_verified ON users(is_verified);
```

#### calendar_events
```sql
CREATE TABLE calendar_events (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    event_type VARCHAR(50), -- 'feast', 'fast', 'saint_day'
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

CREATE INDEX idx_calendar_date ON calendar_events(date);
CREATE INDEX idx_calendar_type ON calendar_events(event_type);
```

#### prayers
```sql
CREATE TABLE prayers (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(100) UNIQUE NOT NULL,
    category VARCHAR(50), -- 'morning', 'evening', 'akathist', 'canon'
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

CREATE INDEX idx_prayers_category ON prayers(category);
CREATE INDEX idx_prayers_published ON prayers(is_published);
CREATE INDEX idx_prayers_slug ON prayers(slug);
```

#### books
```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(100) UNIQUE NOT NULL,
    title_sk VARCHAR(255) NOT NULL,
    title_hu VARCHAR(255),
    author VARCHAR(255),
    category VARCHAR(50), -- 'patrology', 'lives', 'catechism', 'bible'
    description_sk TEXT,
    description_hu TEXT,
    content_sk TEXT,
    content_hu TEXT,
    pdf_url VARCHAR(500),
    cover_image_url VARCHAR(500),
    isbn VARCHAR(20),
    published_year INTEGER,
    is_published BOOLEAN DEFAULT FALSE,
    views_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_books_category ON books(category);
CREATE INDEX idx_books_slug ON books(slug);
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

CREATE INDEX idx_churches_city ON churches(city);
CREATE INDEX idx_churches_active ON churches(is_active);
```

#### media_files
```sql
CREATE TABLE media_files (
    id SERIAL PRIMARY KEY,
    type VARCHAR(20), -- 'audio', 'video', 'pdf'
    title_sk VARCHAR(255) NOT NULL,
    title_hu VARCHAR(255),
    description_sk TEXT,
    description_hu TEXT,
    file_url VARCHAR(500) NOT NULL,
    thumbnail_url VARCHAR(500),
    duration INTEGER, -- seconds
    file_size INTEGER, -- bytes
    transcription TEXT,
    category VARCHAR(50),
    is_published BOOLEAN DEFAULT FALSE,
    views_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_media_type ON media_files(type);
CREATE INDEX idx_media_category ON media_files(category);
```

#### user_bookmarks
```sql
CREATE TABLE user_bookmarks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    content_type VARCHAR(20), -- 'prayer', 'book', 'media'
    content_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, content_type, content_id)
);

CREATE INDEX idx_bookmarks_user ON user_bookmarks(user_id);
```

#### notifications
```sql
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    type VARCHAR(50), -- 'new_content', 'daily_reading', 'feast_reminder'
    title VARCHAR(255),
    message TEXT,
    link VARCHAR(500),
    is_read BOOLEAN DEFAULT FALSE,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_notifications_user ON notifications(user_id);
CREATE INDEX idx_notifications_read ON notifications(is_read);
```

### MongoDB Collections

#### saints (MongoDB - flexible schema)
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
  "miracles": [
    {
      "title": "...",
      "description": "..."
    }
  ],
  "prayers": ["..."],
  "related_saints": [ObjectId, ObjectId],
  "created_at": ISODate,
  "updated_at": ISODate
}
```

---

## 🔐 USER MANAGEMENT SYSTEM

### Authentication Flow

1. **Registration:**
   - User fills email + password
   - Backend validates, hashes password
   - Creates unverified account
   - Sends verification email
   - User clicks link → account verified

2. **Login:**
   - User enters email + password
   - Backend validates credentials
   - Issues JWT access token (15 min) + refresh token (7 days)
   - Stores refresh token in Redis
   - Returns tokens to client

3. **Token Refresh:**
   - Client sends refresh token
   - Backend validates, issues new access token
   - Optional: rotate refresh token

4. **Password Reset:**
   - User requests reset
   - Backend sends reset link (valid 1 hour)
   - User clicks link, enters new password
   - Backend updates password

### User Settings

```python
class UserSettings:
    language: str = 'sk'  # 'sk' or 'hu'
    theme: str = 'light'  # 'light', 'dark', 'auto'
    email_notifications: bool = True
    push_notifications: bool = False
    notification_types: {
        'daily_readings': True,
        'feast_days': True,
        'new_content': False,
        'newsletter': True
    }
    default_prayer_text: str = 'modern'  # 'modern', 'slavonic'
```

### Notification Types

1. **Daily Readings** - Každé ráno 7:00
2. **Feast Day Reminders** - Deň pred sviatkom
3. **New Content** - Pri pridaní nového obsahu
4. **Newsletter** - Týždenný/mesačný súhrn

---

## 🚀 STORIES & DEVELOPMENT PLAN

### STORY 1: Základná Infraštruktúra ⚙️
**Status:** 🔄 In Progress  
**Priority:** CRITICAL  
**Estimated:** 3-4 týždne

**Tasks:**
- [x] 1.1 - Git repository setup
- [ ] 1.2 - Folder structure creation
- [ ] 1.3 - FastAPI základná aplikácia
- [ ] 1.4 - PostgreSQL databáza setup
- [ ] 1.5 - MongoDB setup (optional pre štart)
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
**Estimated:** 2-3 týždne

### STORY 3: Modlitby a Bohoslužby 🙏
**Status:** ⏳ Planned  
**Priority:** HIGH  
**Estimated:** 3-4 týždne

### STORY 4: AI Preklad Systém 🤖
**Status:** ⏳ Planned  
**Priority:** HIGH  
**Estimated:** 2 týždne

### STORY 5: Knižnica a Obsahový Systém 📚
**Status:** ⏳ Planned  
**Priority:** MEDIUM  
**Estimated:** 3 týždne

### STORY 6: Médiá (Audio/Video) 🎬
**Status:** ⏳ Planned  
**Priority:** MEDIUM  
**Estimated:** 2 týždne

### STORY 7: Mapa Chrámov a Komunita 🗺️
**Status:** ⏳ Planned  
**Priority:** LOW  
**Estimated:** 1-2 týždne

### STORY 8: User Management & Notifications 🔔
**Status:** 🔄 In Progress (súčasť STORY 1)  
**Priority:** HIGH  
**Estimated:** 2 týždne

**Tasks:**
- [ ] 8.1 - User registration endpoint
- [ ] 8.2 - Email verification system
- [ ] 8.3 - JWT authentication
- [ ] 8.4 - User profile management
- [ ] 8.5 - Password reset flow
- [ ] 8.6 - Email notification system (n8n)
- [ ] 8.7 - Push notifications setup
- [ ] 8.8 - Newsletter subscription
- [ ] 8.9 - User preferences/settings
- [ ] 8.10 - Bookmarks system
- [ ] 8.11 - Reading progress tracking
- [ ] 8.12 - OAuth2 integration (Google, Facebook)

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
  5. Email - Send to subscribed users (if enabled)
  6. Social Media - Post to Facebook/Instagram
```

### 2. User Registration Welcome
```yaml
Trigger: Webhook - new user registered
Steps:
  1. Generate verification token
  2. Email - Send verification email
  3. Wait for verification
  4. Email - Send welcome email
  5. PostgreSQL - Update user preferences
```

### 3. Daily Notifications
```yaml
Trigger: Cron - každý deň 07:00
Steps:
  1. PostgreSQL - Get users with daily_notifications=true
  2. Get today's readings from calendar_events
  3. For each user:
     - Email - Send daily reading
     - Push - Send push notification (if enabled)
  4. PostgreSQL - Log sent notifications
```

### 4. Content Translation Pipeline
```yaml
Trigger: Webhook - new content added
Steps:
  1. PostgreSQL - Fetch untranslated content
  2. Claude API - Translate SK → HU
  3. Quality Check - Validate glossary terms
  4. Email - Notify admin for review
  5. Wait for approval
  6. PostgreSQL - Save translation
  7. Redis - Clear content cache
```

### 5. Weekly Newsletter
```yaml
Trigger: Cron - každú nedeľu 18:00
Steps:
  1. PostgreSQL - Get this week's highlights
  2. Generate HTML email template
  3. PostgreSQL - Get subscribed users
  4. For each user:
     - Personalize content (language)
     - Email - Send newsletter
  5. Track open rates, clicks
```

---

## 🎨 DESIGN SYSTEM

### Color Palette

```css
:root {
  /* Primary Colors */
  --primary: #8B4513;        /* Sienna Brown - ikony, drevo */
  --primary-dark: #654321;
  --primary-light: #A0522D;
  
  /* Secondary Colors */
  --secondary: #DAA520;      /* Goldenrod - svätosť, ikony */
  --secondary-dark: #B8860B;
  --secondary-light: #FFD700;
  
  /* Accent Colors */
  --accent: #B22222;         /* Firebrick Red - liturgia */
  --accent-dark: #8B0000;
  --accent-light: #CD5C5C;
  
  /* Neutral Colors */
  --background: #F5F5DC;     /* Beige - pergamen */
  --background-dark: #E6E6D0;
  --surface: #FFFFFF;
  --text: #2F4F4F;           /* Dark Slate Gray */
  --text-light: #696969;
  --border: #D3D3D3;
  
  /* Dark Mode */
  --dark-bg: #1A1A1A;
  --dark-surface: #2D2D2D;
  --dark-text: #E5E5E5;
  
  /* Status Colors */
  --success: #228B22;
  --warning: #FF8C00;
  --error: #DC143C;
  --info: #4169E1;
}
```

### Typography

```css
/* Font Families */
--font-heading: 'Georgia', 'Times New Roman', serif;
--font-body: 'Open Sans', 'Segoe UI', sans-serif;
--font-slavonic: 'Monomakh Unicode', 'Ponomar Unicode', serif;
--font-mono: 'Consolas', 'Monaco', monospace;

/* Font Sizes */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */
```

### Components

- **Buttons:** Rounded, shadow on hover
- **Cards:** White bg, subtle shadow, rounded corners
- **Inputs:** Clear labels, validation states
- **Navigation:** Fixed top, responsive hamburger menu
- **Icons:** Lucide React / Heroicons

---

## 📱 RESPONSIVE DESIGN

### Breakpoints

```css
/* Mobile First */
--mobile: 0px;
--tablet: 640px;
--laptop: 1024px;
--desktop: 1280px;
--wide: 1536px;
```

### Key Features

- ✅ Mobile-first approach
- ✅ Touch-friendly (min 44px tap targets)
- ✅ Responsive images
- ✅ Flexible grid layout
- ✅ Accessible navigation
- ✅ PWA installable

---

## 🔄 GIT WORKFLOW

### Branches

```
main (production, protected)
  └─ develop (development, protected)
       ├─ feature/liturgical-calendar
       ├─ feature/user-auth
       ├─ feature/prayers-library
       └─ hotfix/critical-bug
```

### Commit Convention

```
feat: Add liturgický kalendár API endpoint
fix: Fix Pascha calculation for leap years
docs: Update MASTER_CONTEXT with user schema
refactor: Improve translation service caching
test: Add unit tests for calendar service
chore: Update dependencies to latest versions
style: Format code with black
perf: Optimize database queries for prayers
ci: Add GitHub Actions workflow
```

### Commit Process

```bash
# 1. Pull latest
git pull origin develop

# 2. Create feature branch
git checkout -b feature/my-feature

# 3. Make changes...

# 4. Run tests
pytest tests/

# 5. Format code
black app/ scripts/
flake8 app/ scripts/

# 6. Commit
git add .
git commit -m "feat: Add user registration endpoint

- Created /api/auth/register endpoint
- Added email validation
- Integrated with PostgreSQL users table
- Added verification email sending via n8n

STORY-8 Task 8.1 complete"

# 7. Push
git push origin feature/my-feature

# 8. Create Pull Request on GitHub
# 9. Review & Merge to develop
# 10. Deploy from develop to staging
# 11. Merge develop → main for production
```

---

## 🧪 TESTING STRATEGY

### Test Pyramid

```
         /\
        /E2E\         (Few - Critical flows)
       /------\
      /  API  \       (More - All endpoints)
     /----------\
    /    UNIT    \    (Most - All functions)
   /--------------\
```

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

- [ ] Server access (SSH)
- [ ] Domain registered (pravoslavie.sk)
- [ ] DNS configured
- [ ] SSL certificate (Let's Encrypt)
- [ ] PostgreSQL installed & configured
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
- [ ] Monitoring setup

---

## 🔒 SECURITY

### Best Practices

- ✅ HTTPS only (SSL/TLS)
- ✅ Password hashing (bcrypt)
- ✅ JWT tokens with expiration
- ✅ Rate limiting
- ✅ CSRF protection
- ✅ SQL injection prevention (SQLAlchemy)
- ✅ XSS prevention (template escaping)
- ✅ Input validation (Pydantic)
- ✅ Environment variables for secrets
- ✅ Regular security updates

### Secrets Management

```bash
# .env file (NEVER commit to Git)
DATABASE_URL=postgresql://user:pass@localhost/dbname
REDIS_URL=redis://localhost:6379
JWT_SECRET=random-secret-key
ANTHROPIC_API_KEY=sk-ant-...
SMTP_PASSWORD=...
```

---

## 📊 MONITORING & ANALYTICS

### Metrics to Track

- **Performance:** Response times, database queries
- **Users:** Registrations, logins, active users
- **Content:** Most viewed prayers, books, media
- **Errors:** 500 errors, failed API calls
- **Infrastructure:** CPU, RAM, disk usage

### Tools

- **Application:** Built-in logging
- **Infrastructure:** Prometheus + Grafana (optional)
- **User Analytics:** Google Analytics / Matomo
- **Uptime:** UptimeRobot

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

### AI Services

- **Anthropic Claude:** https://docs.anthropic.com/
- **OpenAI Whisper:** https://github.com/openai/whisper

---

## ⚠️ CRITICAL REMINDERS

### Pre každý nový chat:

1. 🔥 **VŽDY NAJPRV** načítaj GitHub súbory
2. 🔥 **NIKDY** nepredpokladaj štruktúru projektu
3. 🔥 **VŽDY** over aktuálny stav v PROJECT_STATUS.md
4. 🔥 **VŽDY** commit + push po dokončení práce
5. 🔥 **VŽDY** aktualizuj session notes

### Git Rules:

- ✅ Commit často, malé zmeny
- ✅ Opisné commit messages
- ✅ Test pred commit
- ✅ Pull pred push
- ✅ Feature branches pre nové features

### Documentation Rules:

- ✅ Update MASTER_CONTEXT pri architektonických zmenách
- ✅ Session notes každý deň
- ✅ Code comments v slovenčine
- ✅ API dokumentácia vždy aktuálna

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

### V2.0 Features (Future)

- ✅ Mobilná aplikácia (React Native)
- ✅ Offline mode (full PWA)
- ✅ Live streaming bohoslužieb
- ✅ AI chatbot pre duchovné otázky
- ✅ VR prehliadky chrámov
- ✅ Donation system

---

**Document Version:** 1.0  
**Created:** 2025-10-19  
**Last Updated:** 2025-10-19  
**Status:** Initial Setup  
**Next:** Begin STORY 1 Implementation

🕊️ **S Bohom!**