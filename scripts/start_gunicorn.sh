#!/bin/bash
SERVER=0.0.0.0
PORT=8000
PROJECT_DIR=/app
USER=root
DJANGO_SETTINGS_MODULE=config.settings
TIMEOUT=60
GUNICORN="gunicorn -b $SERVER:$PORT config.wsgi --timeout ${TIMEOUT} --preload --log-level debug --access-logfile -"
BASE_CMD="$GUNICORN"

echo
echo
env |sort
echo
echo


if [ ${DJANGO_ENV} == "production" ] || [ ${DJANGO_ENV} == "staging" ]; then
  echo "DJANGO_ENV: ${DJANGO_ENV}"
  echo
  echo "Uploading Static files to S3..."
  python src/manage.py migrate --settings config.settings.${DJANGO_ENV}
  python src/manage.py collectstatic --no-input --settings config.settings.${DJANGO_ENV}
  echo
  echo "DONE Uploading Static files to S3"
fi

if [[ -z "${DJANGO_ENV}" ]]; then
  START="$BASE_CMD --env DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}"
else
  START="$BASE_CMD --env DJANGO_SETTINGS_MODULE=config.settings"
fi

echo $START
cd ${PROJECT_DIR}/src
echo "starting ${SERVER}:${1}"
$START
sleep 1

exit 0
