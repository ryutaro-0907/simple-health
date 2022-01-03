# Simple health

## Development with docker-compose
You must specify environment variables.
```shell
export HRM_DB_PASS="pass"
docker-compose up
```
Then, you should follow [Setup database](#Database)
You may need to set `HRM_CLOCKIFY_APIKEY` written in [wiki](https://gitlab.com/hacarus/internal/management/human-resource-management/-/wikis/DB%E3%80%81Clockify%E3%81%AE%E8%A8%AD%E5%AE%9A%E6%83%85%E5%A0%B1)

## Frontend


### Setup

- Install node and npm. See [Docs](https://nodejs.org/en/download/)

- Install dependencies

```shell script
cd frontend
npm install
```

- Run development setup

```shell script
# develop
npm run dev
```

You should be able to see this in the command line

```
 DONE  Compiled successfully in 16217ms                                                                             1:24:25 PM

  App running at:
  - Local:   http://localhost:9527/
  - Network: http://192.168.1.3:9527/

  Note that the development build is not optimized.
  To create a production build, run npm run build.
```

### Build with Docker
To push the image to the ECR, login first.
```bash
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com
```
Then,
```bash
docker build -t 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_frontend:$version .
docker push 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_frontend:$version
docker tag 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_frontend:$version hrm_frontend
docker run -d -it -p 8080:8080 -v path_to_log:/var/log/nginx --name hrm_frontend hrm_frontend
```
If the repository of ECR has not been created yet, refer to the following to create it.
- https://docs.aws.amazon.com/ja_jp/AmazonECR/latest/userguide/getting-started-cli.html

## Backend

### Setup using poetry

- Install poetry. Refer to [Documenation](https://python-poetry.org/docs/#installation)

- Initialize and install dependency

```shell script
cd backend
poetry config virtualenvs.in-project true
poetry install
```

- Run backend

```shell script
poetry run python run.py
```
### Build with Docker
To push the image to the ECR, login first.
```bash
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com
```
Then,
```bash
docker build --build-arg HRM_DB_PASS=$password --build-arg HRM_DB_HOST=$host --build-arg HRM_DB_PORT=20601 --build-arg HRM_CLOCKIFY_APIKEY=$key -t 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_backend$version .
docker push 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_backend:$version
docker tag 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_backend:$version hrm_backend
docker run -d -it --name hrm_backend -p 8000:8000 hrm_backend
```
If the repository of ECR has not been created yet, refer to the following to create it.
- https://docs.aws.amazon.com/ja_jp/AmazonECR/latest/userguide/getting-started-cli.html
### Backend structure
```
backend
    ├── Dockerfile         <- Dockerfile for app.
    ├── resource_management
    │   ├── routes         <- Contains all route mapping files.
    │   ├── commons        <- Common library folder.
    │   ├── models         <- Mysql schema and seed files.
    │   ├── config.py      <- If you want to set config, do it here.
    │   └── main.py        <- Application entry point
    │
    └── pyproject.toml     <- A configuration file to store build system requirements for Python projects.
```
### Testing

You can run all test cases just like this

```shell script
# For backend
cd backend
poetry run coverage run -m pytest
```

Or run specific test case as follows

```shell script
# For backend
cd backend
poetry run coverage run -m pytest tests/test_api.py
```

## Database

You can use
- MySQL
- MariaDB

After installing your preferred database, run the following command.

```shell script
cd backend
poetry run python -m resource_management.commons.download_clockify_data --start 2020-04-01 --end 2021-04-01 --mode 0
```
Refer to the following about `mode`.
```
mode = 0 -> update all tables.
mode = 1 -> recreate all tabels
mode = 2 -> drop all tables
mode = 3 -> update only `TimeEntry` and `PlannedTimeEntry` table
mode = 4 -> create only `ProjectGroups` table
```

Also, examples of `$start` and `$end` are as follows.
```
$start = 2020-04-01
$end = 2021-04-01
```

To configure your mysql connection, edit the file `backend/resource_managment/models/settings.py`

Alternatively, you can edit/add environment variable if you don't want to edit the config file.

To test if mysql is working correctly, run the backend and access this in the browser: `http://0.0.0.0:8000/users`

## API docs

[OpenAPI](/backend/openapi.json)
