python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn project_framework.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 300 --log-level debug --log-file - --error-logfile - --access-logfile - --capture-output --daemon --pid /tmp/gunicorn.pid --reload --reload-engine auto --reload-restart-delay 1 --reload-restart-cmd "kill -USR2 `cat /tmp/gunicorn.pid`"