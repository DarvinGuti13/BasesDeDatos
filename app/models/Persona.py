from ..database.Postgresql import Postgres

class Persona():

    __cedula                = str
    __p_nombre              = str
    __s_nombre              = str
    __p_apellido            = str
    __s_apellido            = str
    __id_barrio             = str
    __id_distrito           = str
    __id_canton             = str
    __id_provincia          = str
    __id_pais               = str
    __tel_trabajo           = str
    __tel_personal          = str
    __tel_otros             = str
    __cor_trabajo           = str
    __cor_personal          = str
    __cor_otros             = str

    def __init__(self, cedula : str, p_nombre : str, s_nombre : str, p_apellido : str, s_apellido : str, id_barrio : str, id_distrito : str, id_canton : str, id_provincia : str, id_pais : str, tel_personal : str, tel_trabajo : str, tel_otros : str, cor_personal : str, cor_trabajo : str, cor_otros : str):
        print("Nueva persona")
        self.__cedula                = cedula
        self.__p_nombre              = p_nombre
        self.__s_nombre              = s_nombre
        self.__p_apellido            = p_apellido
        self.__s_apellido            = s_apellido
        self.__id_barrio             = id_barrio
        self.__id_distrito           = id_distrito
        self.__id_canton             = id_canton
        self.__id_provincia          = id_provincia
        self.__id_pais               = id_pais
        self.__tel_trabajo           = tel_trabajo
        self.__tel_personal          = tel_personal
        self.__tel_otros             = tel_otros
        self.__cor_trabajo           = cor_trabajo
        self.__cor_personal          = cor_personal
        self.__cor_otros             = cor_otros


    def actualizar(self, p_nom, s_nom, p_ape, s_ape) -> str:
        if not self.__cedula :
            return 'Error: Usuario no registrado'
        
        self.__p_nombre = p_nom
        self.__s_nombre = s_nom
        self.__p_apellido = p_ape
        self.__s_apellido = s_ape

        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "ActualizarPersona"(%s,%s,%s,%s,%s)', 
            ( self.__cedula, self.__p_nombre, self.__s_nombre, self.__p_apellido,self.__s_apellido)
        )
        connection.commit()
        postgres_repository.close_connection()
        return 'Usuario actualizado'

    def eliminar(cedula):
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "EliminarPersona"('"'{0}'"')'.format(cedula))
        connection.commit()
        postgres_repository.close_connection()


    def guardar(self) -> str:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('CALL "InsertarPersona"(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', 
            (self.__cedula, self.__p_nombre, self.__s_nombre, self.__p_apellido, self.__s_apellido, self.__id_pais, 
            self.__id_provincia, self.__id_canton, self.__id_distrito, self.__id_barrio, self.__tel_personal, self.__tel_trabajo, 
            self.__tel_otros, self.__cor_personal, self.__cor_trabajo, self.__cor_otros)
        )
        connection.commit()
        postgres_repository.close_connection()
        return 'Usuario guardado'

    
    @staticmethod
    def obtener_persona() -> dict:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM persona').fetchall()
        postgres_repository.close_connection()

        response = {}
        index = 1
        for persona in data:
            response[str(index)] = { 'cedula' : persona[0], 'nombre' : persona[1] + ' ' + persona[2] + ' ' + 
            persona[3] + ' ' + persona[4], 'direccion' : persona[5] + ', ' + persona[6] + ', ' + persona[7] + ', ' + 
            persona[8] + ', ' + persona[9],'tel_per' : persona[10],'tel_tr' : persona[11],'tel_otr' : persona[12],
            'cor_per' : persona[13],'cor_tr' : persona[14],'cor_otr' : persona[15]}
            index += 1
        return response

    @staticmethod
    def buscar(user_id: str) -> object:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM persona WHERE "Cedula" = %s', (user_id,)).fetchone()
        postgres_repository.close_connection()
        user = Persona(data[0],data[1],data[2],data[3],data[4],data[5],data[6],
            data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15])
        return user

    def to_json_dict(self) -> dict:
        return {'id' : self.__cedula, 'p_nom' : self.__p_nombre, 's_nom' : self.__s_nombre, 'p_ape' : self.__p_apellido, 's_ape' : self.__s_apellido,'bar' : self.__id_barrio,
    'dis': self.__id_distrito, 'cant': self.__id_canton,'prov': self.__id_provincia,'pais': self.__id_pais,'tel_tra': self.__tel_trabajo,'tel_per': self.__tel_personal,
    'tel_otr': self.__tel_otros, 'cor_tra': self.__cor_trabajo,'cor_per': self.__cor_personal,'cor_otr': self.__cor_otros   }
