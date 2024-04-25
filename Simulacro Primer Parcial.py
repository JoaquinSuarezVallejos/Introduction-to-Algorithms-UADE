# Introducción a la Algoritmia: Simulacro de Examen

def Ejercicio1():
    print("\nEjercicio 1:")
    print("- Informe de socios de SportClub -")
    cant_total_socios = 0
    cant_socios_sin_antiguedad = 0
    cant_socios_categoria1 = 0 #1 a 12 años de antiguedad
    cant_socios_categoria2 = 0 #13 a 25 años de antiguedad
    cant_socios_categoria3 = 0 #26 años de antiguedad o más
    suma_antiguedad_categoria1 = 0
    suma_antiguedad_categoria2 = 0
    suma_antiguedad_categoria3 = 0
    promedio_antiguedad_categoria1 = 0
    promedio_antiguedad_categoria2 = 0
    promedio_antiguedad_categoria3 = 0
    
    #Usar banderas!!
    # while bandera == True:
    #     ...
    #     ...
    #     if antiguedad_socio == -1:
    #         bandera = False

    antiguedad_socio = int(input("Para finalizar el programa, escribir '-1'. Ingresá la antiguedad (en años) de un socio: "))
    # while antiguedad_socio < 0 and antiguedad_socio != -1:
        #     int(input("Por favor, ingresá una antiguedad válida: "))

    while antiguedad_socio != -1:
        cant_total_socios += 1
    
        if antiguedad_socio >= 1 and antiguedad_socio <= 12:
            cant_socios_categoria1 += 1
            suma_antiguedad_categoria1 += antiguedad_socio
            promedio_antiguedad_categoria1 = suma_antiguedad_categoria1 / cant_socios_categoria1
        elif antiguedad_socio >= 13 and antiguedad_socio <= 25:
            cant_socios_categoria2 += 1
            suma_antiguedad_categoria2 += antiguedad_socio
            promedio_antiguedad_categoria2 = suma_antiguedad_categoria2 / cant_socios_categoria2
        elif antiguedad_socio >= 26:
            cant_socios_categoria3 += 1
            suma_antiguedad_categoria3 += antiguedad_socio
            promedio_antiguedad_categoria3 = suma_antiguedad_categoria3 / cant_socios_categoria3
        else:
            cant_socios_sin_antiguedad += 1
        
        antiguedad_socio = int(input("Para finalizar el programa, escribir '-1'. Ingresá la antiguedad (en años) de un socio: "))
        # while antiguedad_socio < 0 and antiguedad_socio != -1:
        #     int(input("Por favor, ingresá una antiguedad válida: "))

    print(f"La cantidad total de socios del club es de {cant_total_socios}.")
    print(f"La cantidad de socios sin antiguedad es de {cant_socios_sin_antiguedad}.")
    print(f"La cantidad de socios en categoría 1 (entre 1 y 12 años de antiguedad) es de {cant_socios_categoria1}.")
    print(f"En categoría 2 (entre 13 y 25 años de antiguedad) es de {cant_socios_categoria2}.")
    print(f"En categoría 3 (26 años de antiguedad o más) es de {cant_socios_categoria3}.")
    print(f"El promedio de antiguedad de los socios en categoría 1 es de {promedio_antiguedad_categoria1} años.")
    print(f"En categoría 2 es de {promedio_antiguedad_categoria2} años.")
    print(f"En categoría 3 es de {promedio_antiguedad_categoria3} años.")   


def Ejercicio2():
    print("\nEjercicio 2:")
    print("- Informe de chocotortas -")
    
    # Ingredientes para preparar una chocotorta:
    MIN_GALLETITAS_CHOCOLATE = 0.5 #0.5 kilos (500g)
    MIN_DULCE_DE_LECHE = 0.4 #0.4 kilos (400g)
    MIN_QUESO_CREMA = 0.18 #0.18 kilos (180g)
    cant_galletitas_chocolate = 0
    cant_dulce_de_leche = 0
    cant_queso_crema = 0
    contador_chocotortas = 0
    
    cant_galletitas_chocolate = float(input("Ingresá la cantidad disponible (en kilos) de galletitas de chocolate: "))
    while cant_galletitas_chocolate < 0:
        cant_galletitas_chocolate = float(input("Por favor, ingresá una cantidad válida: "))
    cant_dulce_de_leche = float(input("Ahora ingresá la cantidad disponible (en kilos) de dulce de leche: "))
    while cant_dulce_de_leche < 0:
        cant_dulce_de_leche = float(input("Por favor, ingresá una cantidad válida: "))
    cant_queso_crema = float(input("Por último, ingresá la cantidad disponible (en kilos) de queso crema: "))
    while cant_queso_crema < 0:
        cant_queso_crema = float(input("Por favor, ingresá una cantidad válida: "))
    
    if cant_galletitas_chocolate < MIN_GALLETITAS_CHOCOLATE or cant_dulce_de_leche < MIN_DULCE_DE_LECHE or cant_queso_crema < MIN_QUESO_CREMA:
        print("No se puede preparar ninguna chocotorta con las cantidades ingresadas.")
    else:
        while cant_galletitas_chocolate >= MIN_GALLETITAS_CHOCOLATE and cant_dulce_de_leche >= MIN_DULCE_DE_LECHE and cant_queso_crema >= MIN_QUESO_CREMA:
            cant_galletitas_chocolate -= MIN_GALLETITAS_CHOCOLATE
            cant_dulce_de_leche -= MIN_DULCE_DE_LECHE
            cant_queso_crema -= MIN_QUESO_CREMA
            contador_chocotortas += 1

        print(f"Con las cantidades ingresadas, se pueden preparar {contador_chocotortas} chocotortas.")
        if cant_galletitas_chocolate == 0 and cant_dulce_de_leche == 0 and cant_queso_crema == 0:
            print("No sobró ningún ingrediente.")
        else:
            print(f"Sobrarán {cant_galletitas_chocolate} kilos de galletitas de chocolate, {cant_dulce_de_leche} kilos de dulce de leche y {cant_queso_crema} kilos de queso crema.")
    
    
############################################################################################################

xCheck = False

while xCheck == False:
    ejercicioSeleccionado = int(input("\nIngresá el número del ejercicio que querés ejecutar (del 1 al 14) o '0' para salir del programa: "))
    if ejercicioSeleccionado == 1:
        Ejercicio1()
    elif ejercicioSeleccionado == 2:
        Ejercicio2()
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 14 o '0' para salir del programa: ")