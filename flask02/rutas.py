from flask import Flask, render_template
from modelos import Producto

app = Flask(__name__)

@app.route('/')
def inicio():
  productos = [Producto("Manzanas", 12), Producto("Pera", 13)]
  return render_template('index.hmtl', xxx=productos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)