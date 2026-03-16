# САЙТ НА ДЖАНГО
1. Клонируем реп.
```bash
git clone https://github.com/Firas15/first_web_site_dj.git
```
2. Создаем вирт. окр.
```bash
python -m venv venv
```
3. Активация вирт. окр.
```bash
venv\scripts\activate
```
4. Установка зависимостей проекта
```bash
pip install -r requirements.txt
```
5. Создаем миграцию
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Запуск сервера
```bash
python manage.py runserver
```