# Introducción a la Algoritmia - Clase 2

def Ejercicio1():
    print("\n| Ejercicio 1 |")
    cantidad_horas = int(input("Ingresá la cantidad de horas trabajadas: "))
    tarifa = int(input("Ingresá la tarifa por hora: "))
    sueldo = cantidad_horas * tarifa
    print("Tu sueldo correspondiente es: " + str(sueldo))


def Ejercicio2():
    print("\n| Ejercicio 2 |")
    num1 = int(input("Ingresá el primer número: "))
    num2 = int(input("Ingresá el segundo número: "))
    num3 = int(input("Ingresá el tercer número: "))
    promedio = (num1 + num2 + num3) / 3
    print("El promedio de los números ingresados es: ", promedio)


def Ejercicio3():
    print("\n| Ejercicio 3 |")
    IVA = 0.21
    precioProducto = float(input("Ingresá el precio del producto: "))
    costoIVA = precioProducto * IVA
    print("El IVA del producto es de: ", costoIVA)


def Ejercicio4():
    print("\n| Ejercicio 4 |")
    baseRectangulo = float(input("Ingresá la base del rectángulo: "))
    alturaRectangulo = float(input("Ingresá la altura del rectángulo: "))
    superficieRectangulo = baseRectangulo * alturaRectangulo
    print("La superficie del rectángulo es de: ", superficieRectangulo, "m2")


def Ejercicio5():
    print("\n| Ejercicio 5 |")
    numA = int(input("Ingresá el primer número A: "))
    numB = int(input("Ingresá el segundo número B: "))
    sumaNums = numA + numB
    restaNums = numA - numB
    print("La suma de ambos números es de:", sumaNums, "y la resta es de:", restaNums)


def Ejercicio6():
    print("\n| Ejercicio 6 |")
    num1 = float(input("Ingresá la nota del primer parcial: "))
    num2 = float(input("Ingresá la nota del segundo parcial: "))
    promedio_notas = (num1 + num2) / 2
    print("El promedio de tus notas es de:", promedio_notas)


def Ejercicio7():
    print("\n| Ejercicio 7 |")
    edadPersona = int(input("Ingresá tu edad: "))
    conversion_a_dias = edadPersona * 365
    print("En la fecha de tu último cumpleaños, tenías exactamente", conversion_a_dias, "días de vida.")


def Ejercicio8():
    print("\n| Ejercicio 8 |")
    precioMedicamento = float(input("Ingresá el precio original del medicamento: "))
    MONTO_DESCUENTO = 0.35
    descuento = precioMedicamento * MONTO_DESCUENTO
    importeFinal = precioMedicamento - descuento
    print("El precio final del medicamento con un descuento del 35% es de: $", importeFinal)


def Ejercicio9():
    print("\n| Ejercicio 9 |")
    aportePersona1 = float(input("Ingresá la cantidad de dinero que va a aportar la primera persona: "))
    aportePersona2 = float(input("Ahora la segunda persona: "))
    aportePersona3 = float(input("Y por último, la tercera persona: "))
    sumaAportes = aportePersona1 + aportePersona2 + aportePersona3
    porcentajePersona1 = (aportePersona1 / sumaAportes) * 100
    porcentajePersona2 = (aportePersona2 / sumaAportes) * 100
    porcentajePersona3 = (aportePersona3 / sumaAportes) * 100
    print("El porcentaje de aporte de la primera persona es del: ", porcentajePersona1, "%")
    print("De la segunda persona es del: ", porcentajePersona2, "%")
    print("Y de la tercera persona es del: ", porcentajePersona3, "%")


def Ejercicio10():
    print("\n| Ejercicio 10 |")
    medida_metros = float(input("Ingresá una medida en metros: "))
    medida_centimetros = medida_metros * 100
    medida_pulgadas = medida_centimetros / 2.54
    medida_pies = medida_pulgadas / 12
    medida_yardas = medida_pies / 3
    print("La medida en centímetros es:", medida_centimetros)
    print("La medida en pulgadas es:", medida_pulgadas)
    print("La medida en pies es:", medida_pies)
    print("La medida en yardas es:", medida_yardas)

    
def Ejercicio11():
    print("\n| Ejercicio 11 |")
    vendedor = int(input("Ingresá el número del vendedor: "))
    cantidad_ventas = int(input("Ingresá la cantidad de ventas realizadas: "))
    valor_ventas = float(input("Ingresá el valor total de las ventas: "))
    salario_base = 250000
    comision_por_venta = 50000
    porcentaje_comision = 0.05
    comision_total = comision_por_venta * cantidad_ventas + porcentaje_comision * valor_ventas
    salario_total = salario_base + comision_total
    print("Número del vendedor:", vendedor)
    print("Salario correspondiente:", salario_total)


def Ejercicio12():
    print("\n| Ejercicio 12 |")
    largoParcela = int(input("Ingresá el largo de la parcela agrícola en metros: "))
    anchoParcela = int(input("Ingresá el ancho de la parcela en metros: "))
    superficieParcela = largoParcela * anchoParcela
    cantidad_quintales = superficieParcela / 10 * 2
    print("La cantidad de quintales de trigo que se pueden producir en la parcela es de: ", cantidad_quintales)

    
def Ejercicio13():
    print("\n| Ejercicio 13 |")
    periodo_en_segundos = int(input("Ingresá un período de tiempo en segundos: "))
    periodo_en_dias = periodo_en_segundos // 86400
    periodo_en_segundos %= 86400
    periodo_en_horas = periodo_en_segundos // 3600
    periodo_en_segundos %= 3600
    periodo_en_minutos = periodo_en_segundos // 60
    periodo_en_segundos %= 60
    print(f"El período de tiempo ingresado equivale a: {periodo_en_dias} días, {periodo_en_horas} horas, {periodo_en_minutos} minutos y {periodo_en_segundos} segundos.")

    
def Ejercicio14():
    print("\n| Ejercicio 14 |")
    monto_dinero = int(input("Ingresá un monto de dinero en pesos: "))
    cant_billetes_mil = monto_dinero // 1000
    monto_dinero %= 1000
    cant_billetes_quinientos = monto_dinero // 500
    monto_dinero %= 500
    cant_billetes_cien = monto_dinero // 100
    monto_dinero %= 100
    cant_billetes_cincuenta = monto_dinero // 50
    monto_dinero %= 50
    cant_billetes_diez = monto_dinero // 10
    monto_dinero %= 10
    cant_billetes_cinco = monto_dinero // 5
    monto_dinero %= 5
    cant_billetes_uno = monto_dinero // 1
    print("El cajero automático tendrá que entregar los siguientes billetes:")
    print(f"• {cant_billetes_mil} de mil")
    print(f"• {cant_billetes_quinientos} de quinientos")
    print(f"• {cant_billetes_cien} de cien")
    print(f"• {cant_billetes_cincuenta} de cincuenta")
    print(f"• {cant_billetes_diez} de diez")
    print(f"• {cant_billetes_cinco} de cinco")
    print(f"• {cant_billetes_uno} de uno")


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
    elif ejercicioSeleccionado == 11:
        Ejercicio11()
    elif ejercicioSeleccionado == 12:
        Ejercicio12()
    elif ejercicioSeleccionado == 13:
        Ejercicio13()
    elif ejercicioSeleccionado == 14:
        Ejercicio14()
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 14 o '0' para salir del programa: ")