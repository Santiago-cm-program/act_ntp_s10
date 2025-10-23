""" #### **Ejercicio 13: Selección de Múltiples Filas**
Desarrolla una función que seleccione múltiples filas no consecutivas. La función debe:

- Seleccionar filas usando una lista de posiciones específicas
- Seleccionar filas aleatorias
- Combinar diferentes métodos de selección
- Mostrar estadísticas de las filas seleccionadas
 """
 
import pandas as pd
import data as data
import numpy as np

def seleccion_multiples_filas(df):
    posiciones_especificas = [1, 3, 5, 7, 9]
    # Seleccionar filas usando una lista de posiciones específicas
    filas_especificas = df.iloc[posiciones_especificas]
    print("\n--- 📄 Filas en posiciones específicas (1, 3, 5,7,9")
    print(filas_especificas)
    
    # Seleccionar filas aleatorias
    filas_aleatorias = df.sample(n=5, random_state=42)
    print("\n--- 📄 Filas aleatorias ---")
    print(filas_aleatorias)
    # Combinar diferentes métodos de selección
    combinacion_filas = pd.concat([filas_especificas, filas_aleatorias]).drop_duplicates().reset_index(drop=True)
    print("\n--- 📄 Combinación de filas específicas y aleatorias ---")
    print(combinacion_filas)
    
    # Mostrar estadísticas de las filas seleccionadas
    print("\n--- 📊 Estadísticas de las filas seleccionadas ---")
    print(combinacion_filas.describe())
    
    return filas_especificas, filas_aleatorias, combinacion_filas

if __name__ == "__main__":
    seleccion_multiples_filas(data.df)
    
    
 