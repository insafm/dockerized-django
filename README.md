### Directory Structure

```
├── env
│   ├── .env
│   └── .postgres_env
├── django
│   ├── project_framework
│   |   ├── __init__.py
│   |   ├── settings.py
│   |   ├── urls.py
│   |   ├── wsgi.py
│   ├── app_1
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── app_2
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── static
│   ├── entrypoint_dev.sh
│   ├── entrypoint_production.sh
│   ├── manage.py
│   └── requirements.txt
├── README.md
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── LICENSE
├── SECURITY.md
└── CODE_OF_CONDUCT.md

```

### Terminology:
- Dockerfile: A set of commands to build an image to be run as a container.
- Docker-Compose: A file defining how to run a multi-container Docker application.

### Run Docker Compose To Run The Application
----

- ``` docker-compose -f docker-compose.dev.yml up ``` - Run the development environment.
- ``` docker-compose -f docker-compose.dev.yml up --build -d ``` - Build the development environment and run it.

### Other Common Docker Commands
----

- ``` docker-compose down ``` - Stop all containers.
- ``` docker-compose -f docker-compose.dev.yml down ``` - Stop all containers in the compose file.
- ``` docker-compose down --remove-orphans ``` - Stop all containers and delete all volumes associated with them.
- ``` docker network create supernet ``` - Create network 'supernet' if it doesn't exists.

### Backup & Restore database:
----

- ``` docker exec -t PostgreSQL pg_dumpall -c -U DockerizedDjangoUser > dump/dump_latest.sql ```  - Backup
- ``` cat dump/dump_latest.sql | docker exec -i PostgreSQL psql -U DockerizedDjangoUser ``` - Restore