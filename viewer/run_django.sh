# description
sleep 15
python manage.py migrate
python manage.py migrate logs --database=logs_db
python manage.py migrate blogers --database=default
python manage.py mocks_users
python manage.py mocks_logs
python manage.py runserver 0.0.0.0:8000
