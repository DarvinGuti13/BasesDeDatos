from array import array
from contextlib import redirect_stderr
from curses import flash
from app.models.Cuidador import Cuidador
from pathlib import Path
from flask import Blueprint, render_template, request, redirect, url_for, flash

cuidador = Blueprint('cuidador',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@cuidador.route("/cuidador/guardar", methods=["POST"])
def __save_cuidador() -> str:
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
    fech_ingr         = request.get_json()['fech_ingr']

    nueva_persona = Cuidador(cedula,p_nom,s_nom,p_ape,s_ape,id_barr,id_dist,id_cant,id_prov,id_pais,tel_per,tel_tra,tel_otr,cor_per,cor_tra,cor_otr,fech_ingr)
    message = nueva_persona.guardar()

    return str('{"message": "%s"}' % message)


@cuidador.route("/cuidador/actualizar", methods=["PUT"])
def __edit_cuidador() -> str:
    cedula           = request.get_json()['cedula'] 
    p_nom           = request.get_json()['p_nom']
    s_nom           = request.get_json()['s_nom']
    p_ape           = request.get_json()['p_ape']
    s_ape           = request.get_json()['s_ape']
    fech_ingr         = request.get_json()['fech_ingr']

    persona_to_edit = Cuidador.buscar(cedula)
    message = persona_to_edit.actualizar(p_nom,s_nom, p_ape,s_ape,fech_ingr)

    return str('{"message": "%s"}' % message)

@cuidador.route("/cuidador/eliminar/<ced>", methods=['POST','GET'])
def __delete_cuidador(ced):
    cedula          = ced
    Cuidador.eliminar(cedula)
    flash('¡Se ha eliminado con exito!')
    return redirect(url_for('cuidador.__mostrar_cuidador'))


@cuidador.route("/cuidador/mostrar", methods=["GET"])
def __mostrar_cuidador() -> str:
    return render_template('/cuidador/ListaCuidador.html')


@cuidador.route("/cuidador", methods=["GET"])
def __get_cuidador() -> str:
    resp = Cuidador.obtener_cuidador()
    return resp


@cuidador.route("/cuidador/buscar", methods=["GET"])
def __buscar_cuidador() -> str:
    user_id = request.args['id']
    resp = Cuidador.buscar(user_id)
    return resp.to_json_dict()


@cuidador.route("/cuidador/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('/cuidador/RegistrarCuidador.html')


@cuidador.route("/cuidador/editar/<ced>", methods=["GET"])
def __formulario_edicion(ced):
    return render_template('/cuidador/EditarCuidador.html',cedula=ced)

@cuidador.route("/cuidador/detalles/<ced>", methods=["GET"])
def __formulario_detalles(ced):
    return render_template('/cuidador/DetallesCuidador.html',cedula=ced)
