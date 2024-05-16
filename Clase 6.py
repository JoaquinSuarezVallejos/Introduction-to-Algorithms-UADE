# Introducción a la Algoritmia - Clase 6

def Ejercicio1():
    numeros = []
    for i in range(0, 10):
        num = int(input("Ingrese un número: "))
        numeros.append(num)

    print("Lista original: ")
    print(numeros)

    print("Lista inversa: ")
    for i in range(9, -1, -1):
        print(numeros[i])
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(len(nums))

    for i in range(len(nums)):
        print(nums[i])
    
    
def Ejercicio2():
    # Leer 5 nums, calcular su promedio e imprimir los que son mayores al promedio
    numeros = []
    suma = 0
    promedio = 0

    for i in range(0, 5):
        num = int(input("Ingrese un número: "))
        numeros.append(num)
        suma += num

    promedio = suma / (len(numeros))

    print("Lista resultante: ", numeros)
    print("Promedio calculado: ", promedio)

    print("Números mayores al promedio: ")
    for i in range(len(numeros) -1):
        if numeros[i] > promedio:
            print(numeros[i], end=" ")

def Ejercicio3():
    
    lista = []
    bandera = True
    while bandera:
        n = int(input("Ingrese un número: "))
        if n == -1:
            bandera = False
        else:
            lista.append(n)
    
    max = lista[0]
    posicion = 0
    
    for i in range(len(lista) -1):
        if lista[i] > max:
            max = lista[i]
            posicion = i
    
    print(lista)
    print("El mayor número es: ", max, " y se encuentra en la posición: ", posicion)
    
    del lista[posicion]
    
    print(lista)
    
    
def Ejercicio4():
    # Escribir una función para ingresar números enteros en una lista y devolverla como valor de retorno. 
    # La cantidad de valores a leer se recibe como parámetro.
    
    def cargarLista(cantidad):
        lista = []
        for i in range(cantidad):
            num = int(input("Ingrese un número: "))
            lista.append(num)
        return lista
    
    cant = int(input("Ingrese la cantidad de números a ingresar: "))
    lista = cargarLista(cant)
    print(lista)
   
    
def Ejercicio5(): #Ej 1 y 2 de la guía
    # Escribir una función para ingresar desde el teclado una serie de números entre A y B y guardarlos en una lista. 
    # En caso de ingresar un valor fuera de rango la función mostrará un mensaje de error y solicitará un nuevo número. 
    # Para finalizar la carga se deberá ingresar -1. La función recibe como parámetros los valores de A y B, y devuelve
    # la lista cargada (o vacía, si el usuario no ingresó nada) como valor de retorno. 
    # Tener en cuenta que A puede ser mayor, menor o igual que B.
    
    def cargarLista(A, B):
        lista = []
        if A > B:
            aux = A
            A = B
            B = aux
        
        flag = True
        while flag:
            num = int(input(f"Ingrese un número para agregar a la lista entre {A} y {B}: "))
            if num == -1:
                flag = False
            elif num >= A and num <= B:
                lista.append(num)
            else:
                print("El número ingresado no está dentro del rango permitido.")
        return lista

    def calcularSuma(lista):
        suma = 0
        for i in range(len(lista)):
            suma += lista[i]
        return suma
    
    min = int(input("Ingrese el valor mínimo a evaluar: "))
    max = int(input("Ingrese el valor máximo a evaluar: "))
    lista = cargarLista(min, max)
    print(lista)
    
    print("La suma de los valores ingresados es: ", calcularSuma(lista))


def Ejercicio6():
    def determinarCapicua(lista):
        listaInversa = []
        
        for i in range (len(lista) -1, -1, -1):
            listaInversa.append(lista[i])
        
        for i in range(len(lista)):
            if lista[i] != listaInversa[i]:
                return False
        return True
    
    lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(determinarCapicua(lista))
        

def Ejercicio7():
    def contarApariciones(lista, elemento):
        contador = 0
        for i in range(len(lista)):
            if lista[i] == elemento:
                contador += 1
        return contador
    
    lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    elemento = 4
    print(contarApariciones(lista, elemento))
    

def Ejercicio8():
    def invertirOtraLista(lista):
        listaInversa = []
        
        for i in range (len(lista) -1, -1, -1):
            listaInversa.append(lista[i])
        return listaInversa

    lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    

############################################################################################################

xCheck = False

while xCheck == False:
    ejercicioSeleccionado = int(input("\nIngresá el número del ejercicio que querés ejecutar (del 1 al 14) o '0' para salir del programa: "))
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