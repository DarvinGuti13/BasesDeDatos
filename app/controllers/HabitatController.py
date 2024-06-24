from array import array
from crypt import methods
from app.models.Habitat import Habitat
from pathlib import Path
from flask import Blueprint, render_template, request, redirect, url_for

habitat = Blueprint('habitats',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@habitat.route("/habitat/guardar", methods=["POST"])
def __save_habitats() -> str:
    nombre        = request.get_json()['nombre']
    clima         = request.get_json()['clima']
    vege          = request.get_json()['vege']
    cont          = request.get_json()['cont']

    nueva_habitats = Habitat(nombre, clima, vege, cont)
    message = nueva_habitats.guardar()

    return str('{"message": "%s"}' % message)


@habitat.route("/habitat/actualizar", methods=["PUT"])
def __edit_habitats() -> str:
    hab_id        = request.get_json()['id']
    nombre        = request.get_json()['nombre']
    clima         = request.get_json()['clima']
    vege          = request.get_json()['vege']
    cont          = request.get_json()['cont']

    habitats_to_edit = Habitat.buscar(hab_id)
    message = habitats_to_edit.actualizar(nombre, clima, vege, cont)

    return str('{"message": "%s"}' % message)

@habitat.route("/habitat/eliminar/<id>", methods=["POST","GET"])
def __eliminar_habitats(id):
    Habitat.eliminar(id)
    return redirect(url_for('habitats.__mostrar_habitats'))

@habitat.route("/habitat/mostrar", methods=["GET"])
def __mostrar_habitats() -> str:
    return render_template('/habitat/ListaHabitat.html')


@habitat.route("/habitat", methods=["GET"])
def __get_habitats() -> str:
    resp = Habitat.obtener_habitats()
    return resp


@habitat.route("/habitat/buscar", methods=["GET"])
def __buscar_habitats() -> str:
    user_id = request.args['id']
    resp = Habitat.buscar(user_id)
    return resp.to_json_dict()


@habitat.route("/habitat/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('/habitat/RegistrarHabitat.html')


@habitat.route("/habitat/editar/<id>", methods=["GET"])
def __formulario_edicion(id):
    return render_template('/habitat/EditarHabitat.html',id=id)
