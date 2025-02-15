from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/')
def page():
    return redirect('http://mediatech.com.ec/', code=301)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    print ("Running on port: ", port)
    app.run(host='0.0.0.0', port=port)