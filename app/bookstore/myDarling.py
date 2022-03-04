import pandas as pd
import numpy as np
import time
from datetime import datetime

dias = {
    "Mon" : "Lunes",
    "Tue" : "Martes",
    "Wed" : "Miercoles",
    "Thu" : "Jueves",
    "Fri" : "Viernes",
    "Sat" : "Sabado",
    "Sun" : "Domingo"
}

meses = {
    "Jan" : "Enero",
    "Feb" : "Febrero",
    "Mar" : "Marzo",
    "Apr" : "Abril",
    "May" : "Mayo",
    "Jun" : "Junio",
    "Jul" : "Julio",
    "Aug" : "Agosto",
    "Sep" : "Septiembre",
    "Oct" : "Octubre",
    "Nov" : "Noviembre",
    "Dec" : "Diciembre"
}


def get_now():
    # Obtener Fecha actual
    date_object = datetime.today()
    now = datetime.today().strftime('%Y-%m-%d %I:%M:%S %p')
    return now