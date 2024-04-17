# Se provee del archivo recordatorios.py que incluye una serie de eventos que quieren ser recordados por usted. El formato de estos recordatorios son una fecha (año-mes-día), una hora y una descripción del evento.
# 
# Aplicando métodos apropiados para la estructura de datos entregada edite la lista de recordatorios de la siguiente manera:
# NOTA: Los eventos deben siempre editarse de tal manera que mantengan su orden en el tiempo. Y el código debe ejecutarse en el orden entregado en las
# instrucciones dadas a continuación:
# 1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
# 2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio.
# 3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo.
# 4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
# Al ejecutar el programa se espera el siguiente output: python recordatorios.py
# [['2021-01-01', '11:00', 'Levantarse y ejercitar'],
# ['2021-01-02', '06:00', 'Empezar el año'],
# ['2021-07-16', '13:00', 'No hacer nada es feriado'],
# ['2021-09-18', '16:00', 'Ramadas'],
# ['2021-12-24', '22:00', 'Cena de Navidad'],
# ['2021-12-25', '00:00', 'Navidad'],
# ['2021-12-31', '22:00', 'Cena de Año Nuevo']]


recordatorios = [
    ['2021-01-01', '11:00', 'Levantarse y ejercitar'],
    ['2021-07-15', '13:00', 'No hacer nada es feriado'],
    ['2021-09-18', '16:00', 'Ramadas'],
]

# 1. Agregar evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
nuevo_evento = ['2021-02-02', '06:00', 'Empezar el año']
recordatorios.append(nuevo_evento)

# 2. Corregir el evento del 15 de Julio al 16 de Julio.
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'

# 3. Eliminar el evento del día del trabajo.
for evento in recordatorios:
    if "trabajo" in evento[2]:
        recordatorios.remove(evento)
        break  # Rompemos el bucle después de eliminar el primer evento del trabajo.

# 4. Agregar una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
cena_navidad = ['2021-12-24', '22:00', 'Cena de Navidad']
navidad = ['2021-12-25', '00:00', 'Navidad']
cena_ano_nuevo = ['2021-12-31', '22:00', 'Cena de Año Nuevo']
recordatorios.append(cena_navidad)
recordatorios.append(navidad)
recordatorios.append(cena_ano_nuevo)

# Imprimir los recordatorios actualizados
for evento in recordatorios:
    print(evento)
