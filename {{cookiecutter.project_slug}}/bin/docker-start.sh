#!/bin/bash
: "${PROJECT_NAME:={{cookiecutter.project_slug}}}"

if  docker ps | grep " $PROJECT_NAME$"; then
    echo "Container already started. Do nothing"
elif docker ps -a |grep " $PROJECT_NAME$" ; then
    docker start $PROJECT_NAME
else
  docker run -i -d \
            --platform linux/amd64 \
            -v $HOME/.ssh:/home/jumbo/.ssh \
            -v `pwd`:/app/$PROJECT_NAME \
            -v $HOME/.aws/credentials:/home/jumbo/.aws/credentials:ro \
            --add-host=host.docker.internal:host-gateway \
            -p 8012:8012 \
            -p 7777:7777 \
            --name $PROJECT_NAME \
            -t $PROJECT_NAME:latest \
            /bin/bash
  docker exec -i -t $PROJECT_NAME poetry install
fi
