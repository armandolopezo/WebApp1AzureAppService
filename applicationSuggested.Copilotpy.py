import time
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Hello Best Bike App!</h1></body></html>\n"

@app.route('/redirect')
def page():
    return redirect('http://mediatech.com.ec/', code=301)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)