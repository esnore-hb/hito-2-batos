import psycopg2
import csv

conn = psycopg2.connect(
    host="cc3201.dcc.uchile.cl",
    user="cc3201",
    database="cc3201",
    password="opilar miasma",
    port="5525"
)
cur = conn.cursor()

with open("data/reviews.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    i = 0
    for row in reader:
        i += 1
        if i == 1:
            continue
        if i == 10000:  # para pruebas
            break

        id_review = int(row[0].strip().strip('"').strip("'"))
        nombre = row[1].strip().strip('"').strip("'")

        # ---- limpiar y dividir los scores ----
        scores_str = row[5].strip().strip("{}")
        pares = scores_str.split(",")

        valores = []
        for par in pares:
            if ":" in par:
                _, val = par.split(":", 1)
                val = val.strip().strip("'").strip('"')
                if val.isdigit():  # asegurar que es número
                    valores.append(int(val))

        # Calcular promedio
        if valores:
            promedio = round(sum(valores) / len(valores), 2)
        else:
            promedio = 0

        # -------------- insertar promedio -----------------
        cur.execute("SELECT nombre FROM calificacion WHERE nombre=%s LIMIT 1", [nombre])
        r = cur.fetchone()
        if not r:
            print(f"{i}: nombre={nombre}, promedio={promedio}, id_review={id_review}")
            cur.execute(
                "INSERT INTO calificacion (nombre, valor, id_review) VALUES (%s, %s, %s)",
                [nombre, promedio, id_review]
            )

conn.commit()
conn.close()
