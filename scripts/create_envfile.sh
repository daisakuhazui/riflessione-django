#!/bin/bash

env | sort | grep AWS_ > .env
env | sort | grep EMAIL >> .env
env | sort | grep MUSICFILES_BUCKET_NAME >> .env
cat .env

exit 0
