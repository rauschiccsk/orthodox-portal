@echo off
REM Monastier Online - Folder Structure Creation Script (Windows)
REM Vytvorí kompletnú štruktúru priečinkov a súborov

echo 🕊️ Monastier Online - Creating project structure...
echo.

REM Hlavné priečinky aplikácie
mkdir app\api\v1 2>nul
mkdir app\core 2>nul
mkdir app\models 2>nul
mkdir app\schemas 2>nul
mkdir app\services 2>nul
mkdir app\db\repositories 2>nul
mkdir app\utils 2>nul
mkdir app\middleware 2>nul
mkdir app\tasks 2>nul

REM Frontend
mkdir frontend\templates\auth 2>nul
mkdir frontend\templates\calendar 2>nul
mkdir frontend\templates\prayers 2>nul
mkdir frontend\templates\books 2>nul
mkdir frontend\templates\media 2>nul
mkdir frontend\templates\churches 2>nul
mkdir frontend\templates\admin 2>nul
mkdir frontend\templates\partials 2>nul
mkdir frontend\static\css 2>nul
mkdir frontend\static\js 2>nul
mkdir frontend\static\img\icons 2>nul
mkdir frontend\static\fonts 2>nul

REM Database migrations
mkdir alembic\versions 2>nul

REM Tests
mkdir tests\unit 2>nul
mkdir tests\integration 2>nul
mkdir tests\e2e 2>nul

REM Scripts
mkdir scripts 2>nul

REM n8n workflows
mkdir n8n 2>nul

REM Config
mkdir config 2>nul

REM Documentation
mkdir docs\sessions 2>nul

REM Data
mkdir data\calendar 2>nul
mkdir data\translations 2>nul
mkdir data\backup 2>nul

REM Logs
mkdir logs 2>nul

echo ✅ Folders created!
echo.
echo Creating __init__.py files...

REM Create __init__.py files
type nul > app\__init__.py
type nul > app\api\__init__.py
type nul > app\api\v1\__init__.py
type nul > app\core\__init__.py
type nul > app\models\__init__.py
type nul > app\schemas\__init__.py
type nul > app\services\__init__.py
type nul > app\db\__init__.py
type nul > app\db\repositories\__init__.py
type nul > app\utils\__init__.py
type nul > app\middleware\__init__.py
type nul > app\tasks\__init__.py
type nul > tests\__init__.py

echo ✅ __init__.py files created!
echo.
echo Creating main application files...

REM Main app files
type nul > app\main.py
type nul > app\config.py
type nul > app\dependencies.py

REM API endpoints
type nul > app\api\v1\calendar.py
type nul > app\api\v1\prayers.py
type nul > app\api\v1\books.py
type nul > app\api\v1\media.py
type nul > app\api\v1\churches.py
type nul > app\api\v1\saints.py
type nul > app\api\v1\auth.py
type nul > app\api\deps.py

REM Core
type nul > app\core\security.py
type nul > app\core\config.py
type nul > app\core\cache.py
type nul > app\core\logging.py

REM Models
type nul > app\models\base.py
type nul > app\models\user.py
type nul > app\models\calendar.py
type nul > app\models\prayer.py
type nul > app\models\book.py
type nul > app\models\church.py
type nul > app\models\media.py
type nul > app\models\bookmark.py
type nul > app\models\notification.py

REM Schemas
type nul > app\schemas\user.py
type nul > app\schemas\calendar.py
type nul > app\schemas\prayer.py
type nul > app\schemas\book.py
type nul > app\schemas\church.py
type nul > app\schemas\media.py
type nul > app\schemas\auth.py
type nul > app\schemas\common.py

REM Services
type nul > app\services\auth_service.py
type nul > app\services\calendar_service.py
type nul > app\services\translation_service.py
type nul > app\services\email_service.py
type nul > app\services\notification_service.py
type nul > app\services\search_service.py
type nul > app\services\media_service.py

REM Database
type nul > app\db\session.py
type nul > app\db\base.py
type nul > app\db\init_db.py
type nul > app\db\repositories\base.py
type nul > app\db\repositories\user.py
type nul > app\db\repositories\calendar.py
type nul > app\db\repositories\prayer.py

