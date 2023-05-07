#de curso
from backend.models.postgres_pool_connection import PostgresPool


class tipo_usuario_model:
    def __init__(self):        
        self.mysql_pool = PostgresPool()



    def crear_tipo_usuario(self, nombre_tusr):    
        data = {
            'nombre_tusr' : nombre_tusr
        }  
        query = """insert into tipo_usuario (nombre_tusr) 
            values (%(nombre_tusr)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        #data['tipousr_id'] = cursor.lastrowid
        return data

    def actualizar_tipo_usuario(self, tipousr_id, nombre_tusr):   
        data = {
            'tipousr_id' : tipousr_id,
            'nombre_tusr' : nombre_tusr
        }
        tipousr_id = str(tipousr_id)
        nombre_tusr = str(nombre_tusr)


        query = """update tipo_usuario set nombre_tusr= %(nombre_tusr)s  where tipousr_id = %(tipousr_id)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_tipo_usuario(self, tipousr_id):    
        params = {'tipousr_id' : tipousr_id}      
        query = """delete from tipo_usuario where tipousr_id = %(tipousr_id)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_tipo_usuarios(self):  
        rv = self.mysql_pool.execute("""select * from tipo_usuario""")  
        data = []
        content = {}
        for result in rv:
            content = {'tipousr_id': result[0],'nombre_tusr': result[1]}
            data.append(content)
            content = {}
        return data

