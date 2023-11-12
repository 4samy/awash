release: flask db init
web: gunicorn wsgi:app

db_init: python -c "from api import db; db.create_all()"
db_upgrade: python manage.py db upgrade
