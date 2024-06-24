from array import array
from contextlib import redirect_stderr
from curses import flash
from app.models.Persona import Persona
from pathlib import Path
from flask import Blueprint, render_template, request, redirect, url_for, flash

persona = Blueprint('persona',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@persona.route("/persona/guardar", methods=["POST"])
def __save_persona() -> str:
    cedula           = request.get_json()['ced'] 
    p_nom           = request.get_json()['p_nom']
    s_nom           = request.get_json()['s_nom']
    p_ape           = request.get_json()['p_ape']
    s_ape           = request.get_json()['s_ape']
    id_pais           = request.get_json()['id_pais']
    id_prov           = request.get_json()['id_prov']
    id_cant           = request.get_json()['id_cant']
    id_dist           = request.get_json()['id_dist']
    id_barr           = request.get_json()['id_barr']
    tel_per           = request.get_json()['tel_per']
    tel_tra           = request.get_json()['tel_tra']
    tel_otr           = request.get_json()['tel_otr']
    cor_per           = request.get_json()['cor_per']
    cor_tra           = request.get_json()['cor_tra']
    cor_otr           = request.get_json()['cor_otr']

    nueva_persona = Persona(cedula,p_nom,s_nom,p_ape,s_ape,id_barr,id_dist,id_cant,
        id_prov,id_pais,tel_per,tel_tra,tel_otr,cor_per,cor_tra,cor_otr)
    message = nueva_persona.guardar()

    return str('{"message": "%s"}' % message)


@persona.route("/persona/actualizar", methods=["PUT"])
def __edit_persona() -> str:
    cedula          = request.get_json()['cedula'] 
    p_nom           = request.get_json()['p_nom']
    s_nom           = request.get_json()['s_nom']
    p_ape           = request.get_json()['p_ape']
    s_ape           = request.get_json()['s_ape']

    persona_to_edit = Persona.buscar(cedula)
    message = persona_to_edit.actualizar(p_nom,s_nom,p_ape,s_ape)

    return str('{"message": "%s"}' % message)

@persona.route("/persona/eliminar/<ced>", methods=['POST','GET'])
def __delete_persona(ced):
    cedula          = ced
    Persona.eliminar(cedula)
    flash('¡Se ha eliminado con exito!')
    return redirect(url_for('persona.__mostrar_persona'))


@persona.route("/persona/mostrar", methods=["GET"])
def __mostrar_persona() -> str:
    return render_template('/persona/ListaPersona.html')


@persona.route("/persona", methods=["GET"])
def __get_persona() -> str:
    resp = Persona.obtener_persona()
    return resp


@persona.route("/persona/buscar", methods=["GET"])
def __buscar_persona() -> str:
    user_id = request.args['id']
    resp = Persona.buscar(user_id)
    return resp.to_json_dict()


@persona.route("/persona/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('/persona/RegistrarPersona.html')


@persona.route("/persona/editar/<cedula>", methods=["GET"])
def __formulario_edicion(cedula):
    return render_template('/persona/EditarPersona.html',cedula=cedula)

@persona.route("/persona/detalles/<cedula>", methods=["GET"])
def __formulario_detalles(cedula):
    return render_template('/persona/DetallesPersona.html',cedula=cedula)
