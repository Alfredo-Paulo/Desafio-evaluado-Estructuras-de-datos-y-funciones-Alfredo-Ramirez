# Crear un archivo conversiones.py y una estructura de datos apropiada que permita ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.
# 
# Para ello considere las siguientes tasas de conversión de Peso Chileno:
#  a Sol peruano: 0.0046
#  a Peso Argentino: 0.093
#  a Dólar Americano: 0.00013
# Además, ingrese un 4to argumento que sea el valor en peso chileno a convertir. El programa debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas.
# Al ejecutar el programa se espera el siguiente output: python conversiones.py 0.0046 0.093 0.0013 10000
# Respuesta esperada:
# Los 10000 pesos equivalen a:
# 46.0 Soles
# 930.0 Pesos Arg

import sys

# Definición de las tasas de conversión proporcionadas
tasas_conversion = {
    "Sol": 0.0046,
    "Peso_Argentino": 0.093,
    "Dolar_Americano": 0.00013
}

# Función para convertir el valor en pesos chilenos a las tres divisas especificadas
def convertir_pesos_chilenos(tasas, cantidad):
    # Realizar las conversiones utilizando las tasas de conversión proporcionadas
    sol_peruano = cantidad * tasas["Sol"]
    peso_argentino = cantidad * tasas["Peso_Argentino"]
    dolar_americano = cantidad * tasas["Dolar_Americano"]
    return sol_peruano, peso_argentino, dolar_americano

def main():
    # Verificar si se proporcionan los argumentos adecuados
    if len(sys.argv) != 5:
        print("Usage: python conversiones.py <tasa_sol> <tasa_peso_argentino> <tasa_dolar> <cantidad>")
        return
    
    # Obtener las tasas ingresadas desde la línea de comandos
    tasas_ingresadas = {
        "Sol": float(sys.argv[1]),
        "Peso_Argentino": float(sys.argv[2]),
        "Dolar_Americano": float(sys.argv[3])
    }
    # Obtener la cantidad en pesos chilenos desde la línea de comandos
    cantidad = float(sys.argv[4])

    # Realizar la conversión utilizando las tasas ingresadas
    sol, peso_argentino, dolar = convertir_pesos_chilenos(tasas_ingresadas, cantidad)

    # Imprimir los resultados formateados como se espera
    print(f"Los {cantidad} pesos equivalen a:")
    print(f"{sol:.1f} Soles")
    print(f"{peso_argentino:.1f} Pesos Argentinos")
    print(f"{dolar:.1f} Dólares")

if __name__ == "__main__":
    main()

# ejemplo: ejecutamos el programa con los siguientes argumentos en la línea de comandos:  # " python conversiones.py 0.0046 0.093 0.0013 10000 "



# Los 10000 pesos equivalen a:
# 46.0 Soles
# 930.0 Pesos Argentinos
# 13.0 Dólares

