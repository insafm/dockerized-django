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
7. Django Debug Toolbar: Django debug toolbar configured.

### Django Environment Variables
----

- ``` APPLICATION_NAME```: The name of the application.
- ``` DEBUG```: Debug mode. If on, will display details of error pages. If your app raises an exception when DEBUG is on, will display a detailed traceback, including a lot of metadata about the environment, such as all the currently defined Django settings (from base.py). Never deploy a site into production with DEBUG turned on.
- ``` DJANGO_SETTINGS_MODULE```: The Django settings module to use.
- ``` SECRET_KEY```: The secret key to use for cryptographic operations should be set to a unique, unpredictable value. Never deploy a site into production with the default secret key.
- ``` DATABASE_URL```: The URL of the database to use. You can choose from a variety of database engines.
- ``` ALLOWED_HOSTS```: The comma seperated hostnames that Django will use to access the site.
- ``` TIME_ZONE```: The timezone to use for the site.
- ``` ENABLE_LOGGING```: If on, will enable exception logging in rotated file handler.
- ``` ENABLE_AUTO_LOGGING```: If on, will enable auto exception logging in rotated file handler.
- ``` LOGGING_DIR```: The directory to use for exception logging.
- ``` ENABLE_DEBUG_TOOLBAR```: If on, will enable debug toolbar.

### Terminology
----

- Docker: A containerization technology that provides a simple, reliable, and secure way to run software.
- Dockerfile: A set of commands to build an image to be run as a container.
- Docker-Compose: A file defining how to run a multi-container Docker application.
- Docker-Machine: A tool for managing Docker containers.
- Docker-Registry: A Docker registry that stores images and allows you to share them with others.

### Run Docker Compose To Run The Application
----

- ``` docker-compose --project-name=DockerizedDjango -f docker-compose.yml up ``` - Run the project environment.
- ``` docker-compose --project-name=DockerizedDjango -f docker-compose.yml up --build -d ``` - Build the project environment and run it.
- ``` docker-compose --project-name=DockerizedDjango -f docker-compose.yml -f docker-compose.production.yml up``` - Run the production environment.
- ``` docker-compose --project-name=DockerizedDjango -f docker-compose.yml -f docker-compose.production.yml up --build -d ``` - Build the production environment and run it.

### Other Common Docker Commands
----

- ``` docker-compose --project-name=DockerizedDjango down ``` - Stop all containers.
- ``` docker-compose --project-name=DockerizedDjango -f docker-compose.yml down ``` - Stop all containers in the compose file.
- ``` docker-compose --project-name=DockerizedDjango down --remove-orphans ``` - Stop all containers and delete orphaned containers associated with them.
- ``` docker network create supernet ``` - Create network 'supernet' if it doesn't exists.
- ``` docker system prune -af ``` - Remove all stopped containers, networks, volumes, and images.
- ``` sudo docker network create supernet ``` - Create the network manually.
- ``` sudo docker-compose --project-name=DockerizedDjango -f docker-compose.yml up --build -d ``` - Run the project environment.
- ``` sudo docker logs -f --tail 100 dockerized_django_1 ``` - Display django consol logs.
- ``` sudo docker exec -it dockerized_django_1 sh ``` - Access django shell.

### Backup & Restore Database
----

- ``` docker exec -t PostgreSQL pg_dumpall -c -U DockerizedDjangoUser > dump/dump_latest.sql ```  - Backup
- ``` cat dump/dump_latest.sql | docker exec -i PostgreSQL psql -U DockerizedDjangoUser ``` - Restore

### Upcoming Features
----
0. SMTP Configuration: SMTP configuration for sending emails.
1. Exception Logging: Exception logging using sentry.
2. Shell: Docker commands with interactive shell.
3. Celery: Celery integration.

### Blog Post
----
You can find the blog post [here](https://insafweb.in/blog/category/django/how-to-install-django-with-docker-dockerized-django/).
