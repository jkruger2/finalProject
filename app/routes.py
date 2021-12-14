import jinja2.exceptions
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm, StatSearchForm
import http.client
import json


@app.route('/leaderboards', methods=['GET'])
def leaderboards():
    conn = http.client.HTTPSConnection("call-of-duty-modern-warfare.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
        'x-rapidapi-key': "096457d7f9msh93ab9be5adf5896p1ae9cejsncc1080dc547f"
    }
    conn.request("GET", "/leaderboard/1/psn", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    d = json.loads(data)

    return render_template('leaderboards.html', title="Global Leaderboard", d=d)


@app.route('/statSearch', methods=['GET', 'POST'])
def statSearch():
    try:
        form = StatSearchForm()
        form.platform.choices = ['xbl', 'psn']

        if form.validate_on_submit():
            person = form.username.data
            platform = form.platform.data

            conn = http.client.HTTPSConnection("call-of-duty-modern-warfare.p.rapidapi.com")
            headers = {
                'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
                'x-rapidapi-key': "{Your API Key Here}"
            }
            conn.request("GET", "/multiplayer/{}/{}".format(person, platform), headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            d = json.loads(data)

            return render_template('searchResult.html', d=d)

    except jinja2.exceptions.UndefinedError:
        flash('{} Does not exist on {}. Make sure you spelled the username correctly or try switching the platform'.format(form.username.data, form.platform.data))
        return redirect(url_for('statSearch'))

    return render_template('statSearch.html', form=form, title="Search for a specific users stats")


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