# Создание виртуального окружения

1. Создайте рабочую директорию 
2. Перейдите в созданную директорию через cmd или bash
3. Выполните команду 'python -m venv env'
4. Перейдите в папку './your-project-name/env/Scripts' и выполните команду 'source activate' в bash или выполните команду 'source env/Scripts/activate' в bash
5. Вернитесь на уровень проекта

# Создание Django проекта

1. Выполните команду 'pip install django';
2. Выполните команду 'django-admin startprojects <your-project-name>'
3. После выполнения команды из пункта 2 в вашей папке с проектом будет создана папка '<your-project-name>'. Зайдите в нее и выполните команду ('python manage.py startapp <you-app-name> в bash')
4. Для проверки корректности создания проекта выполните команду 'python manage.py runserver в gibash'
