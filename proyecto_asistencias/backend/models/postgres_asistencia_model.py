from backend.models.postgres_pool_connection import PostgresPool

class AsistenciaModel:
    def __init__(self):        
        self.postgres_connection_pool = PostgresPool()

    def crear_asistencia(self, fecha, id_curso, id_alumno, presente):    
        data = {
            'fecha' : fecha,
            'id_curso' : id_curso,
            'id_alumno' : id_alumno,
            'presente' : presente
        }  
        query = """insert into asistencia (fecha, id_curso, id_alumno, presente) 
            values (%(fecha)s, %(id_curso)s, %(id_alumno)s, %(presente)s)"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        #data['cod_asist'] = cursor.lastrowid
        return data

    def actualizar_asistencia(self, cod_asist, fecha, id_curso, id_alumno, presente):   
        data = {
            'cod_asist' : cod_asist,
            'fecha' : fecha,
            'id_curso' : id_curso,
            'id_alumno' : id_alumno,
            'presente' : presente
        }  
        query = """update asistencia set fecha = %(fecha)s,
                    id_curso= %(id_curso)s, id_alumno= %(id_alumno)s
                    , presente= %(presente)s  where cod_asist = %(cod_asist)s"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_asistencia(self, cod_asist):    
        params = {'cod_asist' : cod_asist}      
        query = """delete from asistencia where cod_asist = %(cod_asist)s"""    
        self.postgres_connection_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_asistencias(self):  
        rv = self.postgres_connection_pool.execute("""select * from asistencia""")  
        data = []
        content = {}
        for result in rv:
            content = {'cod_asist': result[0], 'fecha': result[1], 'id_curso': result[2], 'id_alumno': result[3], 'presente': result[4]}
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    tm = AsistenciaModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python', 1)) 