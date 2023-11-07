from flask import Flask
from datetime import datetime

app = Flask(__name__)  

@app.route('/time')
def time():
    now = datetime.now()
    responseBody = now.strftime("%H:%M:%S")
    return responseBody

# modify response headers for all requests
@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

app.run(debug=True, port=8080, host="0.0.0.0")