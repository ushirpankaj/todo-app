create the virtual environment : 
1. pip install virtualenv
2. virtualenv venv

$env:FLASK_ENV = "development"
preventing __pycache__  :  $env:PYTHONDONTWRITEBYTECODE = "1"

file changes and auto detect : flask run --debug 

install all packages in requirement.txt : pip install -r requirements.txt

migration : flask db upgrade
reverse migration : flask db downgrade
create or make new migration : flask db migrate -m "message"
