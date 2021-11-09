from flask import render_template
from app import app
from app.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    welcomeMessage = "Welcome to Call of Duty stat tracker!"


    return render_template('greeting.html', message=welcomeMessage)

@app.route('/leaderboards')
def leaderboards():

    return render_template('leaderboards.html', title="This is the leaderboards page")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    return render_template('register.html', form=form)