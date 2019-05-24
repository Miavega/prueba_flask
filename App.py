from flask import Flask, render_template, request
#from flask_mysqldb import MySQL

app = Flask(__name__)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password'
#app.config['MYSQL_DB'] = ''
#mysql = MySQL()

@app.route('/')
def Index():
	return render_template('index.html')

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
	if request.method == 'POST':
		nombre = request.form['nombre']
		telefono = request.form['telefono']
		email = request.form['email']
		print(nombre)
		print(telefono)
		print(email)
		return 'Enviado'

@app.route('/modificar_usuario')
def modificar_usuario():
	return 'asdsa'

@app.route('/borrar_usuario')
def borrar_usuario():
	return 'asdsa'

@app.route('/consultar_usuario')
def consultar_usuario():
	return 'asdsa'

if __name__ == '__main__':
	app.run(port = 3000, debug = True)