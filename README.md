# Django Rest API

Basic REST API server

Features checklist:

* Admin panel (Django built-in) ✔
* oAuth + JWT authentication ✔
* Automated testing ✔
* User 
  * Profile
  * Registration
  * Reset password
  * Delete own account
* Push notification (Firebase)

Prerequisites:

1. Python 3.x
2. Sqlite3 (or other RDBMS supported by Django)

Installation:

1. Install dependencies `pip install -r requirements.txt`
2. Migrate database schema `python manage.py runserver`
3. Create first admin `python manage.py createsuperuser --email admin@example.com --username admin`
4. Run test `python manage.py test`
5. Run API server `python manage.py runserver`
