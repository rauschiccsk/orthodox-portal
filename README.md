# 🕊️ Monastier Online (monastier.online)

Centrálny portál pre pravoslávnych veriacich na Slovensku a v Maďarsku.

## 📋 Prehľad

Pravoslávny portál poskytuje komplexný obsah pre pravoslávnych veriacich na jednom mieste:

- 📅 **Liturgický kalendár** - denné čítania, sviatky, posty
- 🙏 **Modlitby** - ranné, večerné, akafisty, bohoslužobné texty
- 📚 **Knižnica** - Biblia, životy svätých, duchovná literatúra
- 🎬 **Médiá** - audio/video nahrávky liturgií, prednášky
- 🗺️ **Mapa chrámov** - všetky pravoslávne chrámy na Slovensku
- 🔔 **Notifikácie** - denné pripomienky, novinky

## 🌍 Jazyky

- 🇸🇰 **Slovenčina** (primárne)
- 🇭🇺 **Maďarčina** (AI preklad)

## 🏗️ Tech Stack

- **Backend:** Python 3.11, FastAPI, SQLAlchemy
- **Database:** PostgreSQL 15, MongoDB, Redis
- **Frontend:** Jinja2, TailwindCSS, Alpine.js
- **Automation:** n8n workflows
- **AI:** Anthropic Claude (preklad)

## 📁 Štruktúra Projektu

```
orthodox-portal/
├── app/                    # FastAPI aplikácia
│   ├── routes/            # API endpoints
│   ├── models/            # Database models
│   ├── services/          # Business logic
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, images
├── scripts/               # Python utility scripts
├── n8n_workflows/         # Automation workflows
├── tests/                 # Unit & integration tests
├── docs/                  # Dokumentácia
│   ├── MASTER_CONTEXT.md # Single Source of Truth
│   ├── stories/          # Development stories
│   └── sessions/         # Daily work logs
└── config/               # Configuration files
```

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.11+
python --version

# PostgreSQL 15+
psql --version

# Redis
redis-cli --version
```

### Installation

```bash
# 1. Clone repository
git clone https://github.com/rauschiccsk/orthodox-portal.git
cd orthodox-portal

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# alebo
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy config template
cp config/config_template.py config/config.py
# Edit config/config.py with your settings

# 5. Setup database
python scripts/init_database.py

# 6. Run migrations
python scripts/migrate.py

# 7. Start application
python app/main.py
```

### Development Server

```bash
# Start FastAPI with hot reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Application will be available at:
# http://localhost:8000
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_calendar.py
```

## 📖 Dokumentácia

Kompletná dokumentácia je v priečinku `docs/`:

- **[MASTER_CONTEXT.md](docs/MASTER_CONTEXT.md)** - Single Source of Truth
- **[PROJECT_STATUS.md](docs/PROJECT_STATUS.md)** - Aktuálny stav projektu
- **[stories/](docs/stories/)** - Development stories & tasks
- **[architecture/](docs/architecture/)** - Architektonická dokumentácia
- **[sessions/](docs/sessions/)** - Daily work logs

## 🔐 Configuration

Vytvor `config/config.py` zo šablóny:

```python
# Database
DATABASE_URL = "postgresql://user:password@localhost/pravoslavny_portal"
REDIS_URL = "redis://localhost:6379"

# Security
JWT_SECRET = "your-secret-key-here"
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = 15

# Email
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your-email@gmail.com"
SMTP_PASSWORD = "your-app-password"

# AI Translation
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
```

**⚠️ NIKDY necommituj config.py do Git!**

## 🤖 n8n Automation

n8n workflows v priečinku `n8n_workflows/`:

1. **daily_calendar_update.json** - Denná aktualizácia kalendára
2. **content_translation.json** - AI preklad SK → HU
3. **user_notifications.json** - Email & push notifikácie
4. **automated_backup.json** - Automatické zálohy

Import do n8n cez UI → Import → Select JSON file

## 🌐 Deployment

### Production Server

```bash
# 1. Setup systemd service
sudo cp deployment/systemd/monastier-online.service /etc/systemd/system/
sudo systemctl enable monastier-online
sudo systemctl start monastier-online

# 2. Setup Nginx reverse proxy
sudo cp deployment/nginx.conf /etc/nginx/sites-available/monastier.online
sudo ln -s /etc/nginx/sites-available/monastier.online /etc/nginx/sites-enabled/
sudo systemctl reload nginx

# 3. SSL certificate (Let's Encrypt)
sudo certbot --nginx -d monastier.online -d www.monastier.online
```

## 📊 Development Stories

### Status

- ✅ **STORY 1:** Základná infraštruktúra (Complete)
- 🔄 **STORY 2:** Liturgický kalendár (In Progress)
- ⏳ **STORY 3:** Modlitby a bohoslužby (Planned)
- ⏳ **STORY 4:** AI preklad systém (Planned)
- ⏳ **STORY 5:** Knižnica (Planned)
- ⏳ **STORY 6:** Médiá (Planned)
- ⏳ **STORY 7:** Mapa chrámov (Planned)
- ⏳ **STORY 8:** User management (Planned)

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/my-feature`)
3. Commit changes (`git commit -m 'feat: Add feature'`)
4. Push to branch (`git push origin feature/my-feature`)
5. Open Pull Request

### Commit Convention

```
feat: Add new feature
fix: Fix bug
docs: Update documentation
refactor: Refactor code
test: Add tests
chore: Update dependencies
```

## 📝 License

Tento projekt je licencovaný pod MIT licenciou.

## 👥 Autori

- **ICC (monastierkomarno@gmail.com)** - Initial work & development

## 🙏 Poďakovanie

- **azbyka.ru** - Inšpirácia a vzor
- **posledovanie.ru** - Liturgické texty
- Všetkým duchovným za content review

## 📞 Kontakt

- **Web:** https://monastier.online
- **Email:** monastierkomarno@gmail.com
- **GitHub:** https://github.com/rauschiccsk/orthodox-portal

## 🔗 Užitočné Odkazy

- [Pravoslávna cirkevná obec Bratislava](https://pravoslavni.sk/)
- [Pravoslávna cirkev v českých zemích a na Slovensku](https://pravoslav.cz/)
- [Orthodox Church in America](https://www.oca.org/)

---

🕊️ **S Bohom!**

**Last Updated:** 2025-10-19  
**Version:** 1.0.0