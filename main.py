from flask import Flask
from flask import render_template
from flask import jsonify

import json

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/francy")
def francy():
	text= "FRANCY JULIETH"
	amigos=["Sebastian", "Pedro", "Ferney", "Julio M", "Monica"]
	return render_template('about.html', loco=text, amigos_list=amigos)

@app.route("/migrafo")
def migrafo():
	amigos=[{"name": "Francy", "nacio": 22}, {"name": "Pedro", "nacio": 22}, {"name": "Monica", "nacio": 42}]
	#return json.dumps(amigos)
	return jsonify(amigos)

@app.route("/grafo")
def grafo():
	amigos2=[{"name": "Francy", "nacio": 22}, {"name": "Pedro", "nacio": 22}, {"name": "Monica", "nacio": 42}]
	#return json.dumps(amigos)
	return jsonify(amigos2)

if __name__ == "__main__":
    app.run()