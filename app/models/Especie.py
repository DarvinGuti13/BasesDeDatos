from ..database.Postgresql import Postgres

class Especie():

    __id_especie          = int
    __nombre            = str
    __nombre_Cientifico = str
    __descripcion = str
    


    def __init__(self, nombre : str, nombre_Cientifico : str, descripcion : str):
        print("Nueva especie")
        self.__id_especie          = 0
        self.__nombre            = nombre
        self.__nombre_Cientifico      = nombre_Cientifico
        self.__descripcion      = descripcion


    def actualizar(self, nombre, nombre_Cientifico, descripcion) -> str:
        if self.__id_especie <= 0 :
            return 'Error: Especie no registrada'
        self.__nombre               = nombre
        self.__nombre_Cientifico    = nombre_Cientifico
        self.__descripcion          = descripcion

        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "ActualizarEspecie"(%s,%s,%s,%s)', 
            (self.__id_especie, self.__nombre, self.__nombre_Cientifico, self.__descripcion)
        )
        connection.commit()
        postgres_repository.close_connection()
        
        return 'Especie actualizada'

    def eliminar(id_especie):
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "EliminarEspecie"(%s)', (id_especie,))
        connection.commit()
        postgres_repository.close_connection()

    def guardar(self) -> str:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "InsertarEspecie"(%s, %s, %s)', 
            (self.__nombre, self.__nombre_Cientifico, self.__descripcion)
        )
        connection.commit()
        postgres_repository.close_connection()
        return 'Especie guardada'

    
    @staticmethod
    def obtener_especie() -> dict:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM "Especie"').fetchall()
        postgres_repository.close_connection()
        response = {}
        index = 1
        for especie in data:
            response[str(index)] = { 'id' : especie[0], 'nombre' : especie[1], 'nombre_cientifico' : especie[2], 'descripcion' : especie[3] }
            index += 1
        return response

    @staticmethod
    def buscar(id_esp: int) -> object:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM "Especie" WHERE "Numero_Especie" = %s', (id_esp,)).fetchone()
        postgres_repository.close_connection()

        especie = Especie(data[1], data[2], data[3])
        especie.__id_especie = data[0]
        return especie


    def to_json_dict(self) -> dict:
        return {'Id_Especie' : self.__id_especie, 'Nombre' : self.__nombre, 'Nombre_Cientifico' : self.__nombre_Cientifico, 'Descripcion' : self.__descripcion}
