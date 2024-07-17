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
# |CUMPLEAÑOS:	 |  |          $650	                 |  |              $550	              |  |               $500	            |  |        $35000          |
# |BAUTISMOS:    |  |          $750	                 |  |              $650	              |  |               $600	            |  |        $38000          |
# |OTROS:	     |  |          $1000	             |  |              $900	              |  |               $800	            |  |        $25000          |

# (*) El costo es fijo por tipo de evento, en el mismo está incluido la cantidad de
# empleados y el tipo de equipamiento que se tienen que ocupar por cada uno.

# Además, se sabe que, por la capacidad de la empresa, lo máximo que pueden realizar
# por mes son hasta 80 eventos, pero el mínimo es siempre 30. También, la cantidad de
# fotografías mínimas por evento es de 30 y como máximo son 500. 

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
# Tener en cuenta las restricciones del enunciado para determinar las cantidades correctas al realizar esta generación de datos.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# | IMPORTACIÓN |
from random import randint


# | VARIABLES y CONSTANTES |
TIPO_EVENTO = ["CASAMIENTO", "15 AÑOS", "CUMPLEAÑOS", "BAUTISMOS", "OTROS"] # Lista: tipo de evento.
COSTO_TIPO_EVENTO = [50000, 60000, 35000, 38000, 25000] # Lista: costo por tipo de evento.
PRECIOS_FOTOS_EVENTO = [ # Matriz: precios de fotos por tipo de evento.
    # [0] Precio por unidad hasta 50 fotos, [1] Precio por unidad más de 50 fotos, [2] Precio por unidad más de 100 fotos.
    [750, 650, 600], # CASAMIENTO
    [850, 750, 700], # 15 AÑOS
    [650, 550, 500], # CUMPLEAÑOS
    [750, 650, 600], # BAUTISMOS
    [1000, 900, 800] # OTROS
]

eventos_del_mes = [] # Matriz: eventos realizados en el mes

# Variables totales
cantidad_eventos = 0
facturacion_total = 0
costo_total = 0

# Variables por evento
facturacion_evento = 0
costo_evento = 0


# | FUNCIONES | 
def MenuPrincipal():
    print("\n| MENÚ PRINCIPAL |") # Mostramos el menú
    print("- Junio de 2024 -")
    print("OPCIÓN 1: Ver el total de facturación y de benificio neto, los costos y la cantidad de eventos.")
    print("OPCIÓN 2: Ver el total de facturación y de beneficio neto por tipo de evento, los costos y la cantidad de eventos.")
    print("OPCIÓN 3: Ver el listado completo detallado del total facturado de cada evento realizado.")
    print("OPCIÓN 4: Seleccionar un tipo de evento y ver el detalle de facturación y la cantidad de fotos de cada evento de ese tipo.")
    print("OPCIÓN 5: Salir.")
    
    flag = False
    
    while flag == False: # Pedimos input para que se seleccione una opción
        try:
            opcion_elegida = int(input("\n> Por favor, ingresá el número de la opción que querés seleccionar (1-5): "))
            if opcion_elegida < 1 or opcion_elegida > 5:
                print("Respuesta inválida.")
            else:
                flag = True # El número es válido, sale del bucle
        except ValueError:
            print("Respuesta inválida.")
    
    if opcion_elegida == 1: # Ejecutamos la opción según el input
        Opcion1()
    elif opcion_elegida == 2:
        Opcion2()
    elif opcion_elegida == 3:
        Opcion3()
    elif opcion_elegida == 4:
        Opcion4()
    elif opcion_elegida == 5:
        finalizarPrograma()
    else:
        error()
        

def Opcion1(): # Total de la facturación del mes, los costos y cuantos eventos fueron
    print("\n| OPCIÓN 1 |")
    print("- Junio de 2024 -")
    print("Total de facturación y de beneficio neto, costos y cantidad de eventos.")
    
    print(f"\nCantidad de eventos: {cantidad_eventos}")
    print(f"Facturación total: ${facturacion_total}")
    print(f"Costos totales: ${costo_total}")
    print(f"Beneficio neto: ${facturacion_total - costo_total}")
    
    volver_al_menu_principal()
    
        
def Opcion2(): # Total de facturación por tipo de evento, el costo y la cantidad de eventos ordenado por facturación
    print("\n| OPCIÓN 2 |")
    print("- Junio de 2024 -")
    print("Total de facturación y de beneficio neto por tipo de evento, costos y cantidad de eventos. Orden descendente por facturación.")
    print("")
    
    # Crear una lista con la información de cada tipo de evento
    eventos_por_tipo = []
    for i in range(len(TIPO_EVENTO)):
        tipo_evento = TIPO_EVENTO[i] # Seleccionamos tipo de evento 
        cantidad_eventos_x_tipo = 0 # Asignamos valores a 0 por cada iteración de tipo de evento
        facturacion_x_tipo = 0
        costos_x_tipo = 0
        for evento in eventos_del_mes:
            if evento[0] == tipo_evento: # Verificamos que el tipo de evento sea igual
                cantidad_eventos_x_tipo += 1 # Contador del tipo de evento
                facturacion_x_tipo += evento[2] # Sumamos la facturación
                costos_x_tipo += evento[3] # Sumamos el costo
        eventos_por_tipo.append([tipo_evento, cantidad_eventos_x_tipo, facturacion_x_tipo, costos_x_tipo])
        
    ordenar_eventos_por_facturacion(eventos_por_tipo)
      
    # Imprimir la información de cada tipo de evento
    contadorEvento = 1
    for evento in eventos_por_tipo: # Mostramos eventos ennumerados
        print(f"{contadorEvento}. Tipo de evento: {evento[0]} | Cantidad de eventos: {evento[1]} | Facturación total: ${evento[2]} | Costos totales: ${evento[3]} | Beneficio neto: ${evento[2] - evento[3]}")
        contadorEvento += 1
        
    volver_al_menu_principal()
    

def Opcion3(): # Listado completo detallado del total facturado de cada evento con su tipo, ordenado por total facturado
    print("\n| OPCIÓN 3 |")
    print("- Junio de 2024 -")
    print("Listado completo detallado del total facturado de cada evento con su tipo. Orden descendente por facturación.")
    print("")
        
    listado_todos_los_eventos = []
    for evento in eventos_del_mes: # Asignamos todos los eventos del mes
        listado_todos_los_eventos.append(evento)
        
    ordenar_eventos_por_facturacion(listado_todos_los_eventos)
    
    contadorEvento = 1
    for evento in listado_todos_los_eventos: # Mostramos eventos ennumerados       
        print(f"{contadorEvento}. Tipo de evento: {evento[0]} | Facturación total: ${evento[2]}")
        contadorEvento += 1
        
    volver_al_menu_principal()

    
def Opcion4(): # Seleccionar un tipo de evento y que se detallen la facturación y cantidad de fotos de cada uno de los eventos de ese tipo
    print("\n| OPCIÓN 4 |")
    print("- Junio de 2024 -")
    print("\n1: CASAMIENTO | 2: 15 AÑOS | 3: CUMPLEAÑOS | 4: BAUTISMOS | 5: OTROS")
    
    flag = False
    
    while flag == False:
        try:
            num_evento = int(input("Seleccioná un tipo de evento (1-5) para ver el detalle de facturación (orden descendente) y la cantidad de fotos de cada evento de ese tipo: "))
            if num_evento < 1 or num_evento > 5:
                print("Respuesta inválida.")
            else:
                flag = True # El número es válido, sale del bucle
        except ValueError:
            print("Respuesta inválida.")
    # Se selecciona el tipo de evento que elige el usuario
    if num_evento == 1:
        tipo_evento = "CASAMIENTO"
    elif num_evento == 2:
        tipo_evento = "15 AÑOS"
    elif num_evento == 3:
        tipo_evento = "CUMPLEAÑOS"
    elif num_evento == 4:
        tipo_evento = "BAUTISMOS"
    elif num_evento == 5:
        tipo_evento = "OTROS"
    else:
        error()
    
    eventos_por_tipo = [] # Se genera una matriz según el tipo de evento seleccionado
    for evento in eventos_del_mes:
        if evento[0] == tipo_evento:
            eventos_por_tipo.append(evento)
            
    ordenar_eventos_por_facturacion(eventos_por_tipo)
    
    contadorEvento = 1
    for evento in eventos_por_tipo: # Mostramos eventos ennumerados
        print(f"{contadorEvento}. Tipo de evento: {evento[0]} | Cantidad de fotos: {evento[1]} | Facturación total: ${evento[2]}")
        contadorEvento += 1
    
    volver_al_menu_principal()
    
    
