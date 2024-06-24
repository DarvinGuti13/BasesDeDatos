from .global_routes import inicio as __inicio, head as __header, dbstate as __dbstate
from .controllers import usuarios as __usuarios, persona as __persona, habitat as __habitat, zona as __zona, guia as __guia, cuidador as __cuidador, especie as __especie, itinerario as __itinerario
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config/flask_config.cfg")
app.register_blueprint(__dbstate)
app.register_blueprint(__inicio)
app.register_blueprint(__header)
app.register_blueprint(__usuarios)
app.register_blueprint(__persona)
app.register_blueprint(__zona)
app.register_blueprint(__habitat)
app.register_blueprint(__guia)
app.register_blueprint(__cuidador)
app.register_blueprint(__especie)
app.register_blueprint(__itinerario)