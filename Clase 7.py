# Introducción a la Algoritmia - Clase 7

# LISTAS

import random
    
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
        for i in range(len(lista) - 1, -1, -1):
            listaInvertida.append(lista[i])
        return listaInvertida
    print("Lista invertida: ", revertirLista(lista))

# Ejercicio 7: informar el segundo mayor de una lista.
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
        return segundo_mayor
    lista = [1, 2, 3, 4, 5]
    print("El segundo mayor de la lista es: ", informarSegundoMayor(lista))
    
# Ejercicio 8: 
def Ejercicio8():
    def generarListaAleatoria(N):
        lista = []
        for i in range(N):
            lista.append(random.randint(1, 100))
        return lista
    
    def concatenarValoresParesEImpares(A, B):
        C = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                C.append(A[i])
        for i in range(len(B)):
            if B[i] % 2 != 0:
                C.append(B[i])
        return C
    
    def concatenarImparesyReverso(listaUno, listaDos):
        lista = []
        for i in range (len(listaUno)):
            if listaUno[i] % 2 != 0:
                lista.append(listaUno[i])
                
        pares = []
        for i in range (len(listaDos)):
            if listaDos[i] % 2 == 0:
                pares.append(listaDos[i])
        
        for num in pares:
            numero_invertido = 0
            while num > 0:
                ultimo_digito = num % 10
                numero_invertido = numero_invertido * 10 + ultimo_digito
                num //= 10
            lista.append(numero_invertido)
        return lista
    
    def intercalarListas(listaUno, listaDos):
        lista = []
        for i in range(len(listaUno)):
            lista.append(listaUno[i])
            lista.append(listaDos[i])
        return lista

    cantidad = int(input("Ingresá la cantidad de elementos de dos listas: "))
    A = generarListaAleatoria(cantidad)
    B = generarListaAleatoria(cantidad)
    
    print("Primer Lista (A): ", A)
    print("Segunda Lista (B): ", B)

    C = concatenarValoresParesEImpares(A, B)
    
    print("Lista con pares de A e impares de B: ", C)
    
    D = concatenarImparesyReverso(A, B)
    
    print("Lista con impares de A y pares de B invertidos: ", D)
    
    E = intercalarListas(A, B)
    
    print("Lista intercalada: ", E)
    
############################################################################################################

xCheck = False

while xCheck == False:
    ejercicioSeleccionado = int(input("\nIngresá el número del ejercicio que querés ejecutar (del 1 al 8) o '0' para salir del programa: "))
    if ejercicioSeleccionado == 1:
        Ejercicio1()
    elif ejercicioSeleccionado == 2:
        Ejercicio2()
    elif ejercicioSeleccionado == 3:
        Ejercicio3()
    elif ejercicioSeleccionado == 4:
        Ejercicio4()
    elif ejercicioSeleccionado == 5:
        Ejercicio5()
    elif ejercicioSeleccionado == 6:
        Ejercicio6()
    elif ejercicioSeleccionado == 7:
        Ejercicio7()
    elif ejercicioSeleccionado == 8:
        Ejercicio8()
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 8 o '0' para salir del programa: ")