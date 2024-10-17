from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

# Flask "
app = Flask(__name__, template_folder='datos')

#  base de datos y tabla 
def crear_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS asistentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            universidad TEXT NOT NULL,
            nivel_estudios TEXT NOT NULL,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            correo TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

crear_db()

#  formulario de registro
@app.route('/')
def index():
    return render_template('registro.html')

# manejos formulario
@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        universidad = request.form['universidad']
        nivel_estudios = request.form['nivel_estudios']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        password = request.form['password']

        #  almacenar e datos
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO asistentes (universidad, nivel_estudios, nombres, apellidos, correo, password) VALUES (?, ?, ?, ?, ?, ?)", 
                  (universidad, nivel_estudios, nombres, apellidos, correo, password))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
