# Introducción a la Algoritmia - Clase 4

def Ejercicio1():
    print("\n| Ejercicio 1 |")
    primer_num = 0
    ultimo_num = 0
    num_ingresado = int(input("Para finalizar el programa, escribir '-1'. Ingresá un número entero: "))
    primer_num = num_ingresado
    while num_ingresado != -1:
        ultimo_num = num_ingresado
        num_ingresado = int(input("Ingresá otro número: "))
        
    print(f"El primer número ingresado fue el {primer_num} y el último fue el {ultimo_num}.")
    
    
def Ejercicio2():
    print("\n| Ejercicio 2 |")
    suma = 0
    num_ingresado = int(input("Para finalizar el programa, escribir '-1'. Ingresá un número entero: "))
    while num_ingresado != -1:
        suma += num_ingresado
        num_ingresado = int(input("Ingresá otro número: "))
    
    if suma % 2 == 0:
        print(f"La suma de los números ingresados es {suma} y es par.")
    else:
        print(f"La suma de los números ingresados es {suma} y es impar.")
    
    
def Ejercicio3():
    print("\n| Ejercicio 3 |")
    num_menor = 0
    num_mayor = 0
    num_ingresado = int(input("Para finalizar el programa, escribir '-1'. Ingresá un número entero: "))
    while num_ingresado != -1:
        if num_menor == 0 and num_mayor == 0:
            num_menor = num_ingresado
            num_mayor = num_ingresado
        elif num_ingresado < num_menor:
            num_menor = num_ingresado
        elif num_ingresado > num_mayor:
            num_mayor = num_ingresado
        else:
            pass
        num_ingresado = int(input("Ingresá otro número: "))
        
    print(f"El menor número ingresado fue el {num_menor} y el mayor fue el {num_mayor}.")
    

def Ejercicio4():
    print("\n| Ejercicio 4 |")
    suma_nums_impares = 0
    for num in range(42, 177):
        if num % 2 != 0: # Si el número es impar
            suma_nums_impares += num
        num += 1
    print(f"La suma de los números impares entre 42 y 176 es {suma_nums_impares}.")
    

def Ejercicio5():
    print("\n| Ejercicio 5 |")
    contadorNums = 1
    numNatural = int(input("Por favor, ingresá un número natural: "))
    while numNatural <= 0:
        numNatural = int(input("El número ingresado no es natural. Por favor, ingresá uno natural: "))
    print(f"Los números naturales del 1 al {numNatural} inclusive son:")
    while contadorNums >= 1 and contadorNums <= numNatural:
        print(contadorNums)
        contadorNums += 1


def Ejercicio6():
    print("\n| Ejercicio 6 |")
    num_tabla_de_multiplicar = int(input("Ingresá el número de la tabla de multiplicar que querés ver (del 1 al 12): "))
    while num_tabla_de_multiplicar < 1 or num_tabla_de_multiplicar > 12:
        num_tabla_de_multiplicar = int(input("El número ingresado no es válido. Por favor, ingresá un número del 1 al 12: "))
    for num in range (1, 13):
        print(f"{num_tabla_de_multiplicar} x {num} = {num_tabla_de_multiplicar * num}")
        num += 1


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
    elif ejercicioSeleccionado == 4:
        Ejercicio4()
    elif ejercicioSeleccionado == 5:
        Ejercicio5()
    elif ejercicioSeleccionado == 6:
        Ejercicio6()
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 14 o '0' para salir del programa: ")