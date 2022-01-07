# Simple Health

## Architecture
### clean architecture
#### Entities
    Domain object
    Plain object

#### Use Cases
    What the applicatoin can do.
    Plain code (maybe some utils libraries.)

#### Interfaces
    Retrieve and store data from and to a number of sources (database, network devices, file system, 3rd parties, and so on.)

    Implement the interfaces defined by the use case

    the controller for a MVC

#### External interfaces
    Isolated
    Use any package here

## Setup

### Requirements

- Docker
- Poetry

We recommend installing Poetry using pip or Homebrew to global environment.

### Setup venv

    docker-compose build
    docker-compose run --rm --entrypoint "poetry install" simple-health-back

## Development

### Directory structure

    api
    |-- __init__.py
    |-- main.py
    |-- entities
    |-- usecases
    |-- interfaces
    `-- external_interfaces

### add new dependencies

    docker-compose run --rm --entrypoint "poetry add <new package>" simplehealth-back

### run API

    docker-compose up

If it works well, you can access http://localhost:8000/docs

### Pytest
    poetry run coverage run -m pytest

### test with curl
for users endpoint.
    curl localhost:8000/api/users

    curl -X POST -H "Content-Type: application/json" -d '{"username":"test", "email":"test@gmail.com","password":"test"}' http://localhost:8000/api/users/signup

    curl -X POST -H "Content-Type: application/json" -d '{"email":"test@gmail.com","password":"test"}' http://localhost:8000/api/users/signin

for records endpoint
    curl localhost:8000/api/records/1

    curl -X POST -H "Content-Type: application/json" -d '
                {
                "user_id": 0,
                "created_at": "string",
                "happiness": 0,
                "motivation": 0,
                "workout": "string",
                "helped": "string",
                "carories": 0,
                "steps": 0,
                "meditation": 0,
                "study": 0,
                "work": 0
                }' http://localhost:8000/api/records

