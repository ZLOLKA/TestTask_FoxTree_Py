#!/bin/bash

cmd="$@"

>&2 echo "!!!!!!!! Check PostgreSQL for available !!!!!!!!"
curl http://"$SQL_HOST":"$SQL_PORT" &> /dev/null
until [ $? -eq "52" ]; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
  curl http://"$SQL_HOST":"$SQL_PORT" &> /dev/null
done
>&2 echo "PostgreSQL is up - executing command"


#>&2 echo "Collect static files"
#python manage.py collectstatic --noinput

>&2 echo "Make migrations"
python manage.py makemigrations

>&2 echo "Migration"
python manage.py migrate

>&2 echo "Create super user"
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_NAME

>&2 echo "Server start"
python manage.py runserver 0.0.0.0:8000

exec $cmd
