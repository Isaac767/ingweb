#Archivo para coneccion a mysql
import pymysql # type: ignore

conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='UTPL2023',
    database='universidad',
    port=3306
)

def insert_carrera():
    cursor=conn.cursor()
    cursor.execute("INSERT INTO carrera(codigo, nombre,modalidad_id) values('COMP_01','COMPUTACIÓN',1)")
    conn.commit()
    
def consultar_carreras():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera')
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila[0] , ' - ' ,fila[1],' - ', fila[2])

insert_carrera()
consultar_carreras()


conn.close()  