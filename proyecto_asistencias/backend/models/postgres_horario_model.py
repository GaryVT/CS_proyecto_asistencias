from backend.models.postgres_pool_connection import PostgresPool
import json
class HorarioModel:
    def __init__(self):        
        self.postgres_connection_pool = PostgresPool()

    def crear_horario(self, id_curso, hora_inicio, hora_fin, dia, aula):    
        data = {
            'id_curso' : id_curso,
            'hora_inicio' : hora_inicio,
            'hora_fin' : hora_fin,
            'dia' : dia,
            'aula' : aula
        }  
        query = """insert into horario (id_curso, hora_inicio, hora_fin, dia, aula) 
            values (%(id_curso)s, %(hora_inicio)s, %(hora_fin)s, %(dia)s, %(aula)s)"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        #data['id_horario'] = cursor.lastrowid
        return data

    def actualizar_horario(self, id_horario, id_curso, hora_inicio, hora_fin, dia, aula):   
        data = {
            'id_horario' : id_horario,
            'id_curso' : id_curso,
            'hora_inicio' : hora_inicio,
            'hora_fin' : hora_fin,
            'dia' : dia,
            'aula' : aula
        }  
        query = """update horario set id_curso = %(id_curso)s,
                    hora_inicio= %(hora_inicio)s, hora_fin= %(hora_fin)s
                    , dia= %(dia)s, aula= %(aula)s  where id_horario = %(id_horario)s"""    
        cursor = self.postgres_connection_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result
    
    def eliminar_horario(self, id_horario):    
        params = {'id_horario' : id_horario}      
        query = """delete from horario where id_horario = %(id_horario)s"""    
        self.postgres_connection_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def mostrar_horarios(self):  
        rv = self.postgres_connection_pool.execute("""select * from horario""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_horario': result[0], 'id_curso': result[1], 'hora_inicio': result[2].strftime("%H:%M:%S"), 'hora_fin': result[3].strftime("%H:%M:%S"), 'dia': result[4], 'aula': result[5]}
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    tm = HorarioModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python', 1)) 