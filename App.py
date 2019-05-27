from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:miguelangel@localhost/PruebaFlask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models.models import *

app.secret_key = 'clave-secreta'

@app.route('/')
def Index():
	return render_template('index.html')

@app.route('/equipo')
def equipo():
	return render_template('equipo.html', equipos = consultar_equipo())

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
	nombre = request.args.get('nombre')
	email=request.args.get('email')
	equipo=request.args.get('equipo')
	try:
		usuario=Usuario(
			nombre=nombre,
            email=email,
            equipo=equipo
        )
		db.session.add(usuario)
		db.session.commit()
		flash("Usuario creado. usuario id={}".format(usuario.id))
		return redirect(url_for('equipo'))
	except Exception as e:
		return(str(e))

@app.route('/modificar_usuario')
def modificar_usuario():
	return 'asdsa'

@app.route('/borrar_usuario')
def borrar_usuario():
	return 'asdsa'

@app.route('/consultar_usuario')
def consultar_usuario():
	return 'asdsa'

@app.route('/crear_equipo', methods=['POST'])
def crear_equipo():
	if request.method == 'POST':
		nombre = request.form['nombre']
		desc_equipo = request.form['desc_equipo']
		try:
			equipo=Equipo(
				nombre=nombre,
				desc_equipo=desc_equipo,
			)
			db.session.add(equipo)
			db.session.commit()
			flash("Equipo creado. equipo id={}".format(equipo.id))
			return redirect(url_for('equipo'))
		except Exception as e:
			return(str(e))

@app.route('/modificar_equipo')
def modificar_equipo():
	return 'asdsa'

@app.route('/borrar_equipo')
def borrar_equipo():
	return 'asdsa'

@app.route('/consultar_equipo', methods=['GET'])
def consultar_equipo():
	try:
		equipos=Equipo.query.all()
		return  jsonify([equipo.serialize() for equipo in equipos])
	except Exception as e:
		return(str(e))

if __name__ == '__main__':
	app.run(port = 3000, debug = True)
