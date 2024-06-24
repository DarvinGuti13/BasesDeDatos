from ..database.Postgresql import Postgres

class Zona():

    __id_zona           = int
    __nombre            = str
    __ext_ocup = str


    def __init__(self, nombre : str, ext_ocup : str):
        print("Nuevo usuario")
        self.__id_zona           = 0
        self.__nombre            = nombre
        self.__ext_ocup          = ext_ocup

    def actualizar(self, nombre, ext_ocup) -> str:
        if self.__id_zona <= 0 :
            return 'Error: Usuario no registrado'
        
        self.__nombre       = nombre
        self.__ext_ocup     = ext_ocup

        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "ActualizarZona"(%s,%s,%s)', 
            (self.__id_zona, self.__nombre, self.__ext_ocup)
        )
        connection.commit()
        postgres_repository.close_connection()
        
        return 'Usuario actualizado'

    def eliminar(zona_id):
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "EliminarZona"(%s)', (zona_id,))
        connection.commit()
        postgres_repository.close_connection()

    def guardar(self) -> str:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "InsertarZona"(%s, %s)', 
            (self.__nombre, self.__ext_ocup)
        )
        connection.commit()
        postgres_repository.close_connection()
        return 'Usuario guardado'

    
    @staticmethod
    def obtener_zonas() -> dict:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM "Zona"').fetchall()
        postgres_repository.close_connection()
        response = {}
        index = 1
        for zona in data:
            response[str(index)] = { 'id' : zona[0], 'nombre' : zona[1], 'ext_ocup' : zona[2] }
            index += 1
        return response

    @staticmethod
    def buscar(zona_id: int) -> object:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM "Zona" WHERE "Id_Zona" = %s', (zona_id,)).fetchone()
        postgres_repository.close_connection()

        zona = Zona(data[1], data[2])
        zona.__id_zona = data[0]
        return zona


    def to_json_dict(self) -> dict:
        return {'Id_Zona' : self.__id_zona, 'Nombre' : self.__nombre, 'Extension_Ocupada' : self.__ext_ocup}
