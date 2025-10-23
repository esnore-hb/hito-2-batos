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
conn = psycopg2.connect(host="cc3201.dcc.uchile.cl", user="cc3201", database="cc3201", password="opilar miasma", port="5525")

cur = conn.cursor()

# Implementación de la lógica de lectura de un archivo csv.
with open("data/animes.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            continue
        
        # uid 0 ,title 1,synopsis 2,genre 3,aired 4,episodes 5,members 6,popularity 7,ranked 8,score 9,img_url 10,link 11
        
        anime_id = int(row[0].strip().strip('"').strip('\''))

        titulo = row[1].strip().strip('"').strip('\'')

        sinopsis = row[2].strip().strip('"').strip('\'')

        intervalo_emision = row[4].strip().strip('"').split("to")
        for i in range(len(intervalo_emision)):
            intervalo_emision[i] = intervalo_emision[i].strip()

        inicio_emision = intervalo_emision[1]
        termino_emision = "hoy"
        if len(intervalo_emision > 1): termino_emision = intervalo_emision[1]

        episodios = int(float(row[5].strip().strip('"')))

        miembros = int(row[6].strip().strip('"'))

        popularidad = int(row[7].strip().strip('"'))

        ranking = int(row[8].strip().strip('"'))
        
        puntuacion_anime = int(row[8].strip().strip('"'))

conn.commit()
conn.close()
