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

def findOrInsert(table, name):
    cur.execute("select id from "+table+" where name=%s limit 1", [name])
    r = cur.fetchone()
    if r:
        return r[0]
    else:
        cur.execute("insert into "+table+" (name) values (%s) returning id", [name])
        return cur.fetchone()[0]

# Conexión a la base
conn = psycopg2.connect(
    host="cc3201.dcc.uchile.cl",
    user="cc3201",
    database="cc3201",
    password="opilar miasma",
    port="5525"
)

cur = conn.cursor()

# Lectura del CSV
with open("data/reviews.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i += 1
        if i == 1:
            continue
        if i == 10000:
            break

        # -------------
        # Entidad Review
        # -------------
        id_review = int(row[0].strip().strip('"').strip("'"))
        puntuacion = float(row[4].strip().strip('"').strip("'"))

        # --------------
        # Tabla Reviews
        # --------------
        cur.execute("SELECT id_review FROM Reviews WHERE id_review=%s LIMIT 1", [id_review])
        r = cur.fetchone()
        if r:
            pass
        else:
            cur.execute(
                "INSERT INTO Reviews (id_review, puntuacion) VALUES (%s, %s)",
                [id_review, puntuacion]
            )
        print("procesado:", i)

conn.commit()
conn.close()
