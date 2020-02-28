from flask import Flask, render_template
import requests

url = 'https://corporate.airfrance.com/fr/segment/by-journey/'

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# sanity check route
@app.route('/')
@app.route('/<depart>/<arrivee>')
def home(depart=None, arrivee=None):
    cities = sorted(airport_codes, key=airport_codes.get)
    return render_template('homepage.html', depart=cities, arrivee=cities)


if __name__ == '__main__':
    airport_codes = {}
    with open('ref_codes.csv') as cities:
        for row in cities:
            name = row.split(';')
            airport_codes[name[0].decode('utf-8')] = name[1]

    app.run()