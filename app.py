from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ip')
def ip():
    response = requests.get("https://httpbin.org/ip")
    json = response.json()
    result = json['origin'].split(',')[0]
    return jsonify({"ip":result})

if __name__ == '__main__':
    app.run()
