from flask import Flask, render_template, request, redirect, make_response
import json


app = Flask(__name__)


@app.route("/")
def main_handler():
	return render_template('home.html')

@app.route("/stable")
def stable_handler():
	horses = [{'name':'HorseyHorse', 'gender': 'female'}]
	return render_template('stable.html', horses=horses)

@app.route("/races")
def races_handler():
	return render_template('races.html')


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5050)
	












