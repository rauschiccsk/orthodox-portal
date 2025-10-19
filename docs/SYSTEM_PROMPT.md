# 🕊️ MONASTIER ONLINE - SYSTEM PROMPT

## 🎯 PROJEKT OVERVIEW

**Názov:** Monastier Online  
**Doména:** monastier.online  
**Účel:** Centrálny pravoslávny portál pre slovenských a maďarských veriacich  
**GitHub:** https://github.com/rauschiccsk/orthodox-portal  
**Email:** monastierkomarno@gmail.com

---

## 🚨 PRAVIDLO #1: VŽDY NAJPRV GITHUB PRÍSTUP

**KRITICKÉ:** Pred akoukoľvek prácou na projekte MUSÍŠ:

### 1. ✅ Načítať project_file_access.json:
```
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/project_file_access.json
```

### 2. ✅ Načítať FULL_PROJECT_CONTEXT.md:
```
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/FULL_PROJECT_CONTEXT.md
```

### 3. ✅ Načítať PROJECT_STATUS.md:
```
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/PROJECT_STATUS.md
```

### 4. ✅ Načítať konfiguráciu:
```
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/config/config_template.py
```

**⚠️ AK NEMÔŽEŠ NAČÍTAŤ SÚBORY Z GITHUB → ZASTAV A POVEDZ TO!**  
**⚠️ NIKDY NEPREDPOKLADAJ ŠTRUKTÚRU PROJEKTU! VŽDY NAJPRV OVER V GITHUB!**

---

## 📊 PROJECT INFO

### Základné údaje
- **Tech Stack:** Python 3.11+, FastAPI, PostgreSQL, MongoDB, Redis
- **AI:** Anthropic Claude API (preklad SK ↔ HU)
- **Automation:** n8n workflows
- **Development:** C:\Development\orthodox-portal
- **Deployment:** C:\Deployment\orthodox-portal

### GitHub Repository
```
URL: https://github.com/rauschiccsk/orthodox-portal
Branch: main (production)
Branch: develop (development)
```

### Aktuálny Stav
- **Phase:** Initial Setup / Development / Production
- **Active Story:** STORY X
- **Progress:** X/8 Stories Complete

---

## 🏗️ ARCHITEKTÚRA

### Flow
```
User (Browser)
  ↓ HTTPS
Nginx (reverse proxy)
  ↓
FastAPI (port 8000)
  ↓
PostgreSQL + MongoDB + Redis
  ↓
n8n workflows (automation)
```

### Kľúčové komponenty
1. **FastAPI** - REST API + web interface
2. **PostgreSQL** - hlavná databáza (monastier_online)
3. **MongoDB** - flexibilný obsah (životy svätých)
4. **Redis** - cache, sessions
5. **n8n** - automatizácia (preklady, notifikácie)
6. **Nginx** - reverse proxy, SSL

---

## 🎯 STORIES OVERVIEW

### STORY 1: Základná Infraštruktúra ⚙️
- FastAPI app, databázy, authentication, deployment

### STORY 2: Liturgický Kalendár 📅
- Pascha calculation, sviatky, denné čítania

### STORY 3: Modlitby a Bohoslužby 🙏
- Ranné/večerné modlitby, liturgie, akafisty

### STORY 4: AI Preklad Systém 🤖
- Claude API, SK ↔ HU translation

### STORY 5: Knižnica 📚
- Knihy, životy svätých, Biblia

### STORY 6: Médiá 🎬
- Audio/video liturgií, podcast

### STORY 7: Mapa Chrámov 🗺️
- Chrámy na SK/HU, bohoslužby

### STORY 8: User Management 🔔
- Registrácia, notifikácie, newsletter

---

## 🔄 PRAVIDLÁ PRÁCE

### Pri každom novom chate:
1. 🔥 **VŽDY** načítaj GitHub súbory NAJPRV
2. 🔥 **VŽDY** over aktuálny stav v PROJECT_STATUS.md
3. 🔥 **VŽDY** commit + push po dokončení práce
4. 🔥 **VŽDY** aktualizuj session notes

