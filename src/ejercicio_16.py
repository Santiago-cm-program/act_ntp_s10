""" #### **Ejercicio 16: Selección con Pasos**
Desarrolla una función que use pasos en la selección con `.iloc`. La función debe:

- Seleccionar cada segunda fila
- Seleccionar filas en orden inverso
- Seleccionar cada quinta fila empezando desde la tercera posición
- Combinar pasos en filas y columnas """
import pandas as pd
import data as data

def seleccion_con_pasos(df):
    #seleccionar cada segunda fila  
    cada_segunda_fila= df.iloc[::2]
    print("\n--- 📄 Cada segunda fila ---")
    print(cada_segunda_fila)
    
    #seleccionar filas en orden inverso
    filas_orden_inverso = df.iloc[::-1]
    print("\n--- 📄 Filas en orden inverso ---")
    print(filas_orden_inverso)
    
    #Seleccionar cada quinta fila empezando desde la tercera posición
    cada_quinta_fila= df.iloc[2::5]
    print("\n--- 📄 Cada quinta fila empezando desde la tercera posición ---")
    print(cada_quinta_fila)
    #Combinar pasos en filas y columnas
    combinacion_filas_columnas = df.iloc[::3, ::2]
    print("\n--- 📄 Combinación de cada tercera fila y cada segunda columna ---")
    print(combinacion_filas_columnas)
    
    return cada_segunda_fila, filas_orden_inverso, cada_quinta_fila, combinacion_filas_columnas

if __name__ == "__main__":
    seleccion_con_pasos(data.df)