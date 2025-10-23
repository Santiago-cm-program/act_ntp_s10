""" #### **Ejercicio 18: Trabajo con Listas de Índices**
Crea una función que trabaje con listas de índices dinámicas. La función debe:

- Generar listas de índices basadas en condiciones
- Encontrar posiciones que cumplan criterios específicos
- Seleccionar filas basadas en percentiles
- Mostrar diferentes muestras del DataFrame """

import pandas as pd
import data as data

def trabajo_listas_indices(df):
    #Lista de indices
    lista_indices = df.index[df['salario']>80000].tolist()
    seleccion_indices = df.iloc[lista_indices]
    print("\n--- 📄 Filas con salario mayor a 80000 ---")
    print(seleccion_indices)
    
    # Posiciones que cumplan criterios específicos
    posiciones_altos_salarios = df.index[(df['salario'] > 90000) & (df['experiencia_años'] > 5)].tolist()
    seleccion_posiciones = df.iloc[posiciones_altos_salarios]
    print("\n--- 📄 Filas con salario > 90000 y experiencia > 5 años ---")
    print(seleccion_posiciones)
    
    #seleccionar filas basadas en percentiles
    percentil_90 = df['salario'].quantile(0.9)
    filas_percentil_90 = df[df['salario'] >= percentil_90]
    print("\n--- 📄 Filas con salario en el percentil 90 o superior ---")
    print(filas_percentil_90)
    
    return lista_indices, seleccion_indices, posiciones_altos_salarios, seleccion_posiciones, filas_percentil_90
if __name__ == "__main__":
    trabajo_listas_indices(data.df)