""" 
#### **Ejercicio 19: Combinaciones de .iloc**
Desarrolla una función que combine diferentes usos de `.iloc`. La función debe:

- Crear múltiples vistas usando diferentes patrones de selección
- Combinar selección aleatoria con selección sistemática
- Usar `.iloc` para crear muestras estratificadas
- Comparar diferentes métodos de muestreo
"""

import pandas as pd
import numpy as np
import data as data  # tu DataFrame base

def combinaciones_iloc(df):
    print("\n=== 🎯 EJERCICIO 19: Combinaciones de .iloc ===")

    # --- 1️⃣ Vistas con diferentes patrones ---
    print("\n--- 🔹 Vista 1: Primeras 5 filas y columnas 0 a 3 ---")
    vista_1 = df.iloc[:5, :4]
    print(vista_1)

    print("\n--- 🔹 Vista 2: Filas alternas (0,2,4,6,...) y columnas edad y departamento ---")
    vista_2 = df.iloc[::2, [3, 4]]
    print(vista_2.head())

    # --- 2️⃣ Combinación aleatoria + sistemática ---
    np.random.seed(42)
    filas_random = np.random.choice(len(df), size=5, replace=False)
    # Seleccionamos columnas de interés (edad y salario)
    vista_aleatoria = df.iloc[filas_random, [3, 5]]
    vista_sistematica = df.iloc[::10, [3, 5]]

    print("\n--- 🎲 Vista Aleatoria ---")
    print(vista_aleatoria)

    print("\n--- 📏 Vista Sistemática ---")
    print(vista_sistematica)

    # --- 3️⃣ Muestra estratificada (corregida) ---
    print("\n--- 🧩 Muestra Estratificada por 'departamento' ---")
    estratificada = (
        df.groupby("departamento", group_keys=False)
          .apply(lambda x: x.iloc[np.random.choice(range(len(x)), size=min(2, len(x)), replace=False)])
    )
    print(estratificada)

    # --- 4️⃣ Comparar métodos ---
    resumen = pd.DataFrame({
        "Método": ["Aleatoria", "Sistemática", "Estratificada"],
        "Promedio salario": [
            vista_aleatoria["salario"].mean(),
            vista_sistematica["salario"].mean(),
            estratificada["salario"].mean()
        ],
        "Promedio edad": [
            vista_aleatoria["edad"].mean(),
            vista_sistematica["edad"].mean(),
            estratificada["edad"].mean()
        ]
    })

    print("\n--- 📊 Comparación de Métodos de Muestreo ---")
    print(resumen)

    return vista_1, vista_2, vista_aleatoria, vista_sistematica, estratificada, resumen


if __name__ == "__main__":
    combinaciones_iloc(data.df)
