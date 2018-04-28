from flask import Flask, render_template, request, redirect, make_response
import json

import data
import time


app = Flask(__name__)

data.create_tables()
# data.create_horse()


@app.route("/")
def main_handler():
	return render_template('home.html', messages=[''])


@app.route("/stable")
def stable_handler():
	horses = data.get_horses(0)
	return render_template('stable.html', messages=[''], horses=horses)


@app.route("/create", methods=["GET", "POST", "DELETE"])
def create_handler():
	# if request.method == "POST":
	# 	horse = data.create_horses()
	return render_template('create.html', messages=[''])


@app.route("/races")
def races_handler():
	return render_template('races.html', messages=[''])


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5050)













