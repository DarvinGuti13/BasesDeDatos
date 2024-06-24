from ..database.Postgresql import Postgres

class Habitat():

    __id_habitat     = int
    __nombre         = str
    __clima          = str
    __vege           = str
    __cont           = str


    def __init__(self, nombre : str, clima : str, vege : str, cont : str):
        print("Nuevo usuario")
        self.__id_habitat        = 0
        self.__nombre            = nombre
        self.__clima             = clima
        self.__vege              = vege
        self.__cont              = cont

    def actualizar(self, nombre, clima, vege, cont) -> str:
        if self.__id_habitat <= 0 :
            return 'Error: Usuario no registrado'
        
        self.__nombre            = nombre
        self.__clima             = clima
        self.__vege              = vege
        self.__cont              = cont

        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "ActualizarHabitat"(%s,%s,%s,%s,%s)', 
            (str(self.__id_habitat), self.__nombre, self.__clima, self.__vege, self.__cont)
        )
        connection.commit()
        postgres_repository.close_connection()
        
        return 'Usuario actualizado'

    def guardar(self) -> str:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "InsertarHabitat"(%s, %s, %s, %s)', 
            (self.__nombre, self.__clima, self.__vege, self.__cont)
        )
        connection.commit()
        postgres_repository.close_connection()
        return 'Usuario guardado'

    def eliminar(hab_id):
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "EliminarHabitat"(%s)', (hab_id,))
        connection.commit()
        postgres_repository.close_connection()
    
    @staticmethod
    def obtener_habitats() -> dict:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM habitat').fetchall()
        postgres_repository.close_connection()

        response = {}
        index = 1
        for habitat in data:
            response[str(index)] = { 'id' : habitat[0], 'nombre' : habitat[1], 'clima' : habitat[2], 'tipo_vegetacion' : habitat[3], 'continente' : habitat[4] }
            index += 1
        return response

    @staticmethod
    def buscar(hab_id: int) -> object:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM habitat WHERE "ID" = %s', (hab_id,)).fetchone()
        postgres_repository.close_connection()

        hab = Habitat(data[1], data[2], data[3], data[4])
        hab.__id_habitat = data[0]
        return hab

    def to_json_dict(self) -> dict:
        return {'nombre': self.__nombre, 'clima': self.__clima, 'vegetacion': self.__vege, 'continente': self.__cont}

        
