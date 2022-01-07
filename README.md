# Simple Health

## Setup for development

### Requirements

- pre-commit
- Docker
- Poetry
- Node.js v16.13.0
- pytest

We recommend installing pre-commit, Poetry using pip or Homebrew to global environment.

### Prepare .envrc via direnv
1. Please install [direnv](https://github.com/direnv/direnv) before setting.
2. Edit .envrc with `direnv edit .` command.
3. Add following variables.
```bash
export MODE=dev or debug # debug is for debugging by VSCode
export NGINX_PORT=80
export DOMAIN=localhost
export API_URL=api
export ALLOW_ORIGIN=http://lvh.me:3000 # This setting is optional.
export LOCAL_DATA_DIR='/local/path/to/data/dir'
export FILE_STORAGE=S3 or Local
export AWS_ACCESS_KEY_ID='AWS ACCESS KEY'
export AWS_SECRET_ACCESS_KEY='AWS SECRET ACCESS KEY'
```
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
