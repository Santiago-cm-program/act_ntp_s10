""" #### **Ejercicio 11: Selección Básica con .iloc**
Implementa una función que use `.iloc` para seleccionar datos por posición. La función debe:

- Seleccionar la primera fila
- Seleccionar las primeras 5 filas
- Seleccionar la última fila
- Seleccionar filas específicas por posición """

import pandas as pd 
import data as data
def seleccion_posicion(df):
    #Seleccionar la primera fila
    primera_fila= df.iloc[0]
    print("\n--- 📄 Primera fila ---")
    print(primera_fila)
    
    #Seleccionar las primeras 5 filas
    primeras_cinco_filas= df.iloc[0:5]
    print("\n--- 📄 Primeras 5 filas ---")
    print(primeras_cinco_filas)
    
    #Seleccionar la ultima fila
    ultima_fila= df.iloc[-1]
    print("\n--- 📄 Última fila ---")
    print(ultima_fila)
    
    #Seleccionar filas específicas por posición
    filas_especificas  = df.iloc[[2,5,10]]
    print("\n--- 📄 Filas específicas (2, 5, 10) ---")
    print(filas_especificas)
    
    return primera_fila, primeras_cinco_filas, ultima_fila, filas_especificas
if __name__ == "__main__":
    seleccion_posicion(data.df)