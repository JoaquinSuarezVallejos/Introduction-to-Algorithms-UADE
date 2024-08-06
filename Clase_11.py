# Introducción a la Algoritmia - Clase 11

# MATRICES

import random

# Ejercicio 1: Crear una matriz de n x m y llenarla con números ingresados por el usuario. Luego imprimir la matriz en consola.
def Ejercicio1():
    filas = int(input("Ingresá la cantidad de filas que deseás que tenga la matriz: "))
    columnas = int(input("Ahora ingresá la cantidad de columnas: "))

    matriz = []

    for fila in range(filas):
        matriz.append([])
        for columna in range(columnas):
            matriz[fila].append(0)

    print(matriz)

    for fila in range(filas):
        for columna in range(columnas):
            matriz[fila][columna] = int(input("Ingresá un número: "))

    print(matriz)

    for fila in range(filas):
        for columna in range(columnas):
            print(matriz[fila][columna], end = " ")
        print()

# Ejercicio 2: Crear una matriz de 3x3 y llenarla con números del 1 al 9. Luego imprimir la matriz en consola.
def Ejercicio2():
    matriz = []

    contador = 1

    for fila in range(3):
        fila = []
        for columna in range(3):
            fila.append(contador)
            contador += 1
        matriz.append(fila)
    
    for fila in range (3):
        for columna in range(3):
            print(matriz[fila][columna], end = " ")
        print()
    
# Ejercicio 3: Sumar los elementos de una matriz de 2x2. Pasos: Crear una matriz de 2x2 con números aleatorios de 0 a 9. 
# Sumar todos esos elementos e imprimir la suma.
def Ejercicio3():
    matriz_dos_por_dos = []
    suma = 0

    for f in range(2):
        fila = []
        for c in range(2):
            valor = random.randint(0, 9)
            fila.append(valor)
            suma += valor
        matriz_dos_por_dos.append(fila)
    
    print(matriz_dos_por_dos)
    print(f"La suma de los elementos de la matriz es igual a: {suma}")
    
# Ejercicio 4: Multiplicar una matriz de 4x4 por un número que ingrese el usuario.
def Ejercicio4():
    matriz_cuatro_por_cuatro = []

    matriz_cuatro_por_cuatro.append([1, 2, 3, 4]) 
    matriz_cuatro_por_cuatro.append([5, 6, 7, 8])
    matriz_cuatro_por_cuatro.append([9, 10, 11, 12])
    matriz_cuatro_por_cuatro.append([13, 14, 15, 16])

    numero = int(input("Ingresá el valor por el que querés multiplicar la matriz: "))

    print(f"Matriz antes de multiplicar por {numero}: ")
    for f in range(len(matriz_cuatro_por_cuatro)):
        for c in range(len(matriz_cuatro_por_cuatro[f])):
            print(matriz_cuatro_por_cuatro[f][c], end = " ")
        print()
    
    print(f"Matriz después de multiplicar por {numero}: ")
    for f in range(len(matriz_cuatro_por_cuatro)):
        for c in range(len(matriz_cuatro_por_cuatro[f])):
            matriz_cuatro_por_cuatro[f][c] *= numero
            print(matriz_cuatro_por_cuatro[f][c], end = " ")
        print()

############################################################################################################

xCheck = False

while xCheck == False:
    ejercicioSeleccionado = int(input("\nIngresá el número del ejercicio que querés ejecutar (del 1 al 4) o '0' para salir del programa: "))
    if ejercicioSeleccionado == 1:
        Ejercicio1()
    elif ejercicioSeleccionado == 2:
        Ejercicio2()
    elif ejercicioSeleccionado == 3:
        Ejercicio3()
    elif ejercicioSeleccionado == 4:
        Ejercicio4()
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 4 o '0' para salir del programa: ")