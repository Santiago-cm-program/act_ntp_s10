"""
#### **Ejercicio 9: Combinación de Filtros Complejos**
Desarrolla una función que combine múltiples tipos de filtros. La función debe:

- Filtrar empleados activos, de IT o Finanzas, con salario > 60000 y edad < 45
- Usar operadores lógicos complejos con paréntesis
- Filtrar empleados de ciudades específicas con experiencia > 10 años
- Crear un resumen estadístico de los grupos filtrados
"""

import pandas as pd
import data as data  # Se asume que el archivo data.py contiene df


def filtros_complejos(df):
    # 🔹 Filtro 1: empleados activos, IT o Finanzas, salario > 60000 y edad < 45
    filtro_1 = df.loc[
        (df["activo"] == True)
        & ((df["departamento"] == "IT") | (df["departamento"] == "Finanzas"))
        & (df["salario"] > 60000)
        & (df["edad"] < 45)
    ]
    print("\n--- 🧑‍💼 Empleados activos de IT o Finanzas con salario > 60000 y edad < 45 ---")
    print(filtro_1[["empleado_id", "nombre", "departamento", "edad", "salario", "activo"]])

    # 🔹 Filtro 2: empleados de ciudades específicas con experiencia > 10 años
    ciudades_especificas = ["Cali", "Bogotá", "Medellín"]
    filtro_2 = df.loc[
        (df["ciudad"].isin(ciudades_especificas)) & (df["experiencia_años"] > 10)
    ]
    print("\n--- 🌆 Empleados de ciudades específicas con experiencia > 10 años ---")
    print(filtro_2[["empleado_id", "nombre", "ciudad", "experiencia_años", "salario"]])

    # 🔹 Resumen estadístico de los grupos filtrados
    resumen = {
        "Total empleados (filtro 1)": len(filtro_1),
        "Salario promedio (filtro 1)": round(filtro_1["salario"].mean(), 2)
        if not filtro_1.empty
        else 0,
        "Edad promedio (filtro 1)": round(filtro_1["edad"].mean(), 1)
        if not filtro_1.empty
        else 0,
        "Total empleados (filtro 2)": len(filtro_2),
        "Experiencia promedio (filtro 2)": round(filtro_2["experiencia_años"].mean(), 1)
        if not filtro_2.empty
        else 0,
        "Salario promedio (filtro 2)": round(filtro_2["salario"].mean(), 2)
        if not filtro_2.empty
        else 0,
    }

    print("\n--- 📊 Resumen estadístico ---")
    for k, v in resumen.items():
        print(f"{k}: {v}")

    return filtro_1, filtro_2, resumen


# 🚀 Ejecutar función principal
if __name__ == "__main__":
    filtros_complejos(data.df)
