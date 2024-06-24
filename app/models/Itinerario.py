from ..database.Postgresql import Postgres

class Itinerario():

    __codigo_itinerario         = int
    __duracion_recorrido        = str
    __longitud_recorrido        = str
    __maximo_visitantes_Aut    = str
    __id_especie               = int



    def __init__(self, duracion_recorrido : str, longitud_recorrido : str, maximo_visitantes_Aut : str, id_especie : int):
        print("Nuevo itinerario")
        self.__codigo_itinerario            = 0
        self.__duracion_recorrido           = duracion_recorrido
        self.__longitud_recorrido           = longitud_recorrido
        self.__maximo_visitantes_Aut        = maximo_visitantes_Aut
        self.__id_especie                   = id_especie

    def actualizar(self, duracion_recorrido, longitud_recorrido, maximo_visitantes_Aut, id_especie) -> str:
        if self.__codigo_itinerario <= 0 :
            return 'Error: Itinerario no registrado'
        
        self.__duracion_recorrido               = duracion_recorrido
        self.__longitud_recorrido               = longitud_recorrido
        self.__maximo_visitantes_Aut            = maximo_visitantes_Aut
        self.__id_especie                       = id_especie

        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "ActualizarItinerario"(%s,%s,%s,%s,%s)', 
            (self.__codigo_itinerario, self.__duracion_recorrido, self.__longitud_recorrido, self.__maximo_visitantes_Aut, self.__id_especie)
        )
        connection.commit()
        postgres_repository.close_connection()
        
        return 'Itinerario actualizado'

    def eliminar(zona_id):
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "EliminarItinerario"(%s)', (zona_id,))
        connection.commit()
        postgres_repository.close_connection()

    def guardar(self) -> str:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "InsertarItinerario"(%s, %s, %s, %s)', 
            (self.__duracion_recorrido, self.__longitud_recorrido, self.__maximo_visitantes_Aut, self.__id_especie)
        )
        connection.commit()
        postgres_repository.close_connection()
        return 'Itinerario guardado'

    
    @staticmethod
    def obtener_Itinerario() -> dict:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM itinerario').fetchall()
        postgres_repository.close_connection()
        response = {}
        index = 1
        for itinerario in data:
            response[str(index)] = { 'codigo_itinerario' : itinerario[0], 'duracion_recorrido' : itinerario[1], 'longitud_recorrido' : itinerario[2], 'maximo_visitantes_Aut' : itinerario[3], 'especie' : itinerario[4] }
            index += 1
        return response

    @staticmethod
    def buscar(codigo_itinerario: int) -> object:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM "Itinerario" WHERE "Codigo_Itinerario" = %s', (codigo_itinerario,)).fetchone()
        postgres_repository.close_connection()

        itinerario = Itinerario(data[1], data[2], data[3], data[4])
        itinerario.__codigo_itinerario = data[0]
        return itinerario


    def to_json_dict(self) -> dict:
        return {'Codigo_itinerario' : self.__codigo_itinerario, 'Duracion_recorrido' : self.__duracion_recorrido, 'Longitud_recorrido' : self.__longitud_recorrido, 'Maximo_visitantes' : self.__maximo_visitantes_Aut, 'Id_especie' : self.__id_especie}
