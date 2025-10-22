""" #### **Ejercicio 7: Filtrado por Fechas**
Implementa una función que filtre por fechas usando `.loc`. La función debe:

- Filtrar empleados que ingresaron en 2022
- Filtrar empleados que ingresaron en los últimos 2 años
- Filtrar empleados que ingresaron en el primer trimestre de cualquier año
- Calcular la antigüedad promedio de cada grupo """

import pandas as pd
import data as data
import datetime as dt

def filtro_fechas(df):
    #Filtro empleados que ingresaron en el 2022
    filtro_2022= df.loc[df["fecha_ingreso"].dt.year == 2022]