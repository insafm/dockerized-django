[image]: https://github.com/insafm/dockerized-django/SCREENSHOT.png

### Terminology
----

- Docker: A containerization technology that provides a simple, reliable, and secure way to run software.
- Dockerfile: A set of commands to build an image to be run as a container.
- Docker-Compose: A file defining how to run a multi-container Docker application.
- Docker-Machine: A tool for managing Docker containers.
- Docker-Registry: A Docker registry that stores images and allows you to share them with others.

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