from backend.models.postgres_pool_connection import PostgresPool

class docenteModel:
    def __init__(self):        
        self.postgres_connection_pool = PostgresPool()

    def crear_docente(self, id_usuario, tipousr_id, tipo_docente):    
        data = {
            'id_usuario' : id_usuario,
            'tipousr_id' : tipousr_id,
            'tipo_docente' : tipo_docente
        }  
        query = """insert into docente (id_usuario, tipousr_id, tipo_docente) 
            values (%(id_usuario)s, %(tipousr_id)s, %(tipo_docente)s)"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        #data['id_docente'] = cursor.lastrowid
        return data

    def actualizar_docente(self, id_docente, id_usuario, tipousr_id, tipo_docente):   
        data = {
            'id_docente' : id_docente,
            'id_usuario' : id_usuario,
            'tipousr_id' : tipousr_id,
            'tipo_docente' : tipo_docente
        }  
        query = """update docente set id_usuario = %(id_usuario)s,
                    tipousr_id= %(tipousr_id)s, tipo_docente= %(tipo_docente)s where id_docente = %(id_docente)s"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_docente(self, id_docente):    
        params = {'id_docente' : id_docente}      
        query = """delete from docente where id_docente = %(id_docente)s"""    
        self.postgres_connection_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_docentes(self):  
        rv = self.postgres_connection_pool.execute("""select * from docente""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_docente': result[0],'id_usuario': result[1],'tipousr_id': result[2],'tipo_docente': result[3]}
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    tm = docenteModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python', 1)) 