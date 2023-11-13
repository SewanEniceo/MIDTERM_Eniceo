from flask import Flask
from flask import request
from flask import render_template

login = Flask(__name__)


@login.route("/")
def main():
    return render_template("login.html")

@login.route("/registration.html")
def registration():
    return render_template("registration.html")

@login.route("/login.html")
def backTologin():
    return render_template("login.html")

if __name__ == "__main__":
    login.run(host="0.0.0.0", port=5000)


    