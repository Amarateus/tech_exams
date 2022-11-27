import sys
import time
from itertools import combinations_with_replacement
import os


# Solicitar un nuemro entre 0 y 32000
# Maximo 10 intentos
def pedir_numero():
    intentos = 0
    while intentos < 10:
        try:
            eleccion = int(input("Ingrese un valor entre 0 y 32000: "))
            if eleccion < 0 or eleccion > 32000:
                print("Valor fuera del rango solicitado")
            else:
                return eleccion
        except ValueError:
            print("Debe ingresar un numero entero")
        intentos += 1
    print("Ya has realizado remasiados intentos. Cerrando el programa..")
    time.sleep(2)
    sys.exit()

def crear_fichas(numero):
    lista_numeros = list(range(numero + 1))
    lista_numeros.reverse()
    fichas = combinations_with_replacement(lista_numeros, 2)
    return list(fichas)


######## PROGRAMA #########
while True:
    os.system("cls")
    print("Comenzando programa:")
    print()
    print(crear_fichas(pedir_numero()))
    print()
    pregunta = input("Desea salir del programa? (SI o NO): ")
    if pregunta.lower() == "si" or pregunta.lower() == "s":
        print("Cerrando programa...")
        time.sleep(2)
        sys.exit()