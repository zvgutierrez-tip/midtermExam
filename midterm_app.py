from flask import Flask
from flask import request
from flask import render_template

design = Flask(__name__)

@design.route("/")

def main():
    return render_template("login.html")
@design.route("/registration")

def registration():
    return render_template("registration.html")


if __name__ == "__main__":
    design.run(host="0.0.0.0",port=5000)