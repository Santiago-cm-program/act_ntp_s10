""" #### **Ejercicio 17: Selección Avanzada con .iloc**
Implementa una función que realice selecciones complejas. La función debe:

- Seleccionar subconjuntos específicos del DataFrame
- Usar arrays booleanos con `.iloc`
- Combinar `.iloc` con funciones de agregación
- Crear vistas personalizadas del DataFrame
"""

import pandas as pd
import data as data
import numpy as np

def seleccion_avanzada(df):
    # Seleccionar subconjuntos específicos del DataFrame
    subconjunto = df.iloc[10:21, [0, 2, 4]]
    print("\n--- 📄 Subconjunto específico (filas 10-20, columnas 0, 2, 4) ---")
    print(subconjunto)
    
    # Usar arrays booleanos con .iloc
    boolean_array = np.array([True if i % 3 == 0 else False for i in range(len(df))])
    seleccion_booleana = df.iloc[boolean_array]
    print("\n--- 📄 Selección con array booleano (cada tercera fila) ---")
    print(seleccion_booleana)
    
    # Combinar .iloc con funciones de agregación
    promedio_salario = df.iloc[:, 3].mean()
    print("\n--- 📄 Promedio de salario ---")
    print(promedio_salario)
    
    # Crear vistas personalizadas del DataFrame
    vista_personalizada = df.iloc[:, [1, 3]][df['activo'] == True]
    print("\n--- 📄 Vista personalizada (nombre y salario de empleados activos) ---")
    print(vista_personalizada)
    
    return subconjunto, seleccion_booleana, promedio_salario, vista_personalizada
if __name__ == "__main__":
    seleccion_avanzada(data.df)