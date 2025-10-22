"""#### **Ejercicio 1: Selección Básica con .loc**
Implementa una función que use `.loc` para seleccionar datos específicos del DataFrame. La función debe:

- Seleccionar un empleado específico por su ID
- Seleccionar múltiples empleados usando una lista de IDs
- Seleccionar un rango de empleados
- Mostrar todos los resultados con formato claro
"""

import pandas as pd
import data as data  # Asegúrate de tener el archivo data.py en la misma carpeta

def seleccion_basica(df):
    print("=== 🔹 SELECCIÓN BÁSICA CON .loc ===")

    # 1️⃣ Seleccionar un empleado específico por su ID
    empleado_id = 10
    empleado = df.loc[df['empleado_id'] == empleado_id]
    print(f"\nEmpleado con ID {empleado_id}:")
    print(empleado)

    # 2️⃣ Seleccionar múltiples empleados usando una lista de IDs
    lista_ids = [3, 7, 15, 22]
    empleados_lista = df.loc[df['empleado_id'].isin(lista_ids)]
    print(f"\nEmpleados con IDs {lista_ids}:")
    print(empleados_lista)

    # 3️⃣ Seleccionar un rango de empleados (por ejemplo, del ID 20 al 30)
    rango_ids = df.loc[(df['empleado_id'] >= 20) & (df['empleado_id'] <= 30)]
    print("\nEmpleados con ID entre 20 y 30:")
    print(rango_ids)

    print("\n✅ Selección completada con éxito.")
    return empleado, empleados_lista, rango_ids


# Ejecución del ejercicio (solo si se ejecuta directamente)
if __name__ == "__main__":
    seleccion_basica(data.df)
