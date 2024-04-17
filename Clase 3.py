# Introducción a la Algoritmia - Clase 3
    
# if 0<calificacion>100:  ---- Estructura in-between
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
    num_mes = int(input("Ingresá un número de mes (1 al 12): "))
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
    
    
def Ejercicio7():
    print("\n| Ejercicio 7 |")
    try:
        kilometros = float(input("Ingresá la cantidad de kilómetros recorridos: "))

        if kilometros < 0:
            print("Error: La cantidad de kilómetros no puede ser negativa.")
        
        elif kilometros == 0:
            print("Introducí una cantidad de kilómetros válida.")

        else:
            if kilometros > 0 and kilometros < 10:
                precio = kilometros * 400
            elif kilometros >= 10:
                precio = kilometros * 200
            else:
                print("Error no contemplado.")

            if precio < 2700:
                precio = 2700

        print("El precio del viaje es de: $", precio)
        
    except:
        print("Error: Ingresá un número, no letras o caracteres especiales.")


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
    # elif ejercicioSeleccionado == 4:
    #     Ejercicio4()
    # elif ejercicioSeleccionado == 5:
    #     Ejercicio5()
    # elif ejercicioSeleccionado == 6:
    #     Ejercicio6()
    # elif ejercicioSeleccionado == 7:
    #     Ejercicio7()
    # elif ejercicioSeleccionado == 8:
    #     Ejercicio8()
    # elif ejercicioSeleccionado == 9:
    #     Ejercicio9()
    # elif ejercicioSeleccionado == 10:
    #     Ejercicio10()
    # elif ejercicioSeleccionado == 11:
    #     Ejercicio11()
    # elif ejercicioSeleccionado == 12:
    #     Ejercicio12()
    # elif ejercicioSeleccionado == 13:
    #     Ejercicio13()
    # elif ejercicioSeleccionado == 14:
    #     Ejercicio14()
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 14 o '0' para salir del programa: ")