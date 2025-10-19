# 🕊️ MONASTIER ONLINE - FULL PROJECT CONTEXT

**Complete Single Source of Truth**  
**Last Updated:** 2025-10-19  
**Version:** 1.1.0  
**Status:** Initial Setup - Development Phase

---

## 🤖 INSTRUCTIONS FOR CLAUDE

### When you see this document at the start of a conversation:

**STEP 1: Load Project File Access Map**
```
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/project_file_access.json
```

**STEP 2: Load All Critical Files**
- Parse the JSON file
- Load all files marked with `"always_load": true`
- Load all files with `"priority": 1` 
- Optionally load files with `"priority": 2`
- **SILENTLY SKIP** any files that don't exist (no error messages!)

**STEP 3: Respond to User**
```
✅ Projekt načítaný. Čo robíme?
```

### Critical Rules
- ✅ **NEVER** show error messages for missing files
- ✅ **NEVER** show warnings about files not found
- ✅ **ALWAYS** load silently - if file exists load it, if not skip it
- ✅ After loading, simply say "✅ Projekt načítaný. Čo robíme?"
- ✅ Use Slovak language for all communication
- ✅ Be concise and actionable

### What This Gives You
After loading, you will have access to:
- 📄 Complete project documentation and vision
- 📊 Current project status and progress
- 💻 All source code files (that exist)
- ⚙️ Configuration and settings
- 🧪 Tests and migrations
- 📝 Session notes and history

**You will see the COMPLETE project, not just documentation.**

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
```markdown
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
- [ ] 1.2 - Folder structure creation
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

---

## ⚠️ CRITICAL REMINDERS

### Pre každý nový chat:
1. 🔥 User pošle URL na FULL_PROJECT_CONTEXT.md
2. 🔥 Claude načíta tento dokument
3. 🔥 Claude načíta project_file_access.json
4. 🔥 Claude načíta všetky critical súbory
5. 🔥 Claude odpovie: "✅ Projekt načítaný. Čo robíme?"
6. 🔥 ŽIADNE varovania o chýbajúcich súboroch

### Git Rules:
- ✅ Commit často, malé zmeny
- ✅ Opisné commit messages
- ✅ Test pred commit
- ✅ Pull pred push
- ✅ Feature branches

### Documentation Rules:
- ✅ Update FULL_PROJECT_CONTEXT pri veľkých zmenách
- ✅ Update PROJECT_STATUS.md po každej session
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

## 📞 KONTAKT

- **Email:** monastierkomarno@gmail.com
- **GitHub:** https://github.com/rauschiccsk/orthodox-portal
- **Doména:** https://monastier.online
- **Developer:** rauschiccsk (ICC)

---

## 🤖 FINAL REMINDER FOR CLAUDE

**After loading all files, you should have complete visibility into:**
- ✅ Project vision and architecture
- ✅ Current status and progress
- ✅ All source code (that exists)
- ✅ Configuration
- ✅ Tests
- ✅ Documentation

**Simply respond:**
```
✅ Projekt načítaný. Čo robíme?
```

**Then wait for user's instruction.**

---

**Document Version:** 1.1.0  
**Created:** 2025-10-19  
**Last Updated:** 2025-10-19  
**Status:** Active Development  

🕊️ **S Bohom!**