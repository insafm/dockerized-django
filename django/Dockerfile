# Official python runtime based on Debian - https://hub.docker.com/_/python
FROM python:3.10.5-slim-buster

# Expose the Django application to serve HTTP requests.
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt /app/

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install the system packages required by the Django and PostgreSQL.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    gcc libpq-dev python3-dev \
&& rm -rf /var/lib/apt/lists/*

# Install the requirements
RUN pip install -r requirements.txt

# Copy the Django application to the container
COPY . /app/

# Copy entrypoint.sh to the container and execute it.
COPY ./entrypoint_dev.sh /
ENTRYPOINT ["sh", "/entrypoint_dev.sh"]