""" 
#### **Ejercicio 15: Modificación de Datos con .iloc**
Crea una función que modifique datos usando `.iloc`. La función debe:

- Modificar valores en posiciones específicas
- Modificar un rango de celdas
- Modificar múltiples columnas a la vez
- Mostrar los cambios realizados 
"""

import pandas as pd
import data as data

def modificar_datos_iloc(df):
    # --- 🔢 Modificar valores en posiciones específicas ---
    salario_original = df.iloc[0, 2]
    df.iloc[0, 2] = 99999
    print(f"\n--- 🔄 Modificación de valor en posición (0,2) ---")
    print(f"Salario original: {salario_original} -> Salario modificado: {df.iloc[0, 2]}")

    # --- 🔁 Modificar un rango de celdas ---
    edades_originales = df.iloc[1:6, 1].tolist()
    df.iloc[1:6, 1] = [30, 31, 32, 33, 34]
    print(f"\n--- 🔄 Modificación de rango de celdas en filas ---")
    print(f"Edades originales: {edades_originales} -> Edades modificadas: {df.iloc[1:6, 1].tolist()}")

    # --- 🧩 Modificar múltiples columnas a la vez ---
    # Localizamos los índices exactos de las columnas 'departamento' y 'ciudad'
    idx_dep = df.columns.get_loc("departamento")
    idx_city = df.columns.get_loc("ciudad")

    departamentos_originales = df.iloc[0:3, [idx_dep, idx_city]].values.tolist()

    # Cambiamos usando los índices correctos (ambos son columnas de texto)
    df.iloc[0:3, [idx_dep, idx_city]] = [
        ['Recursos Humanos', 'Bogotá'],
        ['Finanzas', 'Bogotá'],
        ['Operaciones', 'Bogotá']
    ]

    print(f"\n--- 🔄 Modificación de múltiples columnas (departamento y ciudad) ---")
    print(f"Departamentos y ciudades originales: {departamentos_originales} -> Modificados: {df.iloc[0:3, [idx_dep, idx_city]].values.tolist()}")

    return df


if __name__ == "__main__":
    df_modificado = modificar_datos_iloc(data.df)
