from backend.models.postgres_pool_connection import PostgresPool

class CursoModel:
    def __init__(self):        
        self.postgres_connection_pool = PostgresPool()



    def crear_curso(self, id_docente, nombre_curso, descripcion):    
        id_docente = str(id_docente)
        nombre_curso = str(nombre_curso)
        descripcion = str(descripcion)
        data = {
            'id_docente' : id_docente,
            'nombre_curso' : nombre_curso,
            'descripcion':descripcion
        }  



        query = """insert into curso (id_docente, nombre_curso), descripcion 
            values (%(id_docente)s, %(nombre_curso)s, %(descripcion)s)"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        #data['id_alumno'] = cursor.lastrowid
        return data

    def actualizar_curso(self, id_curso, id_docente, nombre_curso, descripcion):   
        data = {
            'id_curso' : id_curso,
            'id_docente' : id_docente,
            'nombre_curso' : nombre_curso,
            'descripcion' : descripcion
        }  
        query = """update curso set id_curso = %(id_curso)s, id_docente = %(id_docente)s,
                    nombre_curso= %(nombre_curso)s, descripcion= %(descripcion)s  where id_curso = %(id_curso)s"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_curso(self, id_curso):    
        params = {'id_curso' : id_curso}      
        query = """delete from curso where id_curso = %(id_curso)s"""    
        self.postgres_connection_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_cursos(self):  
        rv = self.postgres_connection_pool.execute("""select * from curso c""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_curso': result[0], 'id_docente': result[1], 'nombre_curso': result[2], 'descripcion': result[3]}
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    tm = CursoModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python', 1)) 