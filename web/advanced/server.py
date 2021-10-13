from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Life is short, you need Python!"

@app.route("/api", methods=['POST'])
def test():
    return request.form['name']

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
