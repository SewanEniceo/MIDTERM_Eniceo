from flask import Flask
from flask import request
from flask import render_template

login = Flask(__name__)

@login.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    login.run(host="0.0.0.0", port=5000)