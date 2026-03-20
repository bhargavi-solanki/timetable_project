<<<<<<< HEAD
# Automated Timetable Generator

A Django-based web application for generating conflict-free timetables for educational institutions.

## Features
- Department, Faculty, Course, Classroom Management
- Student Groups with multiple divisions
- Automatic Timetable Generation
- Timetable views by Group, Faculty, Room
- 2-5 lectures per day per group

## Setup Instructions

### 1. Requirements
- Python 3.8+
- MySQL Server
- Django 5.0+

### 2. Install Dependencies
```bash
pip install django mysqlclient
```

### 3. Database Setup
Create a MySQL database:
```sql
CREATE DATABASE timetable_db;
```

### 4. Configure Settings
Edit `timetable_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'timetable_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Server
```bash
python manage.py runserver
```

### 8. Access Application
- Admin Panel: http://127.0.0.1:8000/admin/
- Main App: http://127.0.0.1:8000/

## Default Login
- Username: admin
- Password: admin123

## Project Structure
```
ADSC/
├── timetable_project/    # Django project settings
├── timetable/            # Main app with models, views
├── templates/            # HTML templates
└── manage.py
```

## Color Scheme
- Primary Blue: #4361ee
- Dark Navy: #1a1a2e
- Teal: #2ec4b6
- Orange: #f77f00

## License
Educational Use
=======
# timetable_project
This project is an Automated Time Table Generator that helps in creating optimized and conflict-free timetables for students and faculty. It reduces manual effort and ensures efficient scheduling of lectures.

FEATURES :
-> Automatically generates timetable
-> Supports multiple subjects and faculty
-> Customizable lecture limits (min & max)
-> Easy to use interface

TECHNOLOGY USED :
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: MYSQL
>>>>>>> 9c7d92809a1a042ec1bad31b3b471c0b2827e68e
