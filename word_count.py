# El texto Noland el Mentiroso ipsum es un texto de prueba que se utiliza para demostrar distintas

# tipografías además de usarse para rellenar espacios que requieran largos textos :

#Hace cuatrocientos años en cierto país de los mares del norte, existió un hombre llamado Mont Blanc Noland. Un explorador cuyas historias narraban grandes aventuras de sus viajes alrededor del mundo. Sonaban como mentiras pero la población nunca podía determinar si eran ciertas o no.En una ocasión Noland se fue de excursión y cuando volvió informó al rey explicándole que había visto una montaña de oro en una isla a través de los grandes mares. Para verlo por sí mismo, el valiente rey tomó dos mil guerreros y cruzó los grandes mares, luchó contra poderosas tormentas y enormes monstruos marinos.Finalmente el rey, Noland y sólo cien soldados desembarcaron en la isla, pero no había nada más que selva en ésta. Noland fue condenado a muerte por sus mentiras, y sus últimas palabras fueron: «¡¡Seguramente esa parte de la isla se haya hundido y ahora esté en el fondo del mar!!». El rey y los ciudadanos se sorprendieron, pensando que Noland no dejó de mentir hasta su muerte.

# ¿Cuántas palabras componen este texto?
# Genere un archivo llamado word_count.py que importe un texto a Python y realice las # siguientes tareas:
# Utilizando una estructura de datos apropiada, cuente la cantidad de caracteres # distintos que componen un texto.
# Cuente el número de palabras distintas que componen el texto ingresado. Para separar un texto por espacios puede utilizar el método .# split("").
# TIP: Para importar texto en python puede adaptar el siguiente código:
# with open(“texto.txt”, "r") as file:
     # texto=file.read()

def contar_caracteres_y_palabras(texto):
    # Inicializar diccionarios para almacenar caracteres y palabras únicas
    caracteres_distintos = {}
    palabras_distintas = {}

    # Contar caracteres distintos
    for char in texto:
        if char not in caracteres_distintos:
            caracteres_distintos[char] = 1

    # Contar palabras distintas
    palabras = texto.split()
    for palabra in palabras:
        # Eliminar signos de puntuación si es necesario
        palabra_sin_puntuacion = palabra.strip(".,;:!?")
        if palabra_sin_puntuacion not in palabras_distintas:
            palabras_distintas[palabra_sin_puntuacion] = 1

    return len(caracteres_distintos), len(palabras_distintas)

# Texto de ejemplo
texto_ejemplo = "Hace cuatrocientos años en cierto país de los mares del norte, existió un hombre llamado Mont Blanc Noland. Un explorador cuyas historias narraban grandes aventuras de sus viajes alrededor del mundo. Sonaban como mentiras pero la población nunca podía determinar si eran ciertas o no.En una ocasión Noland se fue de excursión y cuando volvió informó al rey explicándole que había visto una montaña de oro en una isla a través de los grandes mares. Para verlo por sí mismo, el valiente rey tomó dos mil guerreros y cruzó los grandes mares, luchó contra poderosas tormentas y enormes monstruos marinos.Finalmente el rey, Noland y sólo cien soldados desembarcaron en la isla, pero no había nada más que selva en ésta. Noland fue condenado a muerte por sus mentiras, y sus últimas palabras fueron: «¡¡Seguramente esa parte de la isla se haya hundido y ahora esté en el fondo del mar!!». El rey y los ciudadanos se sorprendieron, pensando que Noland no dejó de mentir hasta su muerte."

# Llamada a la función
caracteres, palabras = contar_caracteres_y_palabras(texto_ejemplo)
print("Cantidad de caracteres distintos:", caracteres)
print("Cantidad de palabras distintas:", palabras)

