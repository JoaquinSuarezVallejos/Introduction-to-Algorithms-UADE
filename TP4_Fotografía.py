# TP 4 - FOTOGRAFÍA
# Materia: Introducción a la Algoritmia
# Profesora: Julia Monasterio
# Alumnos: Julián Curi y Joaquín Suárez Vallejos

# ENUNCIADO:
# Una empresa de fotógrafos se dedica a la realización de todas las fotografías en diversos
# tipos de eventos. Todos los meses, tienen que generar la facturación de los eventos del
# mes, el cual se calcula según la cantidad de fotos y el tipo de evento y para ello cuentan
# con la siguiente información:

# |Tipo de evento|	|Precio por unidad hasta 50 fotos|	|Precio por unidad más de 50 fotos|	 |Precio por unidad más de 100 fotos|  |Costo tipo de evento (*)|				
# |CASAMIENTO:	 |  |          $750	                 |  |              $650	              |  |               $600	            |  |        $50000          |
# |15 AÑOS:	     |  |          $850	                 |  |              $750	              |  |               $700	            |  |        $60000          |
# |CUMPLEAÑOS:	 |  |          $650	                 |  |              $550	              |  |               $550	            |  |        $35000          |
# |BAUTISMOS:    |  |          $750	                 |  |              $650	              |  |               $650	            |  |        $38000          |
# |OTROS:	     |  |          $1000	             |  |              $900	              |  |               $800	            |  |        $25000          |

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

# OBJETIVO:
# Se solicita el desarrollo de un programa, con un menú principal para poder acceder a las opciones detalladas. 
# El programa solo debe terminar cuando el usuario elija la opción del menú correspondiente a SALIR.
# Los datos serán generados por números al azar ya que la carga manual se complejiza para la ejecución. 
# Tener en cuenta las restricciones del enunciado para determinar las cantidades correctas al realizar esta generación de datos.z

# -----------------------------------------------------------------------------------------------------------------------------------

# | IMPORTACIÓN |
from random import randint


# | VARIABLES |
eventos = []
tipos_evento = ["CASAMIENTO", "15 AÑOS", "CUMPLEAÑOS", "BAUTISMOS", "OTROS"]
cantidad_eventos = randint(30, 80) # Cantidad de eventos generados al azar.
total_facturacion = 0
costos = 0
cantidad_fotos = 0


# | GENERACIÓN DE DATOS |
for i in range(cantidad_eventos):
    evento = {}
    evento["tipo_evento"] = tipos_evento[randint(0, 4)]
    evento["cantidad_fotos"] = randint(50, 500)
    eventos.append(evento)
    cantidad_fotos += evento["cantidad_fotos"]
    
    if evento["cantidad_fotos"] <= 50:
        total_facturacion += evento["cantidad_fotos"] * 50
    elif evento["cantidad_fotos"] > 50 and evento["cantidad_fotos"] <= 100:
        total_facturacion += evento["cantidad_fotos"] * 50
    elif evento["cantidad_fotos"] > 100:
        total_facturacion += evento["cantidad_fotos"] * 50
    else:
        print("Ha ocurrido un error inesperado.")
        exit()
    
    if evento["tipo_evento"] == "CASAMIENTO":
        costos += 50000
    elif evento["tipo_evento"] == "15 AÑOS":
        costos += 60000
    elif evento["tipo_evento"] == "CUMPLEAÑOS":
        costos += 35000
    elif evento["tipo_evento"] == "BAUTISMOS":
        costos += 38000
    elif evento["tipo_evento"] == "OTROS":
        costos += 25000
    else:
        print("Ha ocurrido un error inesperado.")
        exit()


# | FUNCIONES | 
def MenuPrincipal():
    print("\n| MENÚ PRINCIPAL |")
    print("Opción 1: Ver el total de facturación, costos y cantidad de eventos.")
    print("Opción 2: Ver el total de facturación por tipo de evento, costos y cantidad de eventos ordenado por facturación.")
    print("Opción 3: Ver el listado completo detallado del total facturado de cada evento.")
    print("Opción 4: Filtrar por tipo de evento.")
    print("Opción 5: Salir.")
    
    flag = False
    
    while flag == False:
        try:
            opcion_elegida = int(input("\n> Por favor, ingresá el número de la opción que querés seleccionar (1-5): "))
            if opcion_elegida < 1 or opcion_elegida > 5:
                print("Respuesta inválida.")
            else:
                flag = True # El número es válido, sale del bucle.
        except ValueError:
            print("Respuesta inválida.")
    
    if opcion_elegida == 1:
        Opcion1()
    elif opcion_elegida == 2:
        Opcion2()
    elif opcion_elegida == 3:
        Opcion3()
    elif opcion_elegida == 4:
        Opcion4()
    elif opcion_elegida == 5:
        print("Programa finalizado. ¡Hasta luego!")
        exit()
    else:
        print("Ha ocurrido un error inesperado.")
        exit()

def Opcion1(): # Facturación del mes, costos y cantidad de eventos.
    print("Soy la Opción 1.")
    
    # Código de la función
    
    volver_al_menu_principal()
        
def Opcion2(): # Facturación por tipo de evento, costo y cantidad de eventos ordenado por facturación.
    print("Soy la Opción 2.")
    
    # Código de la función
    
    volver_al_menu_principal()

def Opcion3():
    print("Soy la Opción 3.")
    
    # Código de la función
    
    volver_al_menu_principal()
    
def Opcion4():
    print("Soy la Opción 4.")
    
    # Código de la función
    
    volver_al_menu_principal()
    
def volver_al_menu_principal():
    flag = False
    
    while flag == False:
        volver_al_menu_principal = str(input("\n¿Querés volver al menú principal? (Sí: y / No: n): "))
        volver_al_menu_principal.lower()
    
        if volver_al_menu_principal == "y" or volver_al_menu_principal == "yes" or volver_al_menu_principal == "n" or volver_al_menu_principal == "no":
            flag = True
        else:
            print("Respuesta inválida.")
            
    if volver_al_menu_principal == "y" or volver_al_menu_principal == "yes": 
        MenuPrincipal()
    elif volver_al_menu_principal == "n" or volver_al_menu_principal == "no": 
        print("Programa finalizado. ¡Hasta luego!")
        exit()
    else:
        print("Ha ocurrido un error inesperado.")
        exit()


# | PROGRAMA PRINCIPAL |
print("Bienvenido/a al programa de gestión de tu empresa de fotografía.")
MenuPrincipal()