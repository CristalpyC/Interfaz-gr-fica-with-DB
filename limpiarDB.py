#ejecuta este codigo para limpiar la base de datos completa
import sqlite3

from markupsafe import _escape_argspec

db = sqlite3.connect('baseDatos.db')
ClearDB = db.cursor()

ClearDB.execute('DELETE FROM formulario')
db.commit()
print('datos eliminados')

