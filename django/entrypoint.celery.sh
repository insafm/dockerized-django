#!/bin/sh

celery -A project_framework.settings worker --beat --scheduler django --loglevel=info