def ordenar_eventos_por_facturacion(lista_eventos):
    # Ordenar la lista de eventos por facturación de mayor a menor (Bubble Sort)
    for i in range(len(lista_eventos)):
        for j in range(i+1, len(lista_eventos)):
            if lista_eventos[i][2] < lista_eventos[j][2]:
                lista_eventos[i], lista_eventos[j] = lista_eventos[j], lista_eventos[i]
    return lista_eventos
    
    
def volver_al_menu_principal():
    flag = False
    
    while flag == False:
        volver_al_menu_principal = str(input("\n> ¿Querés volver al menú principal? (Sí: y / No: n): "))
        volver_al_menu_principal.lower() # Forzamos la minúscula
    
        if volver_al_menu_principal == "y" or volver_al_menu_principal == "yes" or volver_al_menu_principal == "n" or volver_al_menu_principal == "no": # Verificamos la respuesta
            flag = True
        else:
            print("Respuesta inválida.")
            
    if volver_al_menu_principal == "y" or volver_al_menu_principal == "yes": 
        MenuPrincipal()
    elif volver_al_menu_principal == "n" or volver_al_menu_principal == "no": 
        finalizarPrograma()
    else:
        error()
        
        
def finalizarPrograma():
    print("Programa finalizado. ¡Hasta luego!")
    exit() # Finaliza el programa
        
        
def error():
    print("Ha ocurrido un error inesperado.")
    exit() # Finaliza el programa


# | GENERACIÓN DE DATOS |
cantidad_eventos = randint(30, 80) # Cantidad de eventos generados al azar, considerando el mínimo y el máximo del enunciado.
for evento in range(cantidad_eventos):
    tipo_evento = TIPO_EVENTO[randint(0, 4)] # Se le asigna un tipo de evento.
    cantidad_fotos = randint(30, 500) # Cantidad de fotos generada al azar, considerando el mínimo y el máximo del enunciado.
    
    if cantidad_fotos <= 50: # Precio por unidad hasta 50 fotos
        if tipo_evento == "CASAMIENTO":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[0][0]
        elif tipo_evento == "15 AÑOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[1][0]
        elif tipo_evento == "CUMPLEAÑOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[2][0]
        elif tipo_evento == "BAUTISMOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[3][0]
        elif tipo_evento == "OTROS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[4][0]
        else:
            error()
    elif cantidad_fotos > 50 and cantidad_fotos <= 100: # Precio por unidad más de 50 fotos, hasta 100 fotos
        if tipo_evento == "CASAMIENTO":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[0][1]
        elif tipo_evento == "15 AÑOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[1][1]
        elif tipo_evento == "CUMPLEAÑOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[2][1]
        elif tipo_evento == "BAUTISMOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[3][1]
        elif tipo_evento == "OTROS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[4][1]
        else:
            error()
    elif cantidad_fotos > 100: # Precio por unidad más de 100 fotos
        if tipo_evento == "CASAMIENTO":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[0][2]
        elif tipo_evento == "15 AÑOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[1][2]
        elif tipo_evento == "CUMPLEAÑOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[2][2]
        elif tipo_evento == "BAUTISMOS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[3][2]
        elif tipo_evento == "OTROS":
            facturacion_evento = cantidad_fotos * PRECIOS_FOTOS_EVENTO[4][2]
        else:
            error()
    else:
        error()
        
    if tipo_evento == "CASAMIENTO": # Asignamos el costo según el tipo
        costo_evento = COSTO_TIPO_EVENTO[0]
    elif tipo_evento == "15 AÑOS":
        costo_evento = COSTO_TIPO_EVENTO[1]
    elif tipo_evento == "CUMPLEAÑOS":
        costo_evento = COSTO_TIPO_EVENTO[2]
    elif tipo_evento == "BAUTISMOS":
        costo_evento = COSTO_TIPO_EVENTO[3]
    elif tipo_evento == "OTROS":
        costo_evento = COSTO_TIPO_EVENTO[4]
        
    costo_total += costo_evento # Sumamos el costo de evento por cada evento
    
    facturacion_evento += costo_evento # Agregamos el costo del evento a la facturación
    facturacion_total += facturacion_evento
    
    eventos_del_mes.append([tipo_evento, cantidad_fotos, facturacion_evento, costo_evento])
    
    
# | PROGRAMA PRINCIPAL |
print("\nBienvenido/a al programa de gestión de tu empresa de fotografía.")
MenuPrincipal()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------