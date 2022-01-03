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

    Define interfaces for the data that they need in order to apply some logic. One or more data providers will implement the interface, but the use case doesn’t know where the data is coming from

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
    docker-compose run --rm --entrypoint "poetry install" underground-back

## Development

### Directory structure

    api
    |-- __init__.py
    |-- main.py
    |-- crud     # DB operations
    |-- models   # Class definition for domain models
    |-- routers  # Path definition
    `-- schemas  # Class definition for HTTP request / response.

### add new dependencies

    docker-compose run --rm --entrypoint "poetry add <new package>" underground-back

### run API

    docker-compose up

If it works well, you can access http://localhost:8000/docs

### Initialize development DB

    python ./init_dev_db.py
