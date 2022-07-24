# Learning Objectives
## Students Will Be Able To:
- Describe the use case of Django
- Contrast MVC with Django's MVT architecture
- Describe the components of a Django project
- Describe Django's routing methodology
- Install Django and psycopg2
- Build Django's official tutorial app

# What is Django?
Django is by far the most popular Python-based web framework and its popularity continues to grow thanks to the amazing growth of Python itself.

Django was publicly released in 2005 and got its name from one of its creator's, Adrian Holovaty, who named Django after his favorite guitarist Django Reinhardt.

It's designed for the rapid development of highly-secure web applications.

Compared to the minimalist web framework of Express, Django is a much higher-level framework that provids lots of functionality baked-in, including:

- A powerful Object-Relational-Mapper (ORM) for working with relational databases using Python code instead of SQL.
- A built-in admin app for browsing and manipulating data in the database.
- Built-in user management and authentication.

# Django's MVY Architecture
| Concern                   |     MVC     |    MVT   |
|---------------------------|:-----------:|---------:|
| Database access           | Model       | Model    |
| Code mapped to routes     | Controller  | View     |
| Rendering of dynamic HTML | View        | Template |

# Django is like a One Stop Shop
- The webframe work has many built in packages that are ready on startup

# GETTING STARTED
-  **ALWAYS IMPLEMENT AUTHENTICATION FIRST!**
- sudo service postgresql start
    # To start the postgresql service and connect to postgresql service
- we used psycopg2-binary to use postgreSQL instead of the built in SQLite3
- change DATABASES object in settings.py (Django configurations) to update this database change
- with psql installed createdb <dbname>
- django-admin startproject <dbname>
- python manage.py startapp main_app

# DJANGO HTML TEMPATE
- html templates are located in the main_app.templates directory
- django uses jinja and another template application to work with and render html files
- any route/path that is to return a message to the user must have it's own .html template file in the main_app.template directory unless work with special django html templates such as form.html
- any time you want to convey something to the user, the response must return rendered html
- generally, a get request will return rendered html to the user
- to confirm a post, put, or delete request with some type of visual message, must also return rendered html

# DJANG FORMS.py

# TROUBLE SHOOTING:
- ALWAYS CHECK THE SETTING FILE:
    I had to change the DATABASES object in settings.py from sqlite to postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catcollector',
    }
}