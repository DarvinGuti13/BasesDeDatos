from array import array
from app.models.Zona import Zona
from pathlib import Path
from flask import Blueprint, render_template, request, redirect, url_for

zona = Blueprint('zonas',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@zona.route("/zona/guardar", methods=["POST"])
def __save_zona() -> str:
    nombre           = request.get_json()['nombre']
    ext_cuad         = request.get_json()['ext_cuad']

    nueva_zona = Zona(nombre, ext_cuad)
    message = nueva_zona.guardar()

    return str('{"message": "%s"}' % message)

@zona.route("/zona/eliminar/<id>", methods=["POST","GET"])
def __eliminar_zonas(id):
    Zona.eliminar(id)
    return redirect(url_for('zonas.__mostrar_zonas'))

@zona.route("/zona/actualizar", methods=["PUT"])
def __edit_zonas() -> str:
    zonas_id         = request.get_json()['id']
    nombre           = request.get_json()['nombre']
    ext_mtscuad      = request.get_json()['ext_cuad']

    zonas_to_edit = Zona.buscar(zonas_id)
    message = zonas_to_edit.actualizar(nombre, ext_mtscuad)

    return str('{"message": "%s"}' % message)


@zona.route("/zona/mostrar", methods=["GET"])
def __mostrar_zonas() -> str:
    return render_template('/zona/ListaZona.html')


@zona.route("/zona", methods=["GET"])
def __get_zonas() -> str:
    resp = Zona.obtener_zonas()
    return resp


@zona.route("/zona/buscar", methods=["GET"])
def __buscar_zonas() -> str:
    zonas_id = request.args['id']
    resp = Zona.buscar(zonas_id)
    return resp.to_json_dict()


@zona.route("/zona/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('/zona/RegistrarZona.html')


@zona.route("/zona/editar/<id>", methods = ['GET', 'POST'])
def __formulario_edicion(id):
    return render_template('/zona/EditarZona.html', id=id)