### Git workflow:
- ✅ Commit často, malé zmeny
- ✅ Opisné commit messages (feat/fix/docs/refactor/test/chore)
- ✅ Test pred commit
- ✅ Pull pred push
- ✅ Feature branches pre nové features

### Documentation:
- ✅ Update FULL_PROJECT_CONTEXT pri veľkých zmenách
- ✅ Update PROJECT_STATUS po každej session
- ✅ Session notes každý deň
- ✅ Code comments v slovenčine

---

## 📝 COMMIT MESSAGE CONVENTION

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

**Príklad:**
```bash
git commit -m "feat: Add liturgical calendar API endpoint

- Created /api/calendar/daily endpoint
- Added Pascha calculation algorithm
- Integrated with PostgreSQL calendar_events table
- Added unit tests for date validation

STORY-2 Task 2.1 complete"
```

---

## 🔐 SECURITY & BEST PRACTICES

- ✅ HTTPS only (SSL/TLS)
- ✅ Password hashing (bcrypt)
- ✅ JWT tokens with expiration
- ✅ Rate limiting
- ✅ Input validation (Pydantic)
- ✅ Environment variables for secrets
- ✅ **NEVER** commit config.py, .env files

---

## 📞 KONTAKT & RESOURCES

### Email
- **Projekt:** monastierkomarno@gmail.com
- **SMTP:** monastierkomarno@gmail.com

### GitHub
- **Repo:** https://github.com/rauschiccsk/orthodox-portal
- **Issues:** https://github.com/rauschiccsk/orthodox-portal/issues

### Dokumentácia
- **FULL_PROJECT_CONTEXT:** Kompletný kontext projektu
- **PROJECT_STATUS:** Aktuálny stav a progress
- **MASTER_CONTEXT:** Architektonické detaily
- **Stories:** docs/stories/STORY-X-design.md

### AI Services
- **Claude API:** Anthropic (preklad)
- **Whisper:** OpenAI (transcription)

---

## ⚠️ CRITICAL REMINDERS

1. 🔥 **VŽDY NAJPRV** načítaj GitHub súbory
2. 🔥 **NIKDY** nepredpokladaj štruktúru
3. 🔥 **VŽDY** over stav pred prácou
4. 🔥 **VŽDY** commit po dokončení
5. 🔥 **VŽDY** dokumentuj zmeny

---

## 🎯 TEMPLATE PRE NOVÝ CHAT

```markdown
Pokračujeme na Monastier Online projekte.

KRITICKÉ - Najprv načítaj GitHub súbory:
1. https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/project_file_access.json
2. https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/FULL_PROJECT_CONTEXT.md
3. https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/PROJECT_STATUS.md

GitHub: https://github.com/rauschiccsk/orthodox-portal
Aktuálny stav: [pozri PROJECT_STATUS.md]

Dnes chcem pracovať na: [STORY X, Task X.Y]
```

**Po načítaní odpovedz:**
```
✅ Projekt načítaný. Čo robíme?
```

---

## 📚 QUICK REFERENCE

### Kritické URL
```
Project Files:
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/project_file_access.json

Context:
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/FULL_PROJECT_CONTEXT.md

Status:
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/docs/PROJECT_STATUS.md

Config:
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/config/config_template.py

Requirements:
https://raw.githubusercontent.com/rauschiccsk/orthodox-portal/main/requirements.txt
```

### Common Commands
```bash
# Activate venv
cd C:\Development\orthodox-portal
venv\Scripts\activate

# Run app
python app/main.py
# alebo
uvicorn app.main:app --reload

# Test
pytest tests/

# Database
psql -U portal_user -d monastier_online

# Git
git status
git add .
git commit -m "feat: ..."
git push
```

---

**Last Updated:** 2025-10-19  
**Version:** 1.0.0  
**Status:** Active Development

🕊️ **S Bohom!**