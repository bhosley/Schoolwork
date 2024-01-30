#FROM {{BASEDOCKER}}
FROM tensorflow/tensorflow:2.12.0-gpu-jupyter
# KNOWN FUNCTIONAL -  tensorflow/tensorflow:2.12.0-gpu-jupyter

# Current Known Functional
#? But is it necessary here?
ENV DEBIAN_FRONTEND=noninteractive

# Base Utilities
RUN apt update -yq \
    && apt install -yq \
        #curl \
        wget \ 
        unzip \
        vim \
        cmake \
        sudo \
    && useradd -m docker && echo "docker:docker" | chpasswd \
    # Adding a user, not sure that this is necessary
    && adduser docker sudo \
    # as above..
    && pip3 install pysc2

# SC2 Environment Setup
# List of most recent files can be found at:
# https://github.com/Blizzard/s2client-proto
# and unzipped using Blizzard's Directory Password
ARG PASSWORD=iagreetotheeula
# DL and Unzip Client
RUN wget https://blzdistsc2-a.akamaihd.net/Linux/SC2.4.10.zip && \
    unzip -P ${PASSWORD} SC2.3.16.1.zip -d ~/ && \
    # and map packs
    wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season1.zip && \
    unzip -P ${PASSWORD} Ladder2017Season1.zip -d ~/StarCraftII/Maps && \
    # delete compressed files
    rm *.zip && \
    # use the API's script for pulling replay packs
    echo "wget http://blzdistsc2-a.akamaihd.net/ReplayPacks/3.16.1-Pack_1-fix.zip && unzip -P iagreetotheeula 3.16.1-Pack_1-fix.zip -d ~/StarCraftII/Replays" > download_replays.sh


# Entry point into the container
#ENTRYPOINT ["/bin/bash"]


# Use Tini to init container
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "-g", "--"]



# Is this a needed ACE command?
EXPOSE 6006






#wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season2.zip && \
#wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season3.zip && \
#wget http://blzdistsc2-a.akamaihd.net/MapPacks/Melee.zip && \
#unzip -P ${PASSWORD} Ladder2017Season2.zip -d ~/StarCraftII/Maps && \
#unzip -P ${PASSWORD} Ladder2017Season3.zip -d ~/StarCraftII/Maps && \
#unzip -P ${PASSWORD} Melee.zip -d ~/StarCraftII/Maps && \

## OPENCV Build Section
##RUN mkdir /opencv && \
##curl -fsSL http://bit.ly/OpenCV-Latest | bash -s /opencv-build && \
##rm -rf /opencv-build
##ENV PYTHONPATH=$PYTHONPATH:$HOME/.opencv/lib/python3.2/dist-package
#
#
#
#

# Set up StarCraft II Test Environment for Dentosal python-sc2 bots (not pysc2 bots!)

# Use an official debian stretch slim release as a base image
##FROM python:3.7-slim


##USER root

# From https://github.com/yeungegs/egsy-dockerfiles/tree/master/botbierv2
# Update and install packages for SC2 development environment
# git, unzip and wget for download and extraction
# tree for debugging
##RUN apt-get update && apt-get install --assume-yes --no-install-recommends --no-show-upgraded \
##    libglib2.0-0 \
##    libsm6 \
##    libxext6 \
##    libxrender-dev \
##    git \
##    make \
##    gcc \
##    tree \
##    unzip \
##    wget \
##    gpg \
##    python-dev \
##    procps \
##    lsof \
##    apt-transport-https \
##    # Clean up
##    && rm -rf /var/lib/apt/lists/*

# Add the microsoft repo for dotnetcore
##RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg && \
##    mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/ && \
##    wget -q https://packages.microsoft.com/config/debian/9/prod.list && \
##    mv prod.list /etc/apt/sources.list.d/microsoft-prod.list && \
##    chown root:root /etc/apt/trusted.gpg.d/microsoft.asc.gpg && \
##    chown root:root /etc/apt/sources.list.d/microsoft-prod.list

# Needed for Java install
##RUN mkdir -p /usr/share/man/man1

# Needed to use the 32bit version of wine
##RUN dpkg --add-architecture i386

# Install software via APT
##RUN apt-get update && apt-get install --assume-yes --no-install-recommends --no-show-upgraded \
##    openjdk-11-jdk \
##    wine32 \
##    dotnet-sdk-2.2 \
##    # Clean up
##    && rm -rf /var/lib/apt/lists/*
##
##WORKDIR /root/
##ENV PATH $PATH

