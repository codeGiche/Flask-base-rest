# Flask-base-rest
Base flask app for rest project

### structure

**/api**

this is where the views and routes are built, you can also incorporate these swagger views

**/api/api_swagger**

It is the swagger directory, it is used for the documentation of routes, responses, requests such as the parameters that are passed to an endpoint, what response is expected, what parameters must be passed on the request ...

**/api/resources**

This folder is for the creation of our resources

**/databases**

This folder will contain our sqlalchemy instance

**/exts**

the exts folder contains a file called exts.py that we will use to instantiate our extensions

**/models**

Our folder to create our models

**/modelserializers**

Our folder to create our models serializers

**/private**

This folder is used to create applications for our project and export to another, you can see an example in /private/apps/auth, the instance of the applications created in the /private/apps/auth/\__init\__.py file has to be added in /private/exts/exts.py

**/application.py**

contains the instance of our application in this case called app

**/manager.py**

This is our file to export our models to a database

**/config.py**

configuration file

**/run.py**

file to run our application in developer mode

## steps to start

* `pip install -r requirements.txt`
* `python manager.py db init`
* `python manager.py db migrate`
* `python manager.py db upgrade`

### Create new user

`/api/v1/user : [POST](body) <str:name>, <str:email>`

### Get all users

`/api/v1/user : [GET]`

### Get user id

`/api/v1/user/<int> : [GET](QUERY)`

### Get token

`/api/v1/auth : [POST](body) <str:username>, <str:password>`

### Get all users protect with token

`/api/v1/protect/user : [GET](headers) <Authorization:access_token>`
