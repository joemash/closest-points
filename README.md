# closest_points

[![Build Status](https://travis-ci.org/josemash4@gmail.com/closest_points.svg?branch=master)](https://travis-ci.org/josemash4@gmail.com/closest_points)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

The application exposes APIs that accepts a string of comma separated points and computes the closest points. It then stores them in a table.. Check out the project's [documentation](http://josemash4@gmail.com.github.io/closest_points/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web
```

### Register user

curl -d '{"username":"'"test"'", "password":"test", "email":"test123@test.com", "first_name":"test", "last_name":"user"}' \
     -H "Content-Type: application/json" \
     -X POST localhost:8000/api/v1/user-create/

### Get token from api


curl -d '{"username":"'"test"'", "password":"test"}' \
     -H "Content-Type: application/json" \
     -X POST localhost:8000/api-token-auth/

### Use token to make requests

curl localhost:8000/api/v1/users/ -H 'Authorization: Token 3e213ec878a0cd0856b74ef83c850ca96db52fcc'