from flask import Flask, request, render_template, jsonify, session, redirect


#from flask_sqlalchemy import SQLAlchemy
#from flask_session import Session

import re
import time
import datetime


#from auth import valid_credentials


app = Flask(__name__)



#app.secret_key = "please enter new key"

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

#We can set secure cookies in response
#response.set_cookie('key', 'value', secure=True, httponly=True, samesite='Lax')



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

@app.route("/Download/househub_exe/")
def Download_househub_exe():
    return render_template("Download_househub_exe.html")

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

@app.route("/login", methods=['POST', 'GET'])
def login():
    # if request.method == "POST":
    #     email = request.form.get('email')
    #     password = request.form.get('password')

    #     if valid_credentials(email, password):
    #         session['email'] = email# Store user data in session
    #         return redirect("/dashboard")
    #     else:
    #         if "email" in session:
    #             return redirect("/dashboard")
    #         return render_template("auth.html")
    return render_template("auth.html")


# @app.route('/sessionLogin', methods=['POST'])
# def session_login():
#     # Get the ID token sent by the client
#     id_token = request.json['idToken']
#     # Set session expiration to 5 days.
#     expires_in = datetime.timedelta(days=5)
#     try:
#         # Create the session cookie. This will also verify the ID token in the process.
#         # The session cookie will have the same claims as the ID token.
#         session_cookie = auth.create_session_cookie(id_token, expires_in=expires_in)
#         response = flask.jsonify({'status': 'success'})
#         # Set cookie policy for session cookie.
#         expires = datetime.datetime.now() + expires_in
#         response.set_cookie(
#             'session', session_cookie, expires=expires, httponly=True, secure=True)
#         return response
#     except exceptions.FirebaseError:
#         return flask.abort(401, 'Failed to create a session cookie')


@app.route("/register")
def reg():
    return render_template("reg.html")


if __name__ == "__main__":
    app.run()