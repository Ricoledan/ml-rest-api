# ML-REST-api

🐍 A simple python-based REST API that deploys machine learning models

## Setting up your Python environment

create virtual environment
`python3 -m venv env`

activate environment
`source env/bin/activate`

deactivate environment
`deactivate`

## Dependencies

install dependencies
`python3 -m pip install -r requirements.txt`

lock dependencies
`pip freeze > requirements.txt`

## Run application (Local)

run application with active reload
`uvicorn --app-dir=./app main:app --reload`
