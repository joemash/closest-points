# closest-points

[![Build Status](https://travis-ci.org/josemash4@gmail.com/closest-points.svg?branch=master)](https://travis-ci.org/josemash4@gmail.com/closest-points)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

The application exposes APIs that accepts a string of comma separated points and computes the closest points. It then stores them in a table.. Check out the project's [documentation](http://josemash4@gmail.com.github.io/closest-points/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```
