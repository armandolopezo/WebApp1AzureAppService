from flask import Flask, redirect
app = Flask(__name__)
@app.route('/')
def page():
    return redirect('http://github.com/', code=301)
if __name__ == "__main__":
    app.run()

  