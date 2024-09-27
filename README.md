# AI CHAT #



### Set ENV variable ###

* Clone the repository
* Create .env file at root and add the following

| name                   | value                                                                    | 
|------------------------|--------------------------------------------------------------------------|
| DB_CONNECTION_URL      | postgresql+psycopg2://postgres:postgres@localhost:5432/asset360          | 
| DB_SCHEMA              | ai_assistant                                                             | 
| KEYCLOAK_AUTH_URL      |                                                                          | 
| OPENAI_API_KEY         |                                                                          | 
| OPEN_AI_MODEL          | gpt-3.5-turbo                                                            | 
| CHROMA_COLLECTION      | logicline_collection                                                     | 
| EUREKA_URL             | https://assets360-sales-demo-discovery.azurewebsites.net/eureka          | 

## How do I set up locally? ##

### Prerequisite ###

Following shoul be installed in machine

* Python 3.11
* Docker if required

Run following command to make sure python installed and configured

    python --version

### Run application ###
Install [PIP](https://pip.pypa.io/en/stable/installation/)

Run
    
    pip install pipenv

Run command to install dependencies

    pipenv install

Run command to load ENV variables to virtual env

    pipenv shell

## Migration ##

[Alembic](https://alembic.sqlalchemy.org/en/latest/) is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

Install alembic to create scripts

    pip install alembic

Create revision

    alembic revision -m "A migration "

Run command to execute all migration scripts

    alembic upgrade head

To revert last migration

    alembic downgrade -1

For reference: [Example](https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a)
