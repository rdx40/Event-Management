# Event-Management
A simple CRUD application using pythons Flask framework and postgreSQL

gotta add the static files and make small updates

A Flask-based event management application that allows users to create events, RSVP, and view event details. Admins have access to a dashboard where they can manage users and events.


Features available --> Authenticating User (login & sign up & password storage with hashing)
                       Event Creation and managing attendee list
                       RSVP for events
                       Dashboard for admins and non admin users
                       Roles for users and organizers


## Steps to try it out

1. Clone the repo
2. Set up a virtual environment
3. Run/Create a postgres db. create a db named flask_event_system. modify the database URI in app.py and in migrations/alembic.ini.
4. run the following commands
    "flask db init
flask db migrate
flask db upgrade"

5. then just run the python app
6. in order to try out the admin features you'll have to modify the role column for your user to admin in psql or pgadmin.
