# Event-Management
A simple CRUD application using Python's Flask framework and PostgreSQL.

Got to add the static files and make small updates.

A Flask-based event management application that allows users to create events, RSVP, and view event details. Admins have access to a dashboard where they can manage users and events.

### Features available
- Authenticating User (login & sign up & password storage with hashing)
- Event Creation and managing attendee list
- RSVP for events
- Dashboard for admins and non-admin users
- Roles for users and organizers

## Steps to try it out

1. Clone the repo:

    ```bash
    git clone https://github.com/username/Event-Management.git
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv .pyvenv
    source .pyvenv/bin/activate  # On Linux or macOS
    .pyvenv\Scripts\activate     # On Windows
    ```

3. Run/Create a PostgreSQL database. Create a db named `flask_event_system`, then modify the database URI in `app.py` and in `migrations/alembic.ini`.

4. Run the following commands:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Then just run the Python app:

    ```bash
    flask run
    ```

6. In order to try out the admin features, you'll have to modify the `role` column for your user to `admin` in PostgreSQL or pgAdmin:

    ```sql
    UPDATE users SET role = 'admin' WHERE username = 'your_username';
    ```

    Or you can use pgAdmin's graphical interface to update the role.

