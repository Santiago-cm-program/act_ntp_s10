"""
#### **Ejercicio 10: Análisis Completo con .loc**
Implementa una función que realice un análisis completo usando `.loc`. La función debe:

- Crear múltiples vistas del DataFrame usando diferentes filtros
- Calcular métricas por departamento y ciudad
- Identificar empleados con características específicas (top performers, nuevos, etc.)
- Generar un reporte completo con todas las métricas
"""

import pandas as pd
import data as data
from datetime import datetime


def analisis_completo(df):
    print("\n========== 📊 ANÁLISIS COMPLETO DE EMPLEADOS ==========\n")

    # 🧩 1️⃣ Crear múltiples vistas del DataFrame usando .loc

    # Empleados activos
    activos = df.loc[df["activo"] == True]

    # Empleados con más de 10 años de experiencia
    senior = df.loc[df["experiencia_años"] > 10]

    # Empleados con salario bajo, medio y alto según percentiles
    p25, p75 = df["salario"].quantile([0.25, 0.75])
    salario_bajo = df.loc[df["salario"] <= p25]
    salario_medio = df.loc[(df["salario"] > p25) & (df["salario"] < p75)]
    salario_alto = df.loc[df["salario"] >= p75]

    print("🟢 Empleados activos:", len(activos))
    print("🧓 Empleados con más de 10 años de experiencia:", len(senior))
    print(f"💰 Rangos salariales -> Bajo: ≤ {int(p25)} | Medio: entre {int(p25)}-{int(p75)} | Alto: ≥ {int(p75)}")

    # 📊 2️⃣ Calcular métricas por departamento y ciudad
    metricas_dep = (
        df.groupby("departamento")
        .agg(
            empleados=("empleado_id", "count"),
            salario_promedio=("salario", "mean"),
            edad_promedio=("edad", "mean"),
            experiencia_promedio=("experiencia_años", "mean"),
        )
        .round(1)
    )

    metricas_ciudad = (
        df.groupby("ciudad")
        .agg(
            empleados=("empleado_id", "count"),
            salario_promedio=("salario", "mean"),
            antiguedad_promedio=("fecha_ingreso", lambda x: (datetime.now().year - x.dt.year).mean()),
        )
        .round(1)
    )

    print("\n--- 🏢 Métricas por Departamento ---")
    print(metricas_dep)
    print("\n--- 🌆 Métricas por Ciudad ---")
    print(metricas_ciudad)

    # 🏆 3️⃣ Identificar empleados destacados y nuevos
    top_performers = df.loc[df["salario"] >= df["salario"].quantile(0.9)]
    nuevos = df.loc[df["fecha_ingreso"] >= pd.Timestamp(datetime.now().year - 1, 1, 1)]

    print("\n--- 🏅 Top Performers (salario en el top 10%) ---")
    print(top_performers[["empleado_id", "nombre", "departamento", "salario", "experiencia_años"]])

    print("\n--- 🆕 Empleados ingresados recientemente (último año) ---")
    print(nuevos[["empleado_id", "nombre", "fecha_ingreso", "departamento"]])

    # 📘 4️⃣ Generar un reporte completo
    reporte = {
        "Total empleados": len(df),
        "Empleados activos": len(activos),
        "Top performers": len(top_performers),
        "Nuevos empleados": len(nuevos),
        "Promedio general de salario": round(df["salario"].mean(), 2),
        "Edad promedio general": round(df["edad"].mean(), 1),
        "Experiencia promedio general": round(df["experiencia_años"].mean(), 1),
    }

    print("\n--- 📋 Resumen General ---")
    for k, v in reporte.items():
        print(f"{k}: {v}")

    return {
        "activos": activos,
        "senior": senior,
        "metricas_dep": metricas_dep,
        "metricas_ciudad": metricas_ciudad,
        "top_performers": top_performers,
        "nuevos": nuevos,
        "reporte": reporte,
    }


# 🚀 Ejecutar análisis solo si es el archivo principal
if __name__ == "__main__":
    analisis_completo(data.df)
