""" #### **Ejercicio 14: Selección de Columnas por Posición**
Implementa una función que seleccione columnas usando `.iloc`. La función debe:

- Seleccionar las primeras 3 columnas
- Seleccionar columnas específicas por posición
- Seleccionar la última columna
- Combinar selección de filas y columnas """

import pandas as pd
import data as data

def seleccion_columnas_posicion(df):
    #Seleccionar las primera 3 columnas
    primeras_3_columnas = df.iloc[ :, 0:3]
    
    print("\n--- 📄 Primeras 3 columnas ---")
    print(primeras_3_columnas)
    
    #seleccion de columnas específicas por posición
    columnas_especificas = df.iloc[:, [1, 3, 5]]
    print("\n--- 📄 Columnas específicas (1, 3, 5) ---")
    print(columnas_especificas)
    
    #Seleccionar la ultima columna
    ultima_columna = df.iloc[:, -1]
    print("\n--- 📄 Última columna ---")
    print(ultima_columna)
    
    #Combinar selección de filas y columnas
    combinacion_filas_columnas = df.iloc[0:5, [0, 2, 4]]
    print("\n--- 📄 Combinación de filas (0-4) y columnas (0, 2, 4) ---")
    print(combinacion_filas_columnas)
    
    return primeras_3_columnas, columnas_especificas, ultima_columna, combinacion_filas_columnas

if __name__ == "__main__":
    seleccion_columnas_posicion(data.df)
