from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate  # Add this import
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Event

##da main flask app
app = Flask(__name__)
#modify db role n pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ivanjaison:(putdapasswd w/outparens)@localhost/flask_event_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = "login"


# User Loadin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Failed. Check your email and password.')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You can now login.')
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/dashboard')
@login_required
def dashboard():
    events = Event.query.filter_by(organizer_id=current_user.id).all()
    return render_template('dashboard.html', events=events)


@app.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    print(f"User role: {current_user.role}")  # Debug statement
    if current_user.role != 'organizer':
        flash('You do not have permission to create events.')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        date = request.form['date']
        location = request.form['location']
        event_type = request.form['event_type']

        event = Event(name=name, description=description, date=date, location=location, event_type=event_type, organizer_id=current_user.id)
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!')
        return redirect(url_for('dashboard'))

    return render_template('create_event.html')


@app.route('/rsvp/<int:event_id>', methods=['POST'])
@login_required
def rsvp(event_id):
    event = Event.query.get(event_id)
    if event and current_user not in event.attendees:
        event.attendees.append(current_user)
        event.attendees_count += 1
        db.session.commit()
        flash('You have RSVP\'d to the event!')
    else:
        flash('You are already RSVP\'d to this event.')
    return redirect(url_for('event_details', event_id=event.id))


@app.route('/event_details/<int:event_id>')
@login_required
def event_details(event_id):
    event = Event.query.get(event_id)
    return render_template('event_details.html', event=event)


@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('You are not authorized to view this page.')
        return redirect(url_for('dashboard'))

    users = User.query.all()
    events = Event.query.all()
    return render_template('admin_dashboard.html', users=users, events=events)


if __name__ == '__main__':
    app.run(debug=True)

