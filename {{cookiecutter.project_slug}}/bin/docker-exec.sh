#!/bin/bash

: "${PROJECT_NAME:={{cookiecutter.project_slug}}}"

docker exec -i -t $PROJECT_NAME `echo "${@:1}"`

