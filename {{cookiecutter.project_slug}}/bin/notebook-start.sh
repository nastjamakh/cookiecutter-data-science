#!/bin/bash
: "${PROJECT_NAME:={{cookiecutter.project_slug}}}"

docker exec -i -t  ${PROJECT_NAME} \
  poetry run dotenv run jupyter lab \
  --ip="*" \
  --port=7777 \
  --NotebookApp.token=''  \
  --NotebookApp.custom_display_url=http://localhost:7777
