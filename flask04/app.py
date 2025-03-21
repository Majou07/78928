from flask import Flask, render_template
from producto import Producto
from flask import request
from flask import Response
from flask import redirect, url_for

app = Flask(__name__)
productos = [Producto("computadora", 200), Producto("impresora", 50)]

@app.route('/')
def index():
  return render_template('productos.html', productos=productos)


@app.route('/editar/<producto>/<precio>')
def editar(producto, precio):
  # recuperar producto
  p = Producto(producto, precio)
  #print(producto)
  return render_template('editar.html', producto=producto, precio=precio)
  #profe   return render_template('editar.html', producto=p)


@app.route('/eliminar/<producto>')
def eliminar(producto):
  for i, p in enumerate(productos):
    if p.nombre == producto:
      del productos[i]
  return Response("eliminado", headers={'Location': '/'}, status=302)

#respuesta del profe
#@app.route('/eliminar/<producto>')
#def eliminar(producto):
  #i = 0
  #for e in productos:
    #if e.nombre == nombre:
      #productos.pop(i)
            #print(f"{e.nombre} {e.precio}") 
      #i+=1
  #return Response("eliminado", headers={'Location': '/'}, status=302)


@app.route('/crear', methods=['POST'])
def crear():
   n=request.form.get('nombre')
   p=request.form.get('precio')
   productos.append(Producto(n,p))
   return redirect(url_for('index'))



@app.route('/guardar', methods=['POST'])
def guardar():
  n=request.form.get('nombre')
  p=request.form.get('precio')
  print(n , p)
  i = 0
  for e in productos:
    if e.nombre == n:
      productos[i] = Producto(n,p)
      print(f"{e.nombre} {e.precio}") 
    i+=1
  return Response("guardado", headers={'Location': '/'}, status=302) #location: buscar una ruta a la cual redirigirnos


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)