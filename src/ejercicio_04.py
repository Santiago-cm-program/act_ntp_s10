""" Implementa una función que seleccione columnas específicas con `.loc`. La función debe:

- Seleccionar solo nombre y salario de todos los empleados
- Seleccionar un rango de columnas desde nombre hasta departamento
- Combinar filtro de filas y columnas para empleados mayores de 50 años
- Mostrar las primeras 10 filas de cada selección
"""

import pandas as pd
import data as data

def seleccion_columnas(df):
    # 1️⃣ Seleccionar solo nombre y salario
    filtro_01 = df.loc[:, ['nombre', 'salario']]
    print("\n--- 🧾 Nombre y salario ---")
    print(filtro_01.head(10))

    # 2️⃣ Seleccionar un rango de columnas desde nombre hasta departamento
    filtro_02 = df.loc[:, 'nombre':'departamento']
    print("\n--- 🧩 Rango de columnas desde 'nombre' hasta 'departamento' ---")
    print(filtro_02.head(10))

    # 3️⃣ Filtrar empleados mayores de 50 años y mostrar columnas específicas
    filtro_03 = df.loc[df['edad'] > 50, ['nombre', 'edad', 'salario', 'departamento']]
    print("\n--- 👴 Empleados mayores de 50 años (nombre, edad, salario, departamento) ---")
    print(filtro_03.head(10))

    return filtro_01, filtro_02, filtro_03


# Ejecutar la función
if __name__ == "__main__":
    ejercicio_04 = seleccion_columnas(data.df)
    print("\n✅ Selección de columnas completada correctamente.")
