# Proyectos de Python

## conversiones.py
Este script permite convertir una cantidad de dinero en pesos chilenos a otras divisas, utilizando tasas de conversión ingresadas como argumentos de línea de comandos.
### Uso
python conversiones.py <tasa_sol> <tasa_peso_argentino> <tasa_dolar_americano> <monto_en_pesos_chilenos>

### Ejemplo
python conversiones.py 0.0046 0.093 0.0013 10000

### Respuesta Esperada
Los 10000 pesos equivalen a:
46.0 Soles
930.0 Pesos Argentinos
13.0 Dólares

## word_count.py
Este script cuenta la cantidad de caracteres y palabras distintas en un archivo de texto.
### Uso
python word_count.py <archivo_de_texto>
### Ejemplo
python word_count.py lorem_ipsum.txt

### Respuesta Esperada
El número de caracteres distintos es: 40
El número de palabras distintas es: 243
## recordatorios.py
Este script maneja una lista de eventos para recordar, permitiendo agregar, editar y eliminar eventos de la lista.
### Uso
python recordatorios.py
### Ejemplo
python recordatorios.py
### Respuesta Esperada
[['2021-01-01', '11:00', 'Levantarse y ejercitar'],
['2021-01-02', '06:00', 'Empezar el año'],
['2021-07-16', '13:00', 'No hacer nada es feriado'],
['2021-09-18', '16:00', 'Ramadas'],
['2021-12-24', '22:00', 'Cena de Navidad'],
['2021-12-25', '00:00', 'Navidad'],
['2021-12-31', '22:00', 'Cena de Año Nuevo']]
## Nota
Por favor, asegúrate de que los archivos de texto y cualquier otro recurso necesario estén en el directorio adecuado para que los scripts funcionen correctamente.
