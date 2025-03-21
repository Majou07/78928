from flask import Flask, render_template
from producto import Producto
from flask import request
from flask import Response
from flask import redirect, url_for
import sqlite3

app = Flask(__name__)
#productos = [Producto("computadora", 200), Producto("impresora", 50)]

@app.route('/')
def index():
  con = conexion()
  productos = con.execute("select * from productos").fetchall()
  con.close()
  return render_template('productos.html', productos=productos)


@app.route('/editar/<id>')
def editar(id):
  con = conexion()
  p = con.execute('select * from productos where id = ?', (id)).fetchone()
  con.close()
  return render_template('editar.html', producto=p)


@app.route('/guardar', methods=['POST'])
def guardar():
  n=request.form.get('nombre')
  p=request.form.get('precio')
  id=request.form.get('id')
  print(f"{n} {p} {id}")
  #i = 0
  #for e in productos:
    #if e.nombre == n:
      #productos[i] = Producto(n,p)
      #print(f"{e.nombre} {e.precio}") 
    #i+=1
  con = conexion()
  con.execute('update productos set nombre=?, precio=? where id = ?', (n,p,id))
  con.commit()
  con.close()
  return Response("guardado", headers={'Location': '/'}, status=302) #location: buscar una ruta a la cual redirigirnos




@app.route('/eliminar/<id>')
def eliminar(id):
  #i = 0
  #for e in productos:
    #if e.nombre == nombre:
      #productos.pop(i)
            #print(f"{e.nombre} {e.precio}") 
      #i+=1
  con = conexion()
  con.execute('delete from productos where id=?', (id))
  con.commit()
  con.close()
  return Response("eliminado", headers={'Location': '/'}, status=302)


@app.route('/crear', methods=['POST'])
def crear():
   n=request.form.get('nombre')
   p=request.form.get('precio')
   con = conexion()
   con.execute('insert into productos (nombre, precio) values (?,?)', (n,p))
   con.commit()
   con.close()
   return redirect(url_for('index'))




def conexion():
  con = sqlite3.connect('basedatos.db')
    # hace que las consultas se vuelvan diccionarios pudiendo 
    # seleccionar valores mediante ['nombre_columna']
  con.row_factory = sqlite3.Row
  return con

  
def iniciar_db():
    con = conexion()
    #se crea la tabla 
    con.execute('''
        CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
        )
   ''')
    con.commit() #salva los datos despues de la ejecucion
    con.close()



if __name__ == '__main__':
 iniciar_db()
 app.run(host='0.0.0.0', debug=True)