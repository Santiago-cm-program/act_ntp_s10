""" #### **Ejercicio 5: Modificación de Datos con .loc**
Crea una función que modifique datos usando `.loc`. La función debe:

- Aumentar el salario en 10% a empleados de IT
- Cambiar el estado a inactivo para empleados mayores de 60 años
- Actualizar la ciudad a 'Bogotá' para empleados de RRHH
- Mostrar los cambios realizados antes y después
"""

import pandas as pd
import data as data

def modificacion_datos(df):
    # ===== 1️⃣ AUMENTO DE SALARIO EN IT =====
    print("\n--- 💻 Empleados de IT (antes del aumento) ---")
    print(df.loc[df["departamento"] == "IT", ["nombre", "departamento", "salario"]].head(10))

    df.loc[df["departamento"] == "IT", "salario"] *= 1.10

    print("\n--- 💰 Empleados de IT (después del aumento del 10%) ---")
    print(df.loc[df["departamento"] == "IT", ["nombre", "departamento", "salario"]].head(10))


    # ===== 2️⃣ CAMBIAR ESTADO A INACTIVO SI EDAD > 60 =====
    print("\n--- 👴 Empleados mayores de 60 años (antes) ---")
    print(df.loc[df["edad"] > 60, ["nombre", "edad", "activo"]].head(10))

    df.loc[df["edad"] > 60, "activo"] = False

    print("\n--- ❌ Empleados mayores de 60 años (después del cambio de estado) ---")
    print(df.loc[df["edad"] > 60, ["nombre", "edad", "activo"]].head(10))


    # ===== 3️⃣ ACTUALIZAR CIUDAD A 'Bogotá' EN RRHH =====
    print("\n--- 🏙️ Empleados de RRHH (antes del cambio de ciudad) ---")
    print(df.loc[df["departamento"] == "RRHH", ["nombre", "departamento", "ciudad"]].head(10))

    df.loc[df["departamento"] == "RRHH", "ciudad"] = "Bogotá"

    print("\n--- 🏢 Empleados de RRHH (después del cambio de ciudad) ---")
    print(df.loc[df["departamento"] == "RRHH", ["nombre", "departamento", "ciudad"]].head(10))

    return df


# Ejecutar la función
if __name__ == "__main__":
    ejercicio_05 = modificacion_datos(data.df)
    print("\n✅ Modificaciones aplicadas correctamente.")
