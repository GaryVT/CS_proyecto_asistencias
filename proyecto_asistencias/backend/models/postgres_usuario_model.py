from backend.models.postgres_pool_connection import PostgresPool


class UsuarioModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()

    #No hace falta crear usuario ingresando la foto al sistema
    def crear_usuario(self, dni, contrasena, nombre, apellido, tipousuario,fotoSistema):    
        data = {
            'dni' : dni,
            'contrasena' : contrasena,
            'nombre' : nombre,
            'apellido' : apellido,
            'tipousuario': tipousuario,
            'fotoSistema' : fotoSistema
        } 
        
        dni = str(dni)
        contrasena = str(contrasena)
        nombre = str(nombre)
        apellido = str(apellido)
        tipousuario = str(tipousuario)
        fotoSistema = str(fotoSistema)

        query = """insert into usuario (dni, contrasena, nombre, apellido, tipousuario, fotoSistema) 
            values (%(dni)s, %(contrasena)s, %(nombre)s, %(apellido)s, %(tipousuario)s, %(fotoSistema)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        return data

    def actualizar_usuario(self, id_usuario, dni, contrasena, nombre, apellido, tipousuario):     
        data = {
            'id_usuario' : id_usuario,
            'dni' : dni,
            'contrasena' : contrasena,
            'nombre' : nombre,
            'apellido' : apellido,
            'tipousuario' : tipousuario
        }  
        dni = str(dni)
        contrasena = str(contrasena)
        nombre = str(nombre)
        apellido = str(apellido)
        tipousuario = str(tipousuario)

        query = """update usuario set dni = %(dni)s,
                    contrasena= %(contrasena)s, 
                    nombre= %(nombre)s,
                    apellido= %(apellido)s,  
                    tipousuario= %(tipousuario)s
                    where id_usuario = %(id_usuario)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return data

    def eliminar_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        query = """delete from usuario where id_usuario = %(id_usuario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 
    
    def mostrar_usuarios(self):  
        rv = self.mysql_pool.execute("SELECT * from usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'dni': result[1], 'contrasena': result[2], 'nombre': result[3], 'apellido': result[4], 'tipousuario': result[5]}
            data.append(content)
            content = {}
        return data
    
    def obtener_foto(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        rv = self.mysql_pool.execute("select fotoSistema from usuario where id_usuario =%(id_usuario)s", params)   #rv             
        #rv = self.mysql_pool.execute("SELECT * from usuario")  
        data = []
        content ={}
        for result in rv:
            content = {'result': result[0]}
            data.append(content)
            #content = {}
        return content