REM Utils
type nul > app\utils\pascha.py
type nul > app\utils\liturgical.py
type nul > app\utils\slug.py
type nul > app\utils\validators.py
type nul > app\utils\helpers.py

REM Middleware
type nul > app\middleware\rate_limit.py
type nul > app\middleware\logging.py
type nul > app\middleware\error_handler.py

REM Tasks
type nul > app\tasks\celery_app.py
type nul > app\tasks\calendar_tasks.py
type nul > app\tasks\notification_tasks.py

echo ✅ Application files created!
echo.
echo Creating frontend files...

REM Templates - Base
type nul > frontend\templates\base.html
type nul > frontend\templates\index.html

REM Templates - Auth
type nul > frontend\templates\auth\login.html
type nul > frontend\templates\auth\register.html
type nul > frontend\templates\auth\reset_password.html

REM Templates - Calendar
type nul > frontend\templates\calendar\index.html
type nul > frontend\templates\calendar\day.html

REM Templates - Prayers
type nul > frontend\templates\prayers\index.html
type nul > frontend\templates\prayers\detail.html

REM Templates - Books
type nul > frontend\templates\books\index.html
type nul > frontend\templates\books\read.html

REM Templates - Media
type nul > frontend\templates\media\index.html

REM Templates - Churches
type nul > frontend\templates\churches\map.html

REM Templates - Admin
type nul > frontend\templates\admin\dashboard.html
type nul > frontend\templates\admin\content.html
type nul > frontend\templates\admin\users.html

REM Templates - Partials
type nul > frontend\templates\partials\header.html
type nul > frontend\templates\partials\footer.html
type nul > frontend\templates\partials\navigation.html

REM Static files
type nul > frontend\static\css\tailwind.css
type nul > frontend\static\css\custom.css
type nul > frontend\static\js\main.js
type nul > frontend\static\js\calendar.js
type nul > frontend\static\js\alpine-components.js
type nul > frontend\static\img\logo.svg
type nul > frontend\static\manifest.json

echo ✅ Frontend files created!
echo.
echo Creating other files...

REM Alembic
type nul > alembic\env.py
type nul > alembic\script.py.mako

REM Tests
type nul > tests\conftest.py
type nul > tests\unit\test_auth.py
type nul > tests\unit\test_calendar.py
type nul > tests\unit\test_services.py
type nul > tests\integration\test_api_auth.py
type nul > tests\integration\test_api_calendar.py
type nul > tests\integration\test_database.py
type nul > tests\e2e\test_user_journey.py

REM Scripts
type nul > scripts\init_db.py
type nul > scripts\seed_data.py
type nul > scripts\backup_db.py
type nul > scripts\import_calendar.py
type nul > scripts\translate_batch.py

REM Config
type nul > config\config_template.py
type nul > config\nginx.conf
type nul > config\systemd_service.txt
type nul > config\gunicorn_conf.py

REM Root files
type nul > .gitignore
type nul > .env.example
type nul > README.md
type nul > requirements.txt
type nul > alembic.ini

REM Documentation (only create if not exists)
if not exist docs\FULL_PROJECT_CONTEXT.md type nul > docs\FULL_PROJECT_CONTEXT.md
if not exist docs\PROJECT_STATUS.md type nul > docs\PROJECT_STATUS.md
type nul > docs\MASTER_CONTEXT.md
type nul > docs\API_DOCUMENTATION.md
type nul > docs\DEPLOYMENT.md
type nul > docs\CONTRIBUTING.md

echo ✅ All files created!
echo.
echo Creating data files...

REM Data files
type nul > data\calendar\fixed_feasts.json
type nul > data\calendar\movable_feasts.json
type nul > data\calendar\readings_2025.json
type nul > data\translations\liturgical_terms_sk.json
type nul > data\translations\liturgical_terms_hu.json

echo ✅ Data files created!
echo.
echo 🎉 Project structure complete!
echo.
echo 📁 Structure created in: %CD%
echo.
echo Next steps:
echo 1. Review the structure
echo 2. Update .gitignore file
echo 3. Create .env file from .env.example
echo 4. Start with Task 1.3 - FastAPI základná aplikácia
echo.
echo 🕊️ S Bohom!
echo.
pause