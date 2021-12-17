import jinja2.exceptions
import sqlalchemy.exc
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, StatSearchForm
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
import http.client
import json


@app.route('/leaderboards', methods=['GET'])
@login_required
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
@login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    try:
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Congratulations, you are now a registered user!')
            return redirect(url_for('login'))

    except sqlalchemy.exc.IntegrityError:
        flash("Already Registered user!")
        redirect(url_for('register'))

        return render_template('register.html', username=username, email=email)

    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
