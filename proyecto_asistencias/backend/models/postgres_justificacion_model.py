from backend.models.postgres_pool_connection import PostgresPool

class JustificacionModel:
    def __init__(self):        
        self.postgres_connection_pool = PostgresPool()

    def crear_justificacion(self, cod_asist, fecha, descrip):    
        data = {
            'cod_asist' : cod_asist,
            'fecha' : fecha,
            'descrip' : descrip
        }  
        query = """insert into justificacion (cod_asist, fecha, descrip) 
            values (%(cod_asist)s, %(fecha)s, %(descrip)s)"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        #data['cod_justi'] = cursor.lastrowid
        return data

    def actualizar_justificacion(self, cod_justi, cod_asist, fecha, descrip):   
        data = {
            'cod_justi' : cod_justi,
            'cod_asist' : cod_asist,
            'fecha' : fecha,
            'descrip' : descrip
        }  
        query = """update justificacion set cod_asist = %(cod_asist)s,
                    fecha= %(fecha)s, descrip= %(descrip)s
                    where cod_justi = %(cod_justi)s"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_justificacion(self, cod_justi):    
        params = {'cod_justi' : cod_justi}      
        query = """delete from justificacion where cod_justi = %(cod_justi)s"""    
        self.postgres_connection_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_justificaciones(self):  
        rv = self.postgres_connection_pool.execute("""select * from justificacion""")  
        data = []
        content = {}
        for result in rv:
            content = {'cod_justi': result[0], 'cod_asist': result[1], 'fecha': result[2], 'descrip': result[3]}
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    tm = JustificacionModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python', 1)) 