## Synopsis

A Django webapp managing companies for users and providing a REST API. 
Basically it allows a user to CRUD his own companies, the user and only
him will have R/W access to the companies he owns.

## Installation

### 1) Create a python virtualenv for this project

`python3 -m virtualenv -p /usr/bin/python3.5 companies_site_env`

you can give it the name you like if you want

### 2) Activate the virtualenv

`source companies_site_env/bin/activate`

### 3) Go to the project root and install the requirements

`cd /path/to/companies_site/`
`pip install -rrequirements.txt`

This will install all the dependencies in our virtualenv

### 4) Make data migrations

Assuming that you are already in the project root
`./manage.py makemigrations`
`./manage.py migrate`

The project already contains an sqlite3 database, the existing user is
`admin:admin1234` if you want to delete the db, just remove the 
`db.sqlite3` file and all that the folder
`companies_site/companies/migrations` contains and redo a migration

Warning: if you delete the database, you will have to create a new user,
it can be done simply with
`./manage.py createsuperuser`
Or through the website signup/login page located at 
`http://0.0.0.0:8000/` once you started the django dev server

### 5) Start the dev server
`./manage.py runserver 0.0.0.0:8000`

## API Reference

### The REST API is available at the following urls:

Companies list for current user
`http://0.0.0.0:8000/api/companies/`

Users listing
`http://0.0.0.0:8000/api/users/`

A basic authentication uname/password is used for the access, an example
with curl:

`curl --user uname:password http://0.0.0.0:8000/api/users/`
This fetches the users list.

Or simply open it in your browser, the django rest_framework provides
some views to make the requests simpler.

The functions are:
`GET /api/companies/`: fetch the companies list for the current user
`POST /api/companies/`: creates a new company (you will have to send the
JSON with all the fields except the id, the creation and update date,
here's an example of the format:
`
{
    "owner": "",
    "company_name": "testandco4545",
    "email": "owner@testandco4455.ch",
    "phone_number": "223354466",
    "address_line1": "10, rue du 4545",
    "address_line2": "",
    "postal_code": "1208",
    "city": "Geneve",
    "state_province": "GE",
    "country_code": "DE"
}`
just leave the owner an empty string, the field will be automatically
filled with your user profile in the view controller.

`GET /api/companies/<company_id>`: fetch the details for one company
`PUT /api/companies/<company_id>`: updates a company
`DELETE /api/companies/<company_id>`: deletes a company

### Using the django webapp

Open your browser at the following url: `http://0.0.0.0:8000`
The login page displays, log in if you have already an account, 
otherwise sign up, the both will lead you to the welcome page where
a link to the companies management will be available.
Create, Update or Delete your companies through the interface
