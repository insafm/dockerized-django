# Official python runtime based on Debian - https://hub.docker.com/_/python
FROM python:3.10.5-slim-buster

# Create the non-root user. This user will be used to run the Django
# application. Doing this before any COPY means it won't
# be repeated on rebuild, for marginal savings in space and rebuild time.
# The user can have any name and any uid; it does not need to match any
# particular host system where the image might run.
RUN useradd -M -s /bin/bash dockerizeddjangouser

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install the system packages required by the Django and PostgreSQL.
RUN apt-get update --yes --quiet && \
    apt-get install --yes --quiet --no-install-recommends gcc libpq-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy requirements.txt to the container
COPY requirements.txt /app/

# Install the requirements
RUN pip install -r requirements.txt

# Copy the Django application to the container
COPY . /app/

# Change sorce code ownership to the non-root user.
RUN chown -R dockerizeddjangouser:dockerizeddjangouser /app

# Change the user to the non-root user.
USER dockerizeddjangouser

# Copy entrypoint.sh to the container and execute it.
COPY ./entrypoint.sh /

# Expose the Django application to serve HTTP requests.
EXPOSE 8000

# Run the Django application.
ENTRYPOINT ["sh", "/entrypoint.sh"]
