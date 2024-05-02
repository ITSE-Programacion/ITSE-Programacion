# @title ejercicio con fechas
"""
Se informa el número y nombre del día de la semana de una fecha dada.
"""


# importar el modulo datetime
import datetime

# se crea un diccionario con los nombres
# de los días de la semana
dias_de_la_semana = {1: "lunes",
                     2: "martes",
                     3: "miércoles",
                     4: "jueves",
                     5: "viernes",
                     6: "sábado",
                     7: "domingo"}
dia = 5
mes = 11
anio = 2018

# se crea una fecha
fecha = datetime.date(anio, mes, dia)

# utilizando la función isoweekday()
#  se obtiene el número de día de la semana
numero_dia_semana = fecha.isoweekday()
print(f"La fecha: {fecha:%Y/%B/%d} tiene el número de día de la semana: {numero_dia_semana} y se llama: {dias_de_la_semana[numero_dia_semana]}")
