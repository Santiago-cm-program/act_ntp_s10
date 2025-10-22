""" #### **Ejercicio 6: Filtrado con Funciones de String**
Desarrolla una función que use métodos de string con `.loc`. La función debe:

- Filtrar empleados cuyo nombre contenga el dígito '1'
- Filtrar empleados cuyo apellido termine en '5'
- Filtrar empleados de ciudades que empiecen con 'B'
- Mostrar estadísticas de cada grupo encontrado """

import pandas as pd
import data as data


def filtros_string(df):
    # filtro 1: Nombres que contienen '1'
    filtro_nombre = df.loc[df["nombre"].str.contains("1", na=False)]

    # Filtro de apellido que terminan en '5'
    filtro_apellido = df.loc[df["apellido"].str.endswith("5", na=False)]

    # Filtro de ciudad que empiecen con B
    filtro_ciudades = df.loc[df["ciudad"].str.startswith("B", na=False)]

    print(f"Empleados cuyo nombre contiene '1':\n{filtro_nombre}\n")

    print(f"Empleados cuyo apellido termina en '5':\n{filtro_apellido}\n")

    print(f"Empleados de ciudades que empiezan con 'B':\n{filtro_ciudades}\n")


filtros_string(data.df)
