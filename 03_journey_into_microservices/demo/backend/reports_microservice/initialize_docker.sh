#!/usr/bin/env bash

# build initialize docker
docker build . -t masterclass_reports_microservice_image:1.0

# create virtual environment
docker run -it -v $PWD:/home/masterclass/backend/reports_microservice -t masterclass_reports_microservice_image:1.0 su - masterclass /bin/bash -c  "cd backend/reports_microservice && virtualenv --python=python3.9 /home/masterclass/backend/reports_microservice/reports_microservice_env"

# install requirements
docker run -it -v $PWD:/home/masterclass/backend/reports_microservice -t masterclass_reports_microservice_image:1.0 su - masterclass /bin/bash -c  "cd backend/reports_microservice && export LC_ALL='en_US.UTF-8' && pip install -r requirements.txt"
