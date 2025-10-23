""" 
#### **Ejercicio 8: Filtrado Avanzado con Funciones**
Crea una función que use funciones personalizadas con `.loc`. La función debe:

- Crear una función que clasifique salarios (bajo, medio, alto)
- Filtrar empleados con salario superior al promedio
- Filtrar empleados con salario en el percentil 75
- Mostrar distribución de cada categoría """

import pandas as pd
import data as data 

def filtro_salario(df):
    def clasificar_salario(valor,bajo,alto):
        if valor < bajo:
            return 'Bajo'
        elif valor < alto:
            return 'Medio'
        else:
            return 'Alto'
        
    #Calculo de percentiles
    percentil_25 = df['salario'].quantile(0.25)
    percentil_75 = df['salario'].quantile(0.75)
    
    df["categoria_salario"]= df["salario"].apply(lambda x: clasificar_salario(x,percentil_25,percentil_75)) 
    
    salario_primedio = df["salario"].mean()
    salario_superior_promedio = df.loc[df["salario"] > salario_primedio]
    print("\n--- 💰 Empleados con salario superior al promedio ---")
    print(salario_superior_promedio)
    
    salario_percentil_75 = df.loc[df["salario"] >= percentil_75]
    print("\n--- 💰 Empleados con salario en el percentil 75 ---")
    print(salario_percentil_75)
    
    distribucion = df["categoria_salario"].value_counts()
    print("\n--- 📊 Distribución de categorías de salario ---")
    print(distribucion)
    
    return salario_superior_promedio, salario_percentil_75, distribucion

if __name__ == "__main__":
    filtro_salario(data.df)
    