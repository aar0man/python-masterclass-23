# cd deploy/base_dockers
# docker build . -f default_masterclass_image.Dockerfile -t masterclass-python-39-image:latest

FROM python:3.9-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# upgrading and updating apt
RUN apt-get update -y
RUN apt-get upgrade -y


RUN apt-get install -y sudo apt-transport-https
RUN apt-get install -y --no-install-recommends apt-utils

# packages for django developmet.
RUN apt-get install -y virtualenv python3-dev python-setuptools python3-pip pkg-config default-libmysqlclient-dev  \
    build-essential libpcre3-dev curl

# required for mysql dump
RUN apt-get install -y wget lsb-release
# mysql-apt-config version taken from here- https://dev.mysql.com/downloads/repo/apt/
RUN wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
RUN dpkg -i mysql-apt-config_0.8.22-1_all.deb
RUN apt-get update -y
RUN apt-get install -y mysql-client


# creating directories
RUN mkdir -p /home/masterclass/backend/

# set the encoding
RUN apt-get install -y locales
RUN sed -i 's/^# *\(en_US.UTF-8\)/\1/' /etc/locale.gen && locale-gen
