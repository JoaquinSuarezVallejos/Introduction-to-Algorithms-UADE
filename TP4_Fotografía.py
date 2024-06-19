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
# fotografías mínimas por evento es de 30 y como máximo son 500. El costo de cada foto
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
# Tener en cuenta las restricciones del enunciado para determinar las cantidades correctas al realizar esta generación de datos.

# -----------------------------------------------------------------------------------------------------------------------------------

import random

# | FUNCIONES | 
def Opcion1(eventos): # Facturación del mes, costos y cantidad de eventos.
    total_facturacion = 0
    total_costos = 0
    total_eventos = 0

    for evento in eventos:
        total_facturacion += evento["facturacion"]
        total_costos += evento["costo"]
        total_eventos += 1

    print(f"Total de facturación del mes: ${total_facturacion}")
    print(f"Total de costos del mes: ${total_costos}")
    print(f"Cantidad de eventos realizados: {total_eventos}")


def Opcion2(eventos): # Facturación por tipo de evento, costo y cantidad de eventos ordenado por facturación.
    print("")


# Código principal
flag = True
while flag:
    print("Bienvenido/a al programa de gestión de tu empresa de fotografía. ¿Qué opción deseás seleccionar?")
    print("\nOpción 1: Ver el total de facturación, costos y cantidad de eventos")
    print("Opción 2: Ver el total de facturación por tipo de evento, costos y cantidad de eventos ordenado por facturación")
    print("Opción 3: Ver el listado completo detallado del total facturado de cada evento")
    print("Opción 4: Filtrar por tipo de evento")
    opcion_elegida = input("")
    if opcion_elegida == 0:
        flag = False
