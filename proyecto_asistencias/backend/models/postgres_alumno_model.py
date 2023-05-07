from backend.models.postgres_pool_connection import PostgresPool

class AlumnoModel:
    def __init__(self):        
        self.postgres_connection_pool = PostgresPool()

    def crear_alumno(self, id_usuario, tipousr_id, anio_alumno, carrera):    
        data = {
            'id_usuario' : id_usuario,
            'tipousr_id' : tipousr_id,
            'anio_alumno' : anio_alumno,
            'carrera' : carrera
        }  
        query = """insert into alumno (id_usuario, tipousr_id, anio_alumno, carrera) 
            values (%(id_usuario)s, %(tipousr_id)s, %(anio_alumno)s, %(carrera)s)"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        #data['id_alumno'] = cursor.lastrowid
        return data

    def actualizar_alumno(self, id_alumno, id_usuario, tipousr_id, anio_alumno, carrera):   
        data = {
            'id_alumno' : id_alumno,
            'id_usuario' : id_usuario,
            'tipousr_id' : tipousr_id,
            'anio_alumno' : anio_alumno,
            'carrera' : carrera
        }  
        query = """update alumno set id_usuario = %(id_usuario)s,
                    tipousr_id= %(tipousr_id)s, anio_alumno= %(anio_alumno)s
                    , carrera= %(carrera)s  where id_alumno = %(id_alumno)s"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_alumno(self, id_alumno):    
        params = {'id_alumno' : id_alumno}      
        query = """delete from alumno where id_alumno = %(id_alumno)s"""    
        self.postgres_connection_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_alumnos(self):  
        rv = self.postgres_connection_pool.execute("""select a.id_alumno, u.nombre, u.apellido, a.anio_alumno, a.carrera, u.tipousuario  from alumno a 
inner join usuario u on u.id_usuario = a.id_usuario """)  
        data = []
        content = {}
        for result in rv:
            content = {'id_alumno': result[0], 'nombre': result[1], 'apellido': result[2], 'anio_alumno': result[3], 'carrera': result[4], 'tipousuario': result[5]}
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    tm = AlumnoModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python', 1)) 