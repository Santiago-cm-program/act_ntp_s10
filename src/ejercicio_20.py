"""
#### **Ejercicio 20: Análisis Completo con .iloc**
Implementa una función que realice un análisis completo usando `.iloc`. La función debe:

- Crear diferentes vistas del DataFrame usando posiciones
- Realizar análisis de muestras aleatorias vs sistemáticas
- Comparar rendimiento de diferentes métodos de selección
- Generar un reporte completo con métricas de las diferentes selecciones
"""

import pandas as pd
import numpy as np
import time
import data as data  # Se asume que data.df contiene el DataFrame base


def analisis_completo_iloc(df):
    print("\n=== 📊 EJERCICIO 20: Análisis Completo con .iloc ===")

    # --- 1️⃣ Crear diferentes vistas ---
    print("\n--- 🔹 Vista 1: Primeras 10 filas y columnas 0 a 4 ---")
    vista_general = df.iloc[:10, :5]
    print(vista_general)

    print("\n--- 🔹 Vista 2: Últimas 10 filas y columnas 5 a 9 ---")
    vista_final = df.iloc[-10:, 5:10]
    print(vista_final)

    print("\n--- 🔹 Vista 3: Filas pares y columnas 2, 4, 6 ---")
    vista_pares = df.iloc[::2, [2, 4, 6]]
    print(vista_pares.head())

    # --- 2️⃣ Comparar muestras aleatorias y sistemáticas ---
    np.random.seed(42)
    n_muestra = 10

    # Aleatoria
    t0 = time.time()
    filas_random = np.random.choice(len(df), size=n_muestra, replace=False)
    muestra_aleatoria = df.iloc[filas_random, [3, 4, 5]]
    tiempo_aleatoria = time.time() - t0

    # Sistemática
    t1 = time.time()
    muestra_sistematica = df.iloc[::len(df)//n_muestra, [3, 4, 5]]
    tiempo_sistematica = time.time() - t1

    print("\n--- 🎲 Muestra Aleatoria ---")
    print(muestra_aleatoria)

    print("\n--- 📏 Muestra Sistemática ---")
    print(muestra_sistematica)

    # --- 3️⃣ Calcular métricas comparativas ---
    metricas = pd.DataFrame({
        "Método": ["Aleatoria", "Sistemática"],
        "Promedio edad": [
            muestra_aleatoria["edad"].mean(),
            muestra_sistematica["edad"].mean()
        ],
        "Promedio salario": [
            muestra_aleatoria["salario"].mean(),
            muestra_sistematica["salario"].mean()
        ],
        "Tiempo de ejecución (segundos)": [tiempo_aleatoria, tiempo_sistematica]
    })

    print("\n--- ⏱️ Comparación de rendimiento y métricas ---")
    print(metricas)

    # --- 4️⃣ Reporte completo ---
    resumen = {
        "Total empleados": len(df),
        "Columnas totales": len(df.columns),
        "Edad promedio general": df["edad"].mean(),
        "Salario promedio general": df["salario"].mean(),
        "Método más rápido": (
            "Aleatoria" if tiempo_aleatoria < tiempo_sistematica else "Sistemática"
        ),
    }

    print("\n--- 📋 Reporte General ---")
    for k, v in resumen.items():
        print(f"{k}: {v}")

    return vista_general, vista_final, muestra_aleatoria, muestra_sistematica, metricas, resumen


if __name__ == "__main__":
    analisis_completo_iloc(data.df)
