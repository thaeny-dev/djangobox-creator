#!/usr/bin/env bash

DB_NAME='django_dev_db' # needs to be all lower case.
DB_USERNAME='vagrant'
DB_PASSWORD='pass'

echo "---------------------------------------------"
echo "Running vagrant bootstrap to install requirements"
echo "---------------------------------------------"

if [ "$(whoami)" != "root" ]; then
    echo "---------------------------------------------"
    echo "This script must be run as root!"
    echo "---------------------------------------------"
    exit 1
fi

echo "---------------------------------------------"
echo "updating apt-get"
echo "---------------------------------------------"
apt-get update

echo "---------------------------------------------"
echo "installing libpq-dev python-dev used by postgresql"
echo "---------------------------------------------"
apt-get install -y libpq-dev python-dev

echo "---------------------------------------------"
echo "installing postgresql"
echo "---------------------------------------------"
apt-get install -y postgresql postgresql-contrib

echo "---------------------------------------------"
echo "creating a database and user for postgresql"
echo "---------------------------------------------"

sudo su - postgres << START
createdb $DB_NAME
psql -c "CREATE ROLE $DB_USERNAME WITH LOGIN ENCRYPTED PASSWORD '$DB_PASSWORD';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USERNAME;"
START

echo "---------------------------------------------"
echo "installing install git"
echo "---------------------------------------------"
apt-get install -y git-core

echo "---------------------------------------------"
echo "installing install pip"
echo "---------------------------------------------"
apt-get install -y python-pip

echo "---------------------------------------------"
echo "installing django env based on a requirements file."
echo "---------------------------------------------"
pip install -r "django_shared/requirements.txt"

echo "---------------------------------------------"
echo " Finished."
echo "---------------------------------------------"

printf "Assuming there were no errors above with postgres, here'e the info for your settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '$DB_NAME',
        'USER': '$DB_USERNAME',
        'PASSWORD': '$DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"