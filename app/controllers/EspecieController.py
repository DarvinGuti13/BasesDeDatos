from array import array
from app.models.Especie import Especie
from pathlib import Path
from flask import Blueprint, render_template, request, redirect, url_for

especie = Blueprint('especie',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@especie.route("/especie/guardar", methods=["POST"])
def __save_especie() -> str:
    nombre           = request.get_json()['nombre']
    nombre_cientifico        = request.get_json()['nombre_cientifico']
    descripcion        = request.get_json()['descripcion']

    nueva_especie = Especie(nombre, nombre_cientifico, descripcion)
    message = nueva_especie.guardar()

    return str('{"message": "%s"}' % message)

@especie.route("/especie/eliminar/<id>", methods=["POST","GET"])
def __eliminar_especie(id):
    Especie.eliminar(id)
    return redirect(url_for('especie.__mostrar_especie'))

@especie.route("/especie/actualizar", methods=["PUT"])
def __edit_especie() -> str:
    id_especie              = request.get_json()['id']
    nombre                  = request.get_json()['nombre']
    nombre_cientifico       = request.get_json()['nombre_cientifico']
    descripcion             = request.get_json()['descripcion']
    

    especie_to_edit = Especie.buscar(id_especie)
    message = especie_to_edit.actualizar(nombre, nombre_cientifico, descripcion)

    return str('{"message": "%s"}' % message)


@especie.route("/especie/mostrar", methods=["GET"])
def __mostrar_especie() -> str:
    return render_template('/especie/ListaEspecie.html')


@especie.route("/especie", methods=["GET"])
def __get_especie() -> str:
    resp = Especie.obtener_especie()
    return resp


@especie.route("/especie/buscar", methods=["GET"])
def __buscar_especie() -> str:
    id_especie = request.args['id']
    resp = Especie.buscar(id_especie)
    return resp.to_json_dict()


@especie.route("/especie/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('/especie/RegistrarEspecie.html')


@especie.route("/especie/editar/<id>", methods = ['GET', 'POST'])
def __formulario_edicion(id):
    return render_template('/especie/EditarEspecie.html', id=id)
