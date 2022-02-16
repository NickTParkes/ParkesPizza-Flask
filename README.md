# Pizza Ordering Flask App (In Development)

This is a webapp hosted on Heroku using Python, the Flask framework, Jinja2, and Postgresql.

The app includes:

- SQL Alchemy ORM
- DB Migration
- Object Configuration
- Local/Production Configuration
- Form Validation
- User Registration and Login
- Session tracking

# Local Installation Setup

1. Pull main branch.
2. Run "pip install -r requirements.txt" in the root folder.
3. Set required environmental vars using a ".env" file in the root folder. (Required variables listed below)
4. Run "flask run"

# Required Environmental Variables

- ENV_VAR='local'
- FLASK_APP=wsgi.py
- LOCAL_DB=postgresql://LOCAL_DB_PATH
- SECRET_KEY=SET_DEFAULT_KEY_AS_SECRET
