# Introducción a la Algoritmia - Clase 7

# Copia de listas

# lista1 = [1, 2, 3, 4, 5]
# lista2 = []

# for i in range(len(lista1)):
#     lista2.append(lista1[i])

# print(lista1)
# print(lista2)
# lista1.append(66)
# print(lista1)

import random

def Ejemplo1():
    def cargarLista(n):
        lista = []
        while len(lista) < n:
            num = random.randint(1, 11)
            presente = False
            contador = 0
            while presente == False and contador < len(lista):
                if lista[contador] == num:
                    presente = True
                contador += 1
            
            if not presente:
                lista.append(num)
        return lista

    def buscarLista(elemento, lista):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return True
        return 

    def ordenarSeleccion(lista):
        for i in range(len(lista) -1):
            for j in range(i + 1, len(lista)):
                if lista[i] > lista[j]:
                    temp = lista[i]
                    lista[i] = lista[j]
                    lista[j] = temp
        return lista
    
# Ejercicio 1: crear una lista vacía y agregar números del 1 al 10.
def Ejercicio1():
    def cargarLista():
        lista = []
        for i in range(1, 11):
            lista.append(i)
        return lista
    print("Lista creada: ", cargarLista)

# Ejercicio 2: crear una función que informe la suma de los valores de una lista.
def Ejercicio2():
    lista = [1, 2, 3, 4, 5]
    def calcularSuma(lista):
        suma = 0
        for i in range(len(lista)):
            suma += lista[i]
        return suma
    print("La suma de los elementos es igual a: ", calcularSuma(lista))

# Ejercicio 3: obtener el máximo de la lista.
def Ejercicio3():
    lista = [1, 2, 3, 4, 5]
    def calcularMaximo(lista):
        max = lista[0]
        for i in range(len(lista)):
            if lista[i] > max:
                max = lista[i]
        return max
    print("El máximo de los elementos de la lista es:", calcularMaximo(lista))
    
# Ejercicio 4: buscar un elemento en la lista.
def Ejercicio4():
    lista = [1, 2, 3, 4, 5]
    def buscarElemento(lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    pos = buscarElemento(lista, 3)
    if lista == -1:
        print("El elemento no se encuentra en la lista.")
    else:
        print("El elemento se encuentra en la posición: ", pos)
        
# Ejercicio 5: ordenar una lista de forma secuencial.
def Ejercicio5():
    lista = [5, 3, 1, 4, 2]
    def ordenarListaSecuencial(lista):
        for i in range(len(lista) -1):
            for j in range(i + 1, len(lista)):
                if lista[i] > lista[j]:
                    temp = lista[i]
                    lista[i] = lista[j]
                    lista[j] = temp
        return lista
    print("Lista ordenada de forma secuencial: ", ordenarListaSecuencial(lista))
    
# Ejercicio 6: invertir una lista.
def Ejercicio6():
    lista = [1, 2, 3, 4, 5]
    listaInvertida = []
    def revertirLista(lista):
        for i in range(len(lista), -1, -1):
            listaInvertida.append(lista[i])
        return listaInvertida
    print("Lista invertida: ", revertirLista(lista))

# Ejercicio 7: 
    def Ejercicio7():
        def informarSegundoMayor(lista):
            if len(lista) < 2:
                return -1
            mayor = lista[0]
            segundo_mayor = None
            for i in range(len(lista)):
                if lista[i] > mayor:
                    segundo_mayor = mayor
                    mayor = lista[i]
                elif lista[i] > segundo_mayor:
                    segundo_mayor = lista[i]
            


############################################################################################################

xCheck = False

while xCheck == False:
    ejercicioSeleccionado = int(input("\nIngresá el número del ejercicio que querés ejecutar (del 1 al 3) o '0' para salir del programa: "))
    if ejercicioSeleccionado == 1:
        Ejercicio1()
    elif ejercicioSeleccionado == 2:
        Ejercicio2()
    elif ejercicioSeleccionado == 3:
        Ejercicio3()
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 14 o '0' para salir del programa: ")

    