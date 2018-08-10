FROM python:2.7
MAINTAINER Gatlin Johnson <gatlin@niltag.net>

# create a flask user to run the application
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

# create the working directory
RUN mkdir -p /api
WORKDIR /api

# copy over the requirements file first
COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Now copy our source code
COPY . /api

RUN chown -R flask:flaskgroup /api

USER flask
