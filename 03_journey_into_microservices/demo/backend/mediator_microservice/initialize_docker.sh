#!/usr/bin/env bash

# build initialize docker
docker build . -t masterclass_mediator_microservice_image:1.0

# create virtual environment
docker run -it -v $PWD:/home/masterclass/backend/mediator_microservice -t masterclass_mediator_microservice_image:1.0 su - masterclass /bin/bash -c  "cd backend/mediator_microservice && virtualenv --python=python3.9 /home/masterclass/backend/mediator_microservice/mediator_microservice_env"

# install requirements
docker run -it -v $PWD:/home/masterclass/backend/mediator_microservice -t masterclass_mediator_microservice_image:1.0 su - masterclass /bin/bash -c  "cd backend/mediator_microservice && export LC_ALL='en_US.UTF-8' && pip install -r requirements.txt"
