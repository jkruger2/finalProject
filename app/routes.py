from flask import render_template
from app import app


@app.route('/')
def home():
    welcomeMessage = "Welcome to Call of Duty stat tracker!"


    return render_template('greeting.html', message=welcomeMessage)

@app.route('/leaderboards')
def leaderboards():

    return render_template('leaderboards.html', title="This is the leaderboards page")

@app.route('/login')
def login():

    return render_template('login.html', title="This is the login page")

@app.route('/register')
def register():

    return render_template('register.html', title="This is the register page")