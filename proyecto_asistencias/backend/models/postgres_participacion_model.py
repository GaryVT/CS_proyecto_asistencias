from backend.models.postgres_pool_connection import PostgresPool

class ParticipacionModel:
    def __init__(self):        
        self.postgres_connection_pool = PostgresPool()

    def crear_participacion(self, part_fecha, id_curso, id_alumno, cantidad):    
        data = {
            'part_fecha' : part_fecha,
            'id_curso' : id_curso,
            'id_alumno' : id_alumno,
            'cantidad' : cantidad
        }  
        query = """insert into participacion (part_fecha, id_curso, id_alumno, cantidad) 
            values (%(part_fecha)s, %(id_curso)s, %(id_alumno)s, %(cantidad)s)"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        #data['part_id'] = cursor.lastrowid
        return data

    def actualizar_participacion(self, part_id, part_fecha, id_curso, id_alumno, cantidad):   
        data = {
            'part_id' : part_id,
            'part_fecha' : part_fecha,
            'id_curso' : id_curso,
            'id_alumno' : id_alumno,
            'cantidad' : cantidad
        }  
        query = """update participacion set part_fecha = %(part_fecha)s,
                    id_curso= %(id_curso)s, id_alumno= %(id_alumno)s
                    , cantidad= %(cantidad)s  where part_id = %(part_id)s"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_participacion(self, part_id):    
        params = {'part_id' : part_id}      
        query = """delete from participacion where part_id = %(part_id)s"""    
        self.postgres_connection_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_participaciones(self):  
        rv = self.postgres_connection_pool.execute("""select * from participacion""")  
        data = []
        content = {}
        for result in rv:
            content = {'part_id': result[0], 'part_fecha': result[1], 'id_curso': result[2], 'id_alumno': result[3], 'cantidad': result[4]}
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    tm = ParticipacionModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python', 1)) 