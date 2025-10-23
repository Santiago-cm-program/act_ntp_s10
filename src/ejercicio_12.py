""" #### **Ejercicio 12: Selección con Rangos**
Crea una función que use rangos con `.iloc`. La función debe:

- Seleccionar filas del 10 al 20
- Seleccionar las últimas 10 filas
- Seleccionar filas pares
- Seleccionar cada tercera fila """

import pandas as pd
import data as data

def filtro_seleccion_rangos (df):
    #Seleccionar filas del 10 al 20
    filtro_10_20= df.iloc[10:21]
    print("\n--- 📄 Filas del 10 al 20 ---")
    print(filtro_10_20)
    
    #Seleccionar las ultimas 10 filas
    ultimas_10_filas = df.iloc[-10]
    print("\n--- 📄 Últimas 10 filas ---")
    print(ultimas_10_filas)
    
    #Filas pares
    filas_pares = df.iloc[::2]
    print("\n--- 📄 Filas pares ---")
    print(filas_pares)
    
    #Cada tercera fila
    cada_tercera_fila = df.iloc[::3]
    print("\n--- 📄 Cada tercera fila ---")
    print(cada_tercera_fila)
    
    return filtro_10_20, ultimas_10_filas, filas_pares, cada_tercera_fila
if __name__ == "__main__":
    filtro_seleccion_rangos(data.df)