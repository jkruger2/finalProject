from flask import render_template
from app import app
from app.forms import LoginForm, RegistrationForm
import http.client
import json


@app.route('/leaderboards', methods=['GET'])
def leaderboards():
    conn = http.client.HTTPSConnection("call-of-duty-modern-warfare.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
        'x-rapidapi-key': "e8add8818emsh375582548eaa496p11cec5jsnb2f8ec06618b"
    }
    conn.request("GET", "/leaderboard/1/psn", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    d = json.loads(data)

    return render_template('leaderboards.html', title="This is the leaderboards page", d=d)


@app.route('/')
def home():
    welcomeMessage = "Welcome to Call of Duty stat tracker!"


    return render_template('greeting.html', message=welcomeMessage)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    return render_template('register.html', form=form)