# TP 4 - Fotografía
# Materia: Introducción a la Algoritmia
# Profesora: Julia Monasterio
# Alumnos: Julián Curi y Joaquín Suárez Vallejos

# ENUNCIADO:
# Una empresa de fotógrafos se dedica a la realización de todas las fotografías en diversos
# tipos de eventos. Todos los meses, tienen que generar la facturación de los eventos del
# mes, el cual se calcula según la cantidad de fotos y el tipo de evento y para ello cuentan
# con la siguiente información:

# Tipo de evento	Precio por unidad hasta 50 fotos	Precio por unidad más de 50 fotos	Precio por unidad más de 100 fotos	Costo tipo de evento (*)				
# CASAMIENTO:	      $750	                                   $650	                                   $600	                          $50000
# 15 AÑOS:	          $850	                                   $750	                                   $700	                          $60000
# CUMPLEAÑOS:	      $650	                                   $550	                                   $550	                          $35000
# BAUTISMOS:          $750	                                   $650	                                   $650	                          $38000
# OTROS:	          $1000	                                   $900	                                   $800	                          $25000

# (*) El costo es fijo por tipo de evento, en el mismo está incluido la cantidad de
# empleados y el tipo de equipamiento que se tienen que ocupar por cada uno.

# Además, se sabe que, por la capacidad de la empresa, lo máximo que pueden realizar
# por mes son hasta 80 eventos, pero el mínimo es siempre 30. También, la cantidad de
# fotografías mínimas por evento es de 50 y como máximo son 500. El costo de cada foto
# sacada es de $50 la unidad, igual para todos los eventos.

# La empresa tiene el detalle de todos los eventos del mes, el tipo de evento y la cantidad de fotos que se sacaron. 
# Necesita que se calcule la facturación de cada uno y poder, de esta forma responder las siguientes necesidades:
# ●	Total de la facturación del mes, los costos y cuantos eventos fueron. (Opción 1)
# ●	Total de facturación por tipo de evento, el costo y la cantidad de eventos ordenado por facturación. (Opción 2)
# ●	Listado completo detallado del total facturado de cada evento con su tipo, ordenado por total facturado. (Opción 3)
# ●	Poder seleccionar un tipo de evento y que se detallen la facturación y cantidad de fotos de cada uno de los eventos de ese tipo. (Opción 4)

# Objetivo:
# Se solicita el desarrollo de un programa, con un menú principal para poder acceder a las opciones detalladas. 
# El programa solo debe terminar cuando el usuario elija la opción del menú correspondiente a SALIR.
# Los datos serán generados por números al azar ya que la carga manual se complejiza para la ejecución. 
# Tener en cuenta las restricciones del enunciado para determinar las cantidades correctas al realizar esta generación de datos.z

# -----------------------------------------------------------------------------------------------------------------------------------

# | IMPORTS | 
from random import randint


# | FUNCIONES | 
def Opcion1(): # Facturación del mes, costos y cantidad de eventos.
    print("Soy la Opción 1.")
    
    # Código de la función
    
    volver_a_menu_principal()
        
def Opcion2(): # Facturación por tipo de evento, costo y cantidad de eventos ordenado por facturación.
    print("Soy la Opción 2.")
    
    # Código de la función
    
    volver_a_menu_principal()

def Opcion3():
    print("Soy la Opción 3.")
    
    # Código de la función
    
    volver_a_menu_principal()
    
def Opcion4():
    print("Soy la Opción 4.")
    
    # Código de la función
    
    volver_a_menu_principal()
    
def volver_a_menu_principal():
    volver_a_menu_principal = str(input("\n¿Deseás volver al menú principal? (Sí: y / No: n): "))
    volver_a_menu_principal.lower()
    if volver_a_menu_principal == "y" or volver_a_menu_principal == "yes": 
        return
    else: 
        print("¡Gracias por utilizar el programa! ¡Hasta luego!")
        exit()


# | VARIABLES | 
flag = True
matriz_tabla_eventos = [
    ["CASAMIENTO", 750, 650, 600, 50000],
    ["15 AÑOS", 850, 750, 700, 60000],
    ["CUMPLEAÑOS", 650, 550, 550, 35000],
    ["BAUTISMOS", 750, 650, 650, 38000],
    ["OTROS", 1000, 900, 800, 25000]
]
eventos = []


# | MENÚ PRINCIPAL | 
print("Bienvenido/a al programa de gestión de tu empresa de fotografía.")

while flag:
    print("| MENÚ PRINCIPAL |")
    print("¿Qué opción deseás seleccionar?")
    print("\nOpción 1: Ver el total de facturación, costos y cantidad de eventos.")
    print("Opción 2: Ver el total de facturación por tipo de evento, costos y cantidad de eventos ordenado por facturación.")
    print("Opción 3: Ver el listado completo detallado del total facturado de cada evento.")
    print("Opción 4: Filtrar por tipo de evento.")
    print("Opción 5: Salir.")
    try:
        opcion_elegida = int(input("Ingresá una opción del 1 al 5: "))
    except ValueError:
        opcion_elegida = int(input("Por favor, ingresá una opción válida del 1 al 5: "))
        continue
    if opcion_elegida == 1:
        Opcion1()
    elif opcion_elegida == 2:
        Opcion2()
    elif opcion_elegida == 3:
        Opcion3()
    elif opcion_elegida == 4:
        Opcion4()
    else:
        flag = False
        