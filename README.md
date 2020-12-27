# Blog App

Using Django-x, docker, gunicorn and postgres

## API

You can interact with the API using JSON Web Tokens or valid a username/password.

To generate a JWT with my admin account credentials using httpie:

```bash
http :8000/api/token/ username=mark password=mark
```

Or with the server runnng you can just go to your own localhost:8000 and create your own account through the web browser, and use the same httpie syntax afterwards with that new account's credentials.

HTTP method | Url | Description
----------- | --- | -----------
POST | /api/token | generate a token when supplied with a valid  username/password
GET | /api/v1/create | returns a list of all the posts in the blog
POST | /api/v1/create | allows you to create a new post
GET | /api/v1/update/\<id\> | get the details of a specific post
PUT | /api/v1/update/\<id\> | adjust the details of a specific post
DELETE | /api/v1/delete/\<id\> | delete a specific post
