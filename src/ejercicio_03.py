""" #### **Ejercicio 3: Filtrado con Múltiples Condiciones**
Desarrolla una función que combine múltiples condiciones con `.loc`. La función debe:

- Filtrar empleados de IT con salario mayor a 70000
- Filtrar empleados de Ventas o Marketing
- Filtrar empleados activos con más de 5 años de experiencia
- Mostrar estadísticas básicas de cada grupo filtrado
"""

import pandas as pd
import data as data

def filtros_multiples(df):
    # 1️⃣ Empleados de IT con salario mayor a 70000
    filtro_01 = df.loc[(df['departamento'] == 'IT') & (df['salario'] > 70000)]
    print("\n--- 💻 Empleados de IT con salario > 70000 ---")
    print(filtro_01)
    print(f"Cantidad de registros: {len(filtro_01)}")
    print("\nEstadísticas básicas:")
    print(filtro_01[['salario', 'edad', 'experiencia_años']].describe())

    # 2️⃣ Empleados del departamento Ventas o Marketing
    filtro_02 = df.loc[(df['departamento'] == 'Ventas') | (df['departamento'] == 'Marketing')]
    print("\n--- 🧾 Empleados del departamento Ventas o Marketing ---")
    print(filtro_02)
    print(f"Cantidad de registros: {len(filtro_02)}")
    print("\nEstadísticas básicas:")
    print(filtro_02[['salario', 'edad', 'experiencia_años']].describe())

    # 3️⃣ Empleados activos con más de 5 años de experiencia
    filtro_03 = df.loc[(df['activo'] == True) & (df['experiencia_años'] > 5)]
    print("\n--- 🧑‍💼 Empleados activos con más de 5 años de experiencia ---")
    print(filtro_03)
    print(f"Cantidad de registros: {len(filtro_03)}")
    print("\nEstadísticas básicas:")
    print(filtro_03[['salario', 'edad', 'experiencia_años']].describe())

    return filtro_01, filtro_02, filtro_03


# Ejecutar la función
if __name__ == "__main__":
    ejercicio_03 = filtros_multiples(data.df)
    print("\n✅ Filtros múltiples aplicados correctamente.")
