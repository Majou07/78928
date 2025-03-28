from flask import Blueprint

rutas_bp = Blueprint('rutas', __name__, url_prefix='/api/v1')

@rutas_bp.route('/ruta1')
def rita1():
  return 'Esta es la ruta 1'


@rutas_bp.route('/ruta2')
def rita2():
  return 'Esta es la ruta 2'