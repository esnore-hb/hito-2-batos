import psycopg2
import csv
import re

"""
Integrantes:
- Beatriz Toledo
- Hector Bonilla
- Lazaro Narvaez
"""

# Establecer conexion con la base de datos
conn = psycopg2.connect(host="cc3201.dcc.uchile.cl", user="cc3201", database="cc3201", password="opilar miasma", port="5525")

cur = conn.cursor()

# ----------------------------
# Reiniciar las tablas
# ----------------------------
#cur.execute("TRUNCATE tindanime * RESTART IDENTITY CASCADE")

with open("data/reviews.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            continue
        
        # -------------
        # Entidad Review
        # -------------
        id_review = int(row[0].strip().strip('\'').strip('"'))

        nombre_perfil = row[1].strip().strip('\'').strip('"')
        
        # --------------
        # Tabla Review
        # --------------
        cur.execute("SELECT id_review, nombre_perfil FROM Escribe WHERE id_review=%s AND nombre_perfil=%s limit 1", [id_review, nombre_perfil])
        r = cur.fetchone()
        if(r): pass
        else:
            cur.execute("INSERT INTO Escribe \
                (id_review, nombre_perfil) \
                VALUES (%s, %s)",
                [id_review, nombre_perfil])

        print("procesado:", i)
        

conn.commit()
conn.close()
