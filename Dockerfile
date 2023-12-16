FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    rm -rf /var/lib/apt/lists/*.


COPY . /docbot/

WORKDIR /docbot

RUN pip3 install -r /docbot/requirements.txt