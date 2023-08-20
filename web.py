from flask import Flask, request, render_template, jsonify
import re


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("test.html")

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
    return render_template("hfDBbrowser.html")

@app.route('/submit-api', methods=['POST'])
def submit_api():
    data = request.form
    print(data)
    # Process the data and perform necessary actions
    response = {'message': 'Data submitted successfully'}
    return jsonify(response)


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search_query', '')
        return render_template('search_results.html')

    return render_template('search_form.html')


if __name__ == "__main__":
    app.run()