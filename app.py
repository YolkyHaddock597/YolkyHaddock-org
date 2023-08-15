from flask import Flask, request, render_template, jsonify
import re


app = Flask(__name__)

def validate_parcel_id(parcel_id):
    # Use a regular expression to validate the format
    pattern = r'^\d{3}-[A-Z]-\d{5}-\d{4}-\d{2}$'
    return re.match(pattern, parcel_id)


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

        # Perform proper validation and filtering based on input type
        if validate_parcel_id(search_query):
            # Handle parcel ID search
            # Your code here
            result = "Parcel ID search result"
        else:
            # Handle address or name search
            # Your code here
            result = "Address or Name search result"

        return render_template('search_results.html', result=result)

    return render_template('search_form.html')


if __name__ == "__main__":
    app.run()