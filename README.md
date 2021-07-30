## About

[![Build Status](https://travis-ci.org/josemash4@gmail.com/closest_points.svg?branch=master)](https://travis-ci.org/josemash4@gmail.com/closest_points)

The application exposes APIs that accepts a string of comma separated points and computes the closest points. It then stores them in a table.

## Local Development

- create a virtualenvironment
- install dependencies

     ```python
     pip install -r requirements.txt
     ```
- run server
   ```python 
     python manage.py runserver
   ```

## How To Use
#### Register user

```curl
curl -d '{"username":"'"test"'", "password":"test", "email":"test123@test.com", "first_name":"test", "last_name":"user"}' \
     -H "Content-Type: application/json" \
     -X POST https://closests-points-api.herokuapp.com/api/v1/user-create/
```

```curl
response:
{"id":"920cad0f-2b55-4e84-8f85-0c743d75d560","username":"test","first_name":"test","last_name":"user","email":"test123@test.com","auth_token":"bb5441ca249495d2f94ea4db65fe3c7c1c6cec3c"}
```

#### Get authentication token

```curl
curl -d '{"username":"'"test"'", "password":"test"}' \
     -H "Content-Type: application/json" \
     -X POST https://closests-points-api.herokuapp.com/api-token-auth/
```

```curl
response: 2aa895cb01f47c56bbb61f34c0ffabd54472116e
```
#### Get users

```curl
curl localhost:8000/api/v1/users/ -H 'Authorization: Token 3e213ec878a0cd0856b74ef83c850ca96db52fcc'
```

#### Submit points

```curl
curl --location --request POST 'https://closests-points-api.herokuapp.com/api/v1/points/compute_closest_points/' \
--header 'Authorization: Token 2aa895cb01f47c56bbb61f34c0ffabd54472116e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "submission": "(4,5), (5,5), (1, 2)"
}'
```

``` curl
response: [[4,5],[5,5]]
```
## Prod API URL

https://closests-points-api.herokuapp.com/api/v1/