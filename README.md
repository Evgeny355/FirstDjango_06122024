# FirstDjango_05122024

## Инструкция по развертыванию проекта
1. создание виртуального окружения     "python3 -m venv django_venv"

2. активация виртуального окружения    "source djang_venv/bin/activate"

3. содержание пакетовЁ которые были установлены в данное виртуальное окружение    "pip install -r requirements.txt" 

4. запуск нашего проекта    "python manage.py runserver"

## Дополнительно!!
1. Полезное дополнение для шаблонов   "установить дополнение "Django" и внизу код для вставки в настройки json, чтобы файл с расширением html воспринимался как шаблон django"
"""
extensions install batisteo.vscode-django
""" 
Добавить в "settings.json"
"""
"emmet.includeLanguages": {
    "django-html": "html",
    },
"files.associations": {
    "*.html": "django-html"
    }
"""