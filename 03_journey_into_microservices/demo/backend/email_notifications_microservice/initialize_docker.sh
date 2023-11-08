#!/usr/bin/env bash

# build initialize docker
docker build . -t masterclass_email_notifications_microservice_1:1.0

# create virtual environment
docker run -it -v $PWD:/home/masterclass/backend/email_notifications_microservice -t masterclass_email_notifications_microservice_image:1.0 su - masterclass /bin/bash -c  "cd backend/email_notifications_microservice && virtualenv --python=python3.9 /home/masterclass/backend/email_notifications_microservice/email_notifications_microservice_env"

# install requirements
docker run -it -v $PWD:/home/masterclass/backend/email_notifications_microservice -t masterclass_email_notifications_microservice_image:1.0 su - masterclass /bin/bash -c  "cd backend/email_notifications_microservice && export LC_ALL='en_US.UTF-8' && pip install -r requirements.txt"
