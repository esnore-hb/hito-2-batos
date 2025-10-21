import psycopg2
import psycopg2.extras
import csv
import re

"""
Integrantes:
- Beatriz Toledo
- Hector Bonilla
- Lazaro Narvaez
"""


# Modifique este metodo para adaptarlo a su lógica.
def findOrInsert(table, name):
    cur.execute("select id from "+table+" where name=%s limit 1", [name])
    r = cur.fetchone()
    if(r): return r[0]
    else:
        cur.execute("insert into "+table+" (name) values (%s) returning id", [name])
        return cur.fetchone()[0]

# Establecer conexion con la base de datos
conn = psycopg2.connect(host="cc3201.dcc.uchile.cl", user="cc3201", database="cc3201", password="j'<3_cc3201", port="5440")

cur = conn.cursor()

# Implementación de la lógica de lectura de un archivo csv.
with open('<path_to_file>') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            continue
        
        
        # Your logic here

conn.commit()
conn.close()
