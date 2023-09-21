from flask import Flask, request, render_template, jsonify, session, redirect,url_for, flash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


import re
import time
import datetime

from secret_getrate import gen_new_token
from firebase_api import FireBaseInit

#from auth import valid_credentials


app = Flask(__name__)

key = gen_new_token()
app.secret_key = key

limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])


csrf = CSRFProtect(app)
csrf.init_app(app)



login_Manager = LoginManager()
login_Manager.init_app(app)
login_Manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@login_Manager.user_loader
def load_user(user_id):
    return User(user_id)


app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

config = None

firebase = FireBaseInit(config)

auth = firebase.auth()

@app.route('/')
def hello():
    return render_template("test.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/HouseFinder")
def HouseFinder():
    return render_template("HouseFinder.html")

@app.route("/Download")
def Download():
    return render_template("Download.html")


@app.route("/hfDBbrowser")
def hfDBbrowser():
    return render_template("dev.html")

# @app.route('/submit-api', methods=['POST'])
# def submit_api():
#     data = request.form
#     print(data)
#     # Process the data and perform necessary actions
#     response = {'message': 'Data submitted successfully'}
#     return jsonify(response)

@app.route('/dev')
def dev():
    return render_template("dev.html")

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

# @app.route('/search', methods=['POST', 'GET'])
# def search():
#     if request.method == 'POST':
#         search_query = request.form.get('search_query', '')
#         return render_template('search_results.html')

#     return render_template('search_form.html')

@app.route('/housefinder/api/lookup', methods=['POST', 'GET'])
@limiter.limit("2/minute")
def lookup():
    if request.method == 'POST':
        search_query = request.form.get('search_query', '')
        return render_template('search_results.html')
    return "Please use API client"

@app.route("/page")
def apge():
    return render_template("page.html")

@app.route("/price")
def price():
    return render_template("price.html")


    
@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("10/minute")
def login():
    if 'user_id' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user_info = auth.sign_in_with_email_and_password(email, password)
            print(user_info)
            user_id = user_info['localId']
            user = User(user_id)
            login_user(user)  # Use Flask-Login's login_user function
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        except Exception as e:
            flash(f'Login failed. {str(e)}', 'danger')

    return render_template('auth.html')

@app.route('/profile')
@login_required
def profile():
    return f'Welcome to your profile, {current_user.id}!'

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Use Flask-Login's logout_user function
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@app.route("/register")
def reg():
    return render_template("reg.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run()
