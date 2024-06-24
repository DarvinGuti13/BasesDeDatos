from array import array
from contextlib import redirect_stderr
from curses import flash
from app.models.Guia import Guia
from pathlib import Path
from flask import Blueprint, render_template, request, redirect, url_for, flash

guia = Blueprint('guia',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@guia.route("/guia/guardar", methods=["POST"])
def __save_guia() -> str:
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
    fech_ini         = request.get_json()['fech_ini']

    nueva_persona = Guia(cedula,p_nom,s_nom,p_ape,s_ape,id_barr,id_dist,id_cant,id_prov,id_pais,tel_per,tel_tra,tel_otr,cor_per,cor_tra,cor_otr,fech_ini)
    message = nueva_persona.guardar()

    return str('{"message": "%s"}' % message)


@guia.route("/guia/actualizar", methods=["PUT"])
def __edit_guia() -> str:
    cedula           = request.get_json()['cedula'] 
    p_nom           = request.get_json()['p_nom']
    s_nom           = request.get_json()['s_nom']
    p_ape           = request.get_json()['p_ape']
    s_ape           = request.get_json()['s_ape']
    fech_ini         = request.get_json()['fech_ini']

    guia_to_edit = Guia.buscar(cedula)
    message = guia_to_edit.actualizar(p_nom,s_nom, p_ape,s_ape,fech_ini)

    return str('{"message": "%s"}' % message)

@guia.route("/guia/eliminar/<ced>", methods=['POST','GET'])
def __delete_guia(ced):
    cedula          = ced
    Guia.eliminar(cedula)
    flash('¡Se ha eliminado con exito!')
    return redirect(url_for('guia.__mostrar_guia'))


@guia.route("/guia/mostrar", methods=["GET"])
def __mostrar_guia() -> str:
    return render_template('/guia/ListaGuia.html')


@guia.route("/guia", methods=["GET"])
def __get_guia() -> str:
    resp = Guia.obtener_guia()
    return resp


@guia.route("/guia/buscar", methods=["GET"])
def __buscar_guia() -> str:
    user_id = request.args['id']
    resp = Guia.buscar(user_id)
    return resp.to_json_dict()


@guia.route("/guia/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('/guia/RegistrarGuia.html')


@guia.route("/guia/editar/<ced>", methods=["GET"])
def __formulario_edicion(ced):
    return render_template('/guia/EditarGuia.html',cedula=ced)

@guia.route("/guia/detalles/<ced>", methods=["GET"])
def __formulario_detalles(ced):
    return render_template('/guia/DetallesGuia.html',cedula=ced)
