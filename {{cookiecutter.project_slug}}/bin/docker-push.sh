#!/bin/bash
: "${PROJECT_NAME:={{cookiecutter.project_slug}}}"

aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/i9f8r4q1
docker tag $PROJECT_NAME:latest public.ecr.aws/i9f8r4q1/$PROJECT_NAME:latest
docker push public.ecr.aws/i9f8r4q1/$PROJECT_NAME:latest