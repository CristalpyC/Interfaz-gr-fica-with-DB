from pickle import TRUE
from flask import Flask, render_template, flash, request
import sqlite3

db = sqlite3.connect('baseDatos.db', check_same_thread=False)
cursor = db.cursor()

class Formulario:
    def __init__(self, nombre, apellido, correo, asunto, mensaje):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.asunto = asunto
        self.mensaje = mensaje
        
    def Formulario_datos(self):
        
        
        datos = self.nombre, self.apellido, self.correo, self.asunto, self.mensaje
        cursor.execute('INSERT into formulario(nombre, apellido, correo, asunto, mensaje) VALUES(?, ?, ?, ?, ?)', datos)
        db.commit()
        flash(f'mensaje enviado con exito: " {self.correo} "!', 'success')
  
        return render_template('formulario.html')
        
app = Flask(__name__)
app.config['SECRET_KEY'] = 'titiri'

@app.route('/')
def Inicio():
    return render_template('formulario.html')

@app.route('/formulario', methods=['POST'])
def Formulario_user():
    nombre = request.form['nombre']
    apellido = request.form['apellidos']
    correo = request.form['email']
    asunto = request.form['asunto']
    mensaje = request.form['mensaje']
    
    objeto = Formulario(nombre, apellido, correo, asunto, mensaje)
    
    return objeto.Formulario_datos()

if __name__ =='__main__':
    app.run(debug=True)