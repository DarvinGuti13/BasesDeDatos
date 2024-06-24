from array import array
from re import I
from app.models.Itinerario import Itinerario
from pathlib import Path
from flask import Blueprint, render_template, request, redirect, url_for

itinerario = Blueprint('itinerario',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@itinerario.route("/itinerario/guardar", methods=["POST"])
def __save_itinerario() -> str:
    duracion_recorrido                 = request.get_json()['duracion_recorrido']
    logitud_recorrido                  = request.get_json()['longitud_recorrido']
    maximo_visitantes_Aut              = request.get_json()['maximo_visitantes_Aut']
    id_especie                         = request.get_json()['id_especie']

    nuevo_itinerario = Itinerario (duracion_recorrido, logitud_recorrido, maximo_visitantes_Aut, id_especie)
    message = nuevo_itinerario.guardar()

    return str('{"message": "%s"}' % message)

@itinerario.route("/itinerario/eliminar/<codigo>", methods=["POST","GET"])
def __eliminar_itinerario(codigo):
    Itinerario.eliminar(codigo)
    return redirect(url_for('itinerario.__mostrar_itinerario'))

@itinerario.route("/itinerario/actualizar", methods=["PUT"])
def __edit_itinerario() -> str:
    codigo_itinerario             = request.get_json()['codigo']
    duracion_recorrido            = request.get_json()['duracion_recorrido']
    logitud_recorrido             = request.get_json()['longitud_recorrido']
    maximo_visitantes_Aut         = request.get_json()['maximo_visitantes_Aut']
    id_especie                    = request.get_json()['id_especie']

    itinerario_to_edit = Itinerario.buscar(codigo_itinerario)
    message = itinerario_to_edit.actualizar(duracion_recorrido, logitud_recorrido, maximo_visitantes_Aut, id_especie)

    return str('{"message": "%s"}' % message)


@itinerario.route("/itinerario/mostrar", methods=["GET"])
def __mostrar_itinerario() -> str:
    return render_template('/itinerario/ListaItinerarios.html')


@itinerario.route("/itinerario", methods=["GET"])
def __get_itienerario() -> str:
    resp = Itinerario.obtener_Itinerario()
    return resp


@itinerario.route("/itinerario/buscar", methods=["GET"])
def __buscar_itinerario() -> str:
    codigo_itinerario = request.args['codigo']
    resp = Itinerario.buscar(codigo_itinerario)
    return resp.to_json_dict()


@itinerario.route("/itinerario/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('/itinerario/RegistrarItinerario.html')


@itinerario.route("/itinerario/editar/<codigo>", methods = ['GET', 'POST'])
def __formulario_edicion(codigo):
    return render_template('/itinerario/EditarItinerarios.html', codigo=codigo)
