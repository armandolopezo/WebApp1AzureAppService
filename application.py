from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
        <body>
            <h1>Welcome! My First Python WEB app, greetings ARMANDO LOPEZ</h1>
            <meta http-equiv="refresh" content="3;url=http://mediatech.com.ec/" />
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
