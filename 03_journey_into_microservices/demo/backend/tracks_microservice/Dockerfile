FROM masterclass-python-39-image:latest

RUN useradd -m -s /bin/bash -G sudo masterclass && echo "masterclass:1234" | chpasswd
RUN mkdir -p /home/masterclass/backend/tracks_microservice

# all files under masterclass dir should be owned by masterclass user only
RUN chown masterclass:masterclass /home/masterclass -R

# Install required system packages
RUN apt update
RUN apt-get install -y graphviz libgraphviz-dev pkg-config

# creating the _env inside the image and setting its activation by log in to the masterclass user
RUN virtualenv --python=python3.9 /home/masterclass/backend/tracks_microservice/tracks_microservice_env
RUN echo source /home/masterclass/backend/tracks_microservice/tracks_microservice_env/bin/activate >> /home/masterclass/.profile

# Install pepstats package
RUN apt-get update --fix-missing
RUN sudo apt-get install -y emboss
