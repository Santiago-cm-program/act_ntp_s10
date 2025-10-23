"""
#### **Ejercicio 7: Filtrado por Fechas**
Implementa una función que filtre por fechas usando `.loc`. La función debe:

- Filtrar empleados que ingresaron en 2022
- Filtrar empleados que ingresaron en los últimos 2 años
- Filtrar empleados que ingresaron en el primer trimestre de cualquier año
- Calcular la antigüedad promedio de cada grupo
"""

import pandas as pd
import data as data  # Se asume que el archivo data.py contiene df
from datetime import datetime

def filtro_fechas(df):
    # 📅 Fecha actual
    hoy = pd.Timestamp.today()

    # 🧮 Agregar columna de antigüedad (en años)
    df["antiguedad_anios"] = (hoy - df["fecha_ingreso"]).dt.days / 365

    # 1️⃣ Empleados que ingresaron en 2022
    filtro_2022 = df.loc[df["fecha_ingreso"].dt.year == 2022]
    print("\n--- 📅 Empleados que ingresaron en 2022 ---")
    print(filtro_2022)

    # 2️⃣ Empleados que ingresaron en los últimos 2 años
    dos_anios = hoy - pd.DateOffset(years=2)
    filtro_ultimos2_anios = df.loc[df["fecha_ingreso"] >= dos_anios]
    print("\n--- 📅 Empleados que ingresaron en los últimos 2 años ---")
    print(filtro_ultimos2_anios)

    # 3️⃣ Empleados que ingresaron en el primer trimestre (enero, febrero, marzo)
    filtro_primer_trimestre = df.loc[df["fecha_ingreso"].dt.month.isin([1, 2, 3])]
    print("\n--- 📅 Empleados que ingresaron en el primer trimestre de cualquier año ---")
    print(filtro_primer_trimestre)

    # 4️⃣ Calcular antigüedad promedio por grupo
    resultados = {
        "Antigüedad promedio (2022)": filtro_2022["antiguedad_anios"].mean(),
        "Antigüedad promedio (últimos 2 años)": filtro_ultimos2_anios["antiguedad_anios"].mean(),
        "Antigüedad promedio (1er trimestre)": filtro_primer_trimestre["antiguedad_anios"].mean()
    }

    print("\n--- 📊 Antigüedad Promedio de cada grupo ---")
    for clave, valor in resultados.items():
        print(f"{clave}: {valor:.2f} años")

    return filtro_2022, filtro_ultimos2_anios, filtro_primer_trimestre, resultados


# 🚀 Ejecutar función principal
if __name__ == "__main__":
    filtro_fechas(data.df)
