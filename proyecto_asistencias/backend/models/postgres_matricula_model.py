from backend.models.postgres_pool_connection import PostgresPool

class MatriculaModel:
    def __init__(self):        
        self.postgres_connection_pool = PostgresPool()

    def crear_matricula(self, id_alumno, id_curso, fecha_matricula, estado_matricula):    
        data = {
            'id_alumno' : id_alumno,
            'id_curso' : id_curso,
            'fecha_matricula' : fecha_matricula,
            'estado_matricula' : estado_matricula
        }  
        query = """insert into matricula (id_alumno, id_curso, fecha_matricula, estado_matricula) 
            values (%(id_alumno)s, %(id_curso)s, %(fecha_matricula)s, %(estado_matricula)s)"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        #data['matricula_id'] = cursor.lastrowid
        return data

    def actualizar_matricula(self, matricula_id, id_alumno, id_curso, fecha_matricula, estado_matricula):   
        data = {
            'matricula_id' : matricula_id,
            'id_alumno' : id_alumno,
            'id_curso' : id_curso,
            'fecha_matricula' : fecha_matricula,
            'estado_matricula' : estado_matricula
        }  
        query = """update matricula set id_alumno = %(id_alumno)s,
                    id_curso= %(id_curso)s, fecha_matricula= %(fecha_matricula)s
                    , estado_matricula= %(estado_matricula)s  where matricula_id = %(matricula_id)s"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_matricula(self, matricula_id):    
        params = {'matricula_id' : matricula_id}      
        query = """delete from matricula where matricula_id = %(matricula_id)s"""    
        self.postgres_connection_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_matriculas(self):  
        rv = self.postgres_connection_pool.execute("""select * from matricula""")  
        data = []
        content = {}
        for result in rv:
            content = {'matricula_id': result[0], 'id_alumno': result[1], 'id_curso': result[2], 'fecha_matricula': result[3], 'estado_matricula': result[4]}
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    tm = MatriculaModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python', 1)) 