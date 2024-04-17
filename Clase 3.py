# Introducción a la Algoritmia - Clase 3
    
# if 0<calificacion>100: ---- Estructura in-between (muy útil)
#     print("Calificación inválida")

def Ejercicio1():
    print("\n| Ejercicio 1 |")
    num1 = int(input("Ingresá un número entero: "))
    num2 = int(input("Ahora ingresá otro: "))
    if num1 == num2:
        print("Los números ingresados son iguales.")
    else:
        print("Los números ingresados son distintos.")


def Ejercicio2():
    print("\n| Ejercicio 2 |")
    num1 = int(input("Ingresá un número entero: "))
    if num1 % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
    
    
def Ejercicio3():
    print("\n| Ejercicio 3 |")
    num_mes = int(input("Ingresá un número de mes (1 - 12): "))
    while num_mes < 1 or num_mes > 12:
        num_mes = int(input("El número que ingresaste no pertenece a ningún mes, por favor, ingresá un número válido del 1 al 12: "))
    if num_mes == 1:
        print(f"El mes N°{num_mes} es Enero.")
    elif num_mes == 2:
        print(f"El mes N°{num_mes} es Febrero.")
    elif num_mes == 3:
        print(f"El mes N°{num_mes} es Marzo.")
    elif num_mes == 4:
        print(f"El mes N°{num_mes} es Abril.")
    elif num_mes == 5:
        print(f"El mes N°{num_mes} es Mayo.")
    elif num_mes == 6:
        print(f"El mes N°{num_mes} es Junio.")
    elif num_mes == 7:
        print(f"El mes N°{num_mes} es Julio.")
    elif num_mes == 8:
        print(f"El mes N°{num_mes} es Agosto.")
    elif num_mes == 9:
        print(f"El mes N°{num_mes} es Septiembre.")
    elif num_mes == 10:
        print(f"El mes N°{num_mes} es Octubre.")
    elif num_mes == 11:
        print(f"El mes N°{num_mes} es Noviembre.")
    elif num_mes == 12:
        print(f"El mes N°{num_mes} es Diciembre.")
    else:
        print("Error no contemplado.")
    

def Ejercicio4():
    print("\n| Ejercicio 4 |")
    print("Evento: en el congreso se está por votar una ley muy importante.")
    votos_a_favor = int(input("Ingresá los votos a favor: "))
    votos_en_contra = int(input("Ahora ingresá los votos en contra: "))
    porcentaje_a_favor = (votos_a_favor / (votos_a_favor + votos_en_contra)) * 100
    porcentaje_en_contra = (votos_en_contra / (votos_a_favor + votos_en_contra)) * 100
    if votos_a_favor > votos_en_contra:
        print(f"La ley fue aprobada con {votos_a_favor} votos a favor, representando el {porcentaje_a_favor}% de los votos.")
    elif votos_en_contra > votos_a_favor:
        print(f"La ley fue rechazada con {votos_en_contra} votos en contra, representando el {porcentaje_en_contra}% de los votos.")
    elif votos_a_favor == votos_en_contra:
        print(f"La ley tiene que ir a revisión, la cantidad de votos a favor y en contra es la misma.")
    else:
        print("Error no contemplado.")
    
    
def Ejercicio5():
    print("\n| Ejercicio 5 |")
    nota_primer_parcial = int(input("Ingresá la nota de tu primer parcial (0 - 10): "))
    while nota_primer_parcial < 0 or nota_primer_parcial > 10:
        nota_primer_parcial = int(input("Por favor, ingresá una nota válida (0 - 10): "))
        
    nota_segundo_parcial = int(input("Ahora ingresá la nota de tu segundo parcial (0 - 10): "))
    while nota_segundo_parcial < 0 or nota_segundo_parcial > 10:
        nota_segundo_parcial = int(input("Por favor, ingresá una nota válida (0 - 10): "))
    
    if nota_primer_parcial >= 7 and nota_segundo_parcial >= 7:
        print("Promocionaste la materia.")
    elif nota_primer_parcial >= 4 and nota_segundo_parcial >= 4:
        print("Aprobaste ambos parciales.")
    elif nota_primer_parcial < 4 or nota_segundo_parcial < 4:
        print("Tenés que recuperar.")
    
    
def Ejercicio6():
    print("\n| Ejercicio 6 |")
    COSTO_BASICO_LIBRO = 5000
    costo_total_libro = 0
    
    print("Una editorial determina el precio de un libro según la cantidad de páginas que contiene.")
    num_paginas = int(input("Ingresá el número de páginas de tu libro: "))
    while num_paginas < 1:
        num_paginas = int(input("Por favor, ingresá un número válido: "))
    
    if num_paginas > 600: # Encuadernación con procedimiento especial: $5000 + $32 por página + $1200 + $3360
        costo_total_libro = COSTO_BASICO_LIBRO + (num_paginas * 32) + 1200 + 3360
    elif num_paginas > 300: # Encuadernación en tela: $5000 + $32 por página + $1200
        costo_total_libro = COSTO_BASICO_LIBRO + (num_paginas * 32) + 1200
    elif num_paginas <= 300: # Encuadernación rústica: $5000 + $32 por página
        costo_total_libro = COSTO_BASICO_LIBRO + (num_paginas * 32)
    
    print(f"El costo de tu libro es de ${costo_total_libro}.")

    
def Ejercicio7():
    print("\n| Ejercicio 7 |")
    print("Calculadora de precios de viajes - Fletero")
    PRECIO_VIAJE_MINIMO = 2700
    precio_viaje = 0
    
    kilometros = float(input("Ingresá la cantidad de kilómetros recorridos: "))
    while kilometros <= 0:
        kilometros = float(input("Por favor, ingresá una cantidad de kilómetros válida: "))

    if kilometros > 0 and kilometros < 10:
        precio_viaje = kilometros * 400
    elif kilometros >= 10:
        precio_viaje = kilometros * 200
    else:
        print("Error no contemplado.")

    if precio_viaje < PRECIO_VIAJE_MINIMO:
        precio_viaje = 2700

    print(f"El precio del viaje es de ${precio_viaje}.")


def Ejercicio8():
    print("\n| Ejercicio 8 |")

def Ejercicio9():
    print("\n| Ejercicio 9 |")
    
def Ejercicio10():
    print("\n| Ejercicio 10 |")

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
    elif ejercicioSeleccionado == 7:
        Ejercicio7()
    elif ejercicioSeleccionado == 8:
        Ejercicio8()
    elif ejercicioSeleccionado == 9:
        Ejercicio9()
    elif ejercicioSeleccionado == 10:
        Ejercicio10()
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 14 o '0' para salir del programa: ")