""" #### **Ejercicio 2: Filtrado con Condiciones Simples**
Crea una función que filtre empleados usando condiciones con `.loc`. La función debe:

- Filtrar empleados mayores de 40 años
- Filtrar empleados del departamento 'IT'
- Filtrar empleados con salario mayor a 80000
- Mostrar el número de registros encontrados en cada filtro """

import pandas as pd
import data as data

def filtro(df):
    # Empleados mayores de 40
    mayores_40 = df.loc[df['edad'] > 40]
    print(f"\n--- Empleados mayores de 40 años ---")
    print(mayores_40)
    print(f"Registros encontrados: {len(mayores_40)}\n")
    
    # Empleados del departamento de IT
    empleados_IT = df.loc[df['departamento'] == 'IT']
    print(f"--- Empleados del departamento IT ---")
    print(empleados_IT)
    print(f"Registros encontrados: {len(empleados_IT)}\n")
    
    # Empleados con salarios mayores a 80000
    salario = df.loc[df['salario'] > 80000]
    print(f"--- Empleados con salario mayor a 80000 ---")
    print(salario)
    print(f"Cantidad de registros encontrados: {len(salario)}\n")
    
    return mayores_40, empleados_IT, salario


# Llamar la función usando el DataFrame definido en data.py
Informacion_filtro = filtro(data.df)
print("✅ Filtros aplicados correctamente.")