# Blog App

Using Django-x, docker, gunicorn and postgres

## API

You can interact with the API using JSON Web Tokens or valid a username/password.

HTTP method | Url | Description
----------- | --- | -----------
POST | /api/token | generate a token when supplied with a valid  username/password
GET | /api/v1/create | returns a list of all the posts in the blog
POST | /api/v1/create | allows you to create a new post
GET | /api/v1/update/\<id\> | get the details of a specific post
PUT | /api/v1/update/\<id\> | adjust the details of a specific post
DELETE | /api/v1/delete/\<id\> | delete a specific post
