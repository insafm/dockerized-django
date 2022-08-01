![screenshot](https://github.com/insafm/dockerized-django/blob/main/SCREENSHOT.png?raw=true)

### Why Dockerized Django?
----

0. Preconfigured with Docker.
1. Environment Variables: environ package is used to set environment variables and you can set environment variables in .env file.
2. Settings Module: Used different settings file for development and production with a base settings file.
3. Settings Variables: Moved commonly used variables to .env file.
4. Django Logging: Django logging with rotated file handler.
5. Auto Exception Logging: Auto exception logging using rotating file handler.
6. Production Ready: Production ready with nginx and gunicorn.

### Django Environment Variables
----

- ``` APPLICATION_NAME: The name of the application. Default: 'Dockerized Django' ```
- ``` DEBUG: Debug mode. If on, will display details of error pages. If your app raises an exception when DEBUG is on, will display a detailed traceback, including a lot of metadata about the environment, such as all the currently defined Django settings (from base.py). Never deploy a site into production with DEBUG turned on. Default: 'on' ```
- ``` DJANGO_SETTINGS_MODULE: The Django settings module to use. Default: 'project_framework.settings.development' ```
- ``` SECRET_KEY: The secret key to use for cryptographic operations should be set to a unique, unpredictable value. Never deploy a site into production with the default secret key. Default: '<random string>' ```
- ``` DATABASE_URL: The URL of the database to use. You can choose from a variety of database engines. Default: 'psql://DockerizedDjangoUser:DockerizedDjangoPassword@postgres:5432/DockerizedDjango' ```
- ``` ALLOWED_HOSTS: The comma seperated hostnames that Django will use to access the site. Default: '127.0.0.1,localhost,127.0.0.1:8000,localhost:8000' ```
- ``` TIME_ZONE: The timezone to use for the site. Default: 'UTC' ```
- ``` ENABLE_LOGGING: If on, will enable exception logging in rotated file handler. Default: 'on' ```
- ``` ENABLE_AUTO_LOGGING: If on, will enable auto exception logging in rotated file handler. Default: 'on' ```
- ``` LOGGING_DIR: The directory to use for exception logging. Default: 'logs' ```


### Terminology
----

- Docker: A containerization technology that provides a simple, reliable, and secure way to run software.
- Dockerfile: A set of commands to build an image to be run as a container.
- Docker-Compose: A file defining how to run a multi-container Docker application.
- Docker-Machine: A tool for managing Docker containers.
- Docker-Registry: A Docker registry that stores images and allows you to share them with others.

### Run Docker Compose To Run The Application
----

- ``` docker-compose -f docker-compose.yml up ``` - Run the project environment.
- ``` docker-compose -f docker-compose.yml up --build -d ``` - Build the project environment and run it.

### Other Common Docker Commands
----

- ``` docker-compose down ``` - Stop all containers.
- ``` docker-compose -f docker-compose.yml down ``` - Stop all containers in the compose file.
- ``` docker-compose down --remove-orphans ``` - Stop all containers and delete all volumes associated with them.
- ``` docker network create supernet ``` - Create network 'supernet' if it doesn't exists.
- ``` docker system prune -af ``` - Remove all stopped containers, networks, volumes, and images.

### Backup & Restore Database
----

- ``` docker exec -t PostgreSQL pg_dumpall -c -U DockerizedDjangoUser > dump/dump_latest.sql ```  - Backup
- ``` cat dump/dump_latest.sql | docker exec -i PostgreSQL psql -U DockerizedDjangoUser ``` - Restore

### Upcoming Features
----
0. SMTP Configuration: SMTP configuration for sending emails.
1. Exception Logging: Exception logging using sentry.
2. Django Debug Toolbar: Django debug toolbar integration.
3. Shell: Docker commands with interactive shell.

### Blog Post
----
You can find the blog post [here](https://insafweb.in/blog/category/django/how-to-install-django-with-docker-dockerized-django/).