# Introducción a la Algoritmia - Clase 5

def Ejercicio1():
    print("\n| Ejercicio 1 |")
    flag = True
    edadPersona = 0
    cantidad_menores = 0
    cantidad_mayores = 0
    sumaEdades_menores = 0
    sumaEdades_mayores = 0
    promedio_menores = 0
    promedio_mayores = 0
    
    while flag == True:
        edadPersona = int(input("Para finalizar el programa, escribir '-1'. Ingresá la edad de una persona: "))
        if edadPersona == -1:
            flag = False
        elif edadPersona < 0 or edadPersona > 100:
            print("Ingresaste una edad inválida.")
        else:
            if edadPersona < 18:
                cantidad_menores += 1
                sumaEdades_menores += edadPersona
                promedio_menores = sumaEdades_menores / cantidad_menores
            elif edadPersona >= 18:
                cantidad_mayores += 1
                sumaEdades_mayores += edadPersona
                promedio_mayores = sumaEdades_mayores / cantidad_mayores
            else: print("Error desconocido.")
            
    print("")
            
    if cantidad_menores == 0:
        print("No hay menores de edad.")
    else:
        print(f"Hay {cantidad_menores} menores de edad. El promedio de edad de este grupo es de {promedio_menores} años.")
        
    if cantidad_mayores == 0:
        print("No hay mayores de edad.")
    else:
        print(f"Hay {cantidad_mayores} mayores de edad. El promedio de edad de este grupo es de {promedio_mayores} años.")
        

def Ejercicio2():
    print("\n| Ejercicio 2 |")
    numero_de_legajo = 0
    cant_alumnos_aprobados = 0
    cant_alumnos_desaprobados = 0
    cant_alumnos_aplazados = 0
    suma_notas_aprobados = 0
    suma_cant_alumnos = 0
    porcentaje_aprobados = 0
    porcentaje_desaprobados = 0
    porcentaje_aplazados = 0

    while numero_de_legajo != -1:
        numero_de_legajo = int(input("Para finalizar el programa, escribir '-1'. Ingresá un número de legajo de un alumno: "))
        nota_alumno = int(input("Ingresá la nota del alumno: "))
       
        if nota_alumno < 1 or nota_alumno > 10:
            
            if nota_alumno >= 4:
                cant_alumnos_aprobados += 1
                print("El alumno aprobó.")
            elif nota_alumno < 4 and nota_alumno > 1:
                cant_alumnos_desaprobados += 1
                print("El alumno desaprobó.")
            elif nota_alumno == 1:
                cant_alumnos_aplazados += 1
                print("El alumno aplazó.")
            else:
                print("Error no contemplado.")
    
    suma_cant_alumnos = cant_alumnos_aprobados + cant_alumnos_desaprobados + cant_alumnos_aplazados
    porcentaje_aprobados = (cant_alumnos_aprobados / (suma_cant_alumnos)) * 100
    porcentaje_desaprobados = (cant_alumnos_desaprobados / (suma_cant_alumnos)) * 100
    porcentaje_aplazados = (cant_alumnos_aplazados / (suma_cant_alumnos)) * 100

    print(f"La cantidad de alumnos aprobados es de {cant_alumnos_aprobados} y representan el {porcentaje_aprobados}% del total de alumnos.")
    print(f"La cantidad de alumnos desaprobados es de {cant_alumnos_desaprobados} y representan el {porcentaje_desaprobados}% del total de alumnos.")
    print(f"La cantidad de alumnos aplazados es de {cant_alumnos_aplazados} y representan el {porcentaje_aplazados}% del total de alumnos.")


def Ejercicio3():
    print("\n| Ejercicio 3 |")
    ventas_realizadas = 0
    ventas_con_descuento10 = 0
    ventas_solo_precio_base = 0
    precio_base = float(input("Ingresá el precio base del producto: "))
    cantidad_solicitada = int(input("Ingresá la cantidad solicitada (-1 para finalizar): "))

    while cantidad_solicitada != -1:
        ventas_realizadas += 1
        total_venta = 0

        if cantidad_solicitada <= 12:
            total_venta = cantidad_solicitada * precio_base
            ventas_solo_precio_base += 1
        elif cantidad_solicitada <= 100:
            total_venta = 12 * precio_base + (cantidad_solicitada - 12) * precio_base * 0.9
            ventas_con_descuento10 += 1
        else:
            total_venta = 12 * precio_base + 88 * precio_base * 0.9 + (cantidad_solicitada - 100) * precio_base * 0.75

        precio_promedio = total_venta / cantidad_solicitada
        print(f"Valor total de la venta: {total_venta}")
        print(f"Precio promedio por unidad: {precio_promedio}")

        cantidad_solicitada = int(input("Ingresá la cantidad solicitada (-1 para finalizar): "))

    print(f"Cantidad de ventas realizadas total: {ventas_realizadas}")
    print(f"Cantidad de ventas en las que se aplicó un 10% de descuento: {ventas_con_descuento10}")
    print(f"Cantidad de ventas en las que SOLO se aplicó el precio base: {ventas_solo_precio_base}")


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
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 14 o '0' para salir del programa: ")