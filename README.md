# Simple Health

## Setup for development

### Requirements

- pre-commit
- Docker
- Poetry
- Node.js v16.13.0
- pytest

We recommend installing pre-commit, Poetry using pip or Homebrew to global environment.

### create pre-commit hook script
```bash
$ cd backend
$ pre-commit install
```

### Setup venv
```bash
$ docker-compose build
$ docker-compose run --rm --entrypoint "poetry install" simple-health-back
$ docker-compose run --rm --entrypoint "npm install" simple-health-front
```

### run for development
```bash
$ docker-compose up
```

- Backend: If it works well, you can access http://localhost:8000/docs
- Frontend: Serve with hot reload at localhost:3000

### Backend tests
```bash
$ pytest
```
