@echo off
cd /d %~dp0

call .venv\Scripts\activate.bat


python manage.py makemigrations
python manage.py migrate
python manage.py runserver
pause