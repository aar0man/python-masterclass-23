#!/bin/bash -v

services=`ls backend/ | grep '_microservice$'`

echo "refreshing python requirements"
for current_service in $services; do
  echo "***$current_service***"
  docker run -it -v $PWD/backend/$current_service:/home/masterclass/backend/$current_service \
           -t masterclass_"$current_service"_image:1.0 \
           su - masterclass \
           /bin/bash -c  "cd backend/$current_service && export LC_ALL='en_US.UTF-8' && \
                          pip install --upgrade pip && pip install -r requirements.txt"
done


echo "run migrations"
for current_service in $services; do
  echo "***$current_service***"

  service_name_in_docker_compose="${current_service//_/-}"
  echo "run container"
  docker-compose up -d $service_name_in_docker_compose
  container_name=masterclass_"$service_name_in_docker_compose"_1

  docker exec -it -t $container_name \
         su - masterclass /bin/bash -c \
         "cd backend/$current_service && export LC_ALL='en_US.UTF-8' && python manage.py migrate"
done
