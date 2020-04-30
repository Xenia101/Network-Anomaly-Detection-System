from flask import Flask, jsonify, request, render_template, url_for
import urllib.request
import json
import ast

app = Flask(__name__)

def getLocation():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        url = "https://geolocation-db.com/jsonp/" + request.environ['REMOTE_ADDR']
        ip = urllib.request.urlopen(url)
        data = ip.read().decode()
        data = data.split("(")[1].strip(")")
        return data
    else:
        url = "https://geolocation-db.com/jsonp/" + request.environ['HTTP_X_FORWARDED_FOR']
        ip = urllib.request.urlopen(url)
        data = ip.read().decode()
        data = data.split("(")[1].strip(")")
        return data

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/GeoIP', methods=['GET'])
def GeoIP():
    data = json.loads(getLocation().replace("'", "\""))
    print(type(data))
    return getLocation()

if __name__ == '__main__':
    app.run(host='118.34.62.168', port=5000, debug=True, use_reloader=False)

