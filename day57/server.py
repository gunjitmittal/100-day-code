from flask import Flask, render_template
import datetime
import requests
app = Flask(__name__)
now = datetime.datetime.now()
year = now.year
gend_api_url = "https://api.genderize.io?name="
age_api_url = "https://api.agify.io?name="


@app.route('/')
def hello():
    return render_template('index.html', year=year)


@app.route('/guess/<name>')
def guess(name):
    gend_resp = requests.get(gend_api_url+name)
    gend_resp.raise_for_status()
    gend_data = gend_resp.json()
    gender = gend_data['gender']

    age_resp = requests.get(age_api_url + name)
    age_resp.raise_for_status()
    age_data = age_resp.json()
    age = age_data['age']
    title_name = name.title()
    return render_template('guess.html', name=title_name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
