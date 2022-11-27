from tabulate import tabulate

def crear_matriz(n):
    numeros = list(range(1, n*n + 1))   # Almaceno todos los numeros que usaré en la matriz
    separacion = []  # Separo los numeros en columnas
    while len(numeros) != 0:
        porcion = numeros[:n]
        separacion.append(porcion)
        del(numeros[:n])   

    for i in separacion:
        if separacion.index(i)%2 != 0:
            i.reverse()

    lista_final = []
    elem_1 = 0
    elem_2 = 0
    while elem_1 != n:
        nueva_lista = []
        while elem_2 != n:
            nueva_lista.append(separacion[elem_2][elem_1])
            elem_2 += 1
        lista_final.append(nueva_lista)
        elem_2 = 0
        elem_1 += 1

    return lista_final

columnas = int(input("Ingrese cantidad de columnas: "))

print(tabulate(crear_matriz(columnas)))
