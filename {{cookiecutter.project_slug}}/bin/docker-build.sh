#!/bin/bash
: "${PROJECT_NAME:={{cookiecutter.project_slug}}}"

docker build --no-cache --platform linux/amd64 -t $PROJECT_NAME .