# Download and uncompress StarCraftII from https://github.com/Blizzard/s2client-proto#linux-packages and remove zip file
# If file is locally available, use this instead:
#ADD SC2.4.10.zip /root/
#RUN unzip -P iagreetotheeula SC2.4.10.zip \
#    && rm *.zip
##RUN wget -q 'http://blzdistsc2-a.akamaihd.net/Linux/SC2.4.10.zip' \
##    && unzip -P iagreetotheeula SC2.4.10.zip \
##    && rm *.zip

# Create a symlink for the maps directory
##RUN ln -s /root/StarCraftII/Maps /root/StarCraftII/maps

# Remove the Maps that come with the SC2 client
##RUN rm -Rf /root/StarCraftII/maps/*

# Change to maps folder
##WORKDIR /root/StarCraftII/maps/

# Maps are available here https://github.com/Blizzard/s2client-proto#map-packs and here http://wiki.sc2ai.net/Ladder_Maps
# Download and uncompress StarCraftII Maps, remove zip file - using "maps" instead of "Maps" as target folder
##RUN wget https://sc2ai.net/Maps/Season1Maps.zip
##RUN wget https://sc2ai.net/Maps/Season2Maps.zip
##RUN wget https://sc2ai.net/Maps/Season3Maps.zip
##RUN wget https://sc2ai.net/Maps/Season4Maps.zip
##RUN wget https://sc2ai.net/Maps/Season5Maps.zip
##RUN wget https://sc2ai.net/Maps/Season6Maps.zip
##RUN wget https://sc2ai.net/Maps/Season7Maps.zip
##RUN wget https://sc2ai.net/Maps/Season8Maps.zip
##RUN wget https://sc2ai.net/Maps/Season9Maps.zip
##RUN wget https://sc2ai.net/Maps/Season10Maps.zip
##RUN wget https://sc2ai.net/Maps/Season11Maps.zip
##RUN wget http://wiki.sc2ai.net/images/9/95/S8Wk1Maps.zip
##RUN wget http://wiki.sc2ai.net/images/a/af/Wk2maps.zip
##RUN unzip -o '*.zip'
##
##RUN wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2019Season3.zip
##RUN unzip -P iagreetotheeula -o 'Ladder2019Season3.zip'
##RUN mv Ladder2019Season3/* .
##RUN rmdir Ladder2019Season3
##
##RUN wget http://blzdistsc2-a.akamaihd.net/MapPacks/Melee.zip
##RUN unzip -P iagreetotheeula -o 'Melee.zip'
##RUN mv Melee/* .
##RUN rmdir Melee
##
##RUN rm *.zip
##RUN tree
##
##WORKDIR /root/

# Add Pythonpath to env to user aiarena
##ENV PYTHONPATH=/root/aiarena-client/:/root/aiarena-client/arenaclient/:/root/.local/bin
##ENV HOST 0.0.0.0

# Create Bot and Replay directories (arenaclient specific)
##RUN mkdir -p /root/StarCraftII/Bots
##RUN mkdir -p /root/StarCraftII/Replays

# Download the aiarena client
##RUN git clone https://github.com/BurnySc2/aiarena-client /root/aiarena-client

# Change to working directory
##WORKDIR /root/aiarena-client

# Install poetry and arenaclient requirements
##RUN pip install poetry
##RUN poetry install
# Or if you want to run without poetry (virtual environment):
#RUN poetry export -f requirements.txt --output requirements.txt
#RUN pip install -r requirements.txt

# List contents of working directory
##RUN tree

# Install the arena client as a module
#RUN python /root/aiarena-client/setup.py install

# Setup the config file
##RUN echo '{"bot_directory_location": "/root/StarCraftII/Bots", "sc2_directory_location": "/root/StarCraftII/", "replay_directory_location": "/root/StarCraftII/Replays", "API_token": "", "max_game_time": "60486", "allow_debug": "Off", "visualize": "Off"}' > /root/aiarena-client/arenaclient/proxy/settings.json

##WORKDIR /root/aiarena-client/arenaclient

# Start the proxy server
##ENTRYPOINT [ "poetry", "run", "python", "proxy/server.py", "-f" ]
#ENTRYPOINT [ "python", "proxy/server.py", "-f" ]

# Alternatively start the server via interactive mode (while using 'sh' or 'bash' as entrypoint):
# docker exec -i app python /root/aiarena-client/arenaclient/proxy/server.py -f &
#ENTRYPOINT [ "sh" ]