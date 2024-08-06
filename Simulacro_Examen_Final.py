# Simulacro de Examen Final

# Título: Gestión de Aspirantes en una Academia Deportiva Multidisciplinaria

# Descripción:

# Se te solicita desarrollar un programa en Python para administrar la información de los aspirantes 
# a una academia deportiva que ofrece cuatro disciplinas: fútbol, natación, voleibol y handball. El programa deberá realizar las siguientes tareas:

# Generación de Datos: 

# Permitir al usuario ingresar la cantidad de aspirantes (entre 100 y 500). CHECK
# Generar aleatoriamente los datos de cada aspirante, incluyendo: CHECK
# DNI (número entero aleatorio entre 400.000 y 60.000.000). CHECK
# Edad (número entero aleatorio entre 12 y 80). CHECK
# Deporte de interés (número entero aleatorio entre 1 y 4, donde 1 representa fútbol, 2 natación, 3 voleibol y 4 handball). CHECK

# Clasificación por Deporte:

# Crear listas separadas para cada deporte, almacenando los DNIs de los aspirantes según su elección. CHECK
# Imprimir en pantalla los DNIs de los aspirantes de cada deporte. CHECK

# Resumen por Deporte:

# Calcular e imprimir un resumen ordenado descendentemente por la cantidad de aspirantes en cada deporte, incluyendo: CHECK
# Nombre del deporte. CHECK
# Cantidad de aspirantes. CHECK
# Promedio de edad de los aspirantes. CHECK


# | IMPORTACIÓN |
from random import randint


# | VARIABLES GLOBALES |
# Listas:
DNIs_aspirantes = []
edades_aspirantes = []
deportes_aspirantes = []
lista_futbol = [] # Deporte N°1
lista_natacion = [] # Deporte N°2
lista_voleibol = [] # Deporte N°3
lista_handball = [] # Deporte N°4


# | FUNCIONES |
def cargar_cantidad_aspirantes(): # El usuario carga la cantidad de aspirantes manualmente por consola
    cantidad_aspirantes = int(input("\n> Ingresá la cantidad de aspirantes de la academia (entre 100 y 500): "))
    
    while cantidad_aspirantes < 100 or cantidad_aspirantes > 500:
        cantidad_aspirantes = int(input("\n> Por favor, ingresá un número válido entre 100 y 500: "))
    
    return cantidad_aspirantes
    
    
def generar_datos_aspirantes(cantidad_aspirantes): # Se generan todos los datos de los aspirantes de forma aleatoria
    for _ in range(cantidad_aspirantes):
        DNIs_aspirantes.append(randint(400000, 60000000))
        edades_aspirantes.append(randint(12, 80))
        deportes_aspirantes.append(randint(1, 4))
    return DNIs_aspirantes, edades_aspirantes, deportes_aspirantes
    
    
def clasificar_aspirantes_por_deporte(): # Clasifica a cada aspirante según la elección del deporte en 1 de 4 listas: fútbol (1), natación (2), voleibol (3) o handball (4).
    for i in range(len(DNIs_aspirantes)):
        if deportes_aspirantes[i] == 1: # Fútbol
            lista_futbol.append(DNIs_aspirantes[i])
        elif deportes_aspirantes[i] == 2: # Natación
            lista_natacion.append(DNIs_aspirantes[i])
        elif deportes_aspirantes[i] == 3: # Voleibol
            lista_voleibol.append(DNIs_aspirantes[i])
        else: # Handball
            lista_handball.append(DNIs_aspirantes[i])
    return lista_futbol, lista_natacion, lista_voleibol, lista_handball


def generar_promedio_edad_por_deporte(): # Genera el promedio de edad de los aspirantes por deporte
    suma_edades_futbol = 0
    suma_edades_natacion = 0
    suma_edades_voleibol = 0
    suma_edades_handball = 0
    
    for i in range(len(edades_aspirantes)):
        if deportes_aspirantes[i] == 1:
            suma_edades_futbol += edades_aspirantes[i]
        elif deportes_aspirantes[i] == 2:
            suma_edades_natacion += edades_aspirantes[i]
        elif deportes_aspirantes[i] == 3:
            suma_edades_voleibol += edades_aspirantes[i]
        else:
            suma_edades_handball += edades_aspirantes[i]
    
    edad_promedio_futbol = suma_edades_futbol / len(lista_futbol)
    edad_promedio_natacion = suma_edades_natacion / len(lista_natacion)
    edad_promedio_voleibol = suma_edades_voleibol / len(lista_voleibol)
    edad_promedio_handball = suma_edades_handball / len(lista_handball)
        
    return edad_promedio_futbol, edad_promedio_natacion, edad_promedio_voleibol, edad_promedio_handball
    

def generar_resumen_por_deporte(): # Genera un resumen ordenado de forma descendente por la cantidad de aspirantes en cada deporte y sus edades promedio
    lista_cant_aspirantes_x_deporte = []
    lista_cant_aspirantes_x_deporte.append(len(lista_futbol))
    lista_cant_aspirantes_x_deporte.append(len(lista_natacion))
    lista_cant_aspirantes_x_deporte.append(len(lista_voleibol))
    lista_cant_aspirantes_x_deporte.append(len(lista_handball))
    
    index_deportes = [1, 2, 3, 4]
    
    for i in range(len(lista_cant_aspirantes_x_deporte)): # Ordeno la lista de forma descendente (mayor a menor) con el método Bubble Sort
        for j in range(len(lista_cant_aspirantes_x_deporte)-i-1):
            if lista_cant_aspirantes_x_deporte[j] < lista_cant_aspirantes_x_deporte[j+1]:
                lista_cant_aspirantes_x_deporte[j], lista_cant_aspirantes_x_deporte[j+1] = lista_cant_aspirantes_x_deporte[j+1], lista_cant_aspirantes_x_deporte[j]
                index_deportes[j], index_deportes[j+1] = index_deportes[j+1], index_deportes[j]
                
    edad_promedio_futbol, edad_promedio_natacion, edad_promedio_voleibol, edad_promedio_handball = generar_promedio_edad_por_deporte()
    
    print("\n| RESUMEN POR DEPORTE (orden descendente por cantidad de aspirantes) |")
    for i in range(4):
        if index_deportes[i] == 1:
            print(f"• #{i+1}: La cantidad de aspirantes de la academia de fútbol es de {lista_cant_aspirantes_x_deporte[i]}, y la edad promedio es de {edad_promedio_futbol}")
        elif index_deportes[i] == 2:
            print(f"• #{i+1}: La cantidad de aspirantes de la academia de natación es de {lista_cant_aspirantes_x_deporte[i]} y la edad promedio es de {edad_promedio_natacion}")
        elif index_deportes[i] == 3:
            print(f"• #{i+1}: La cantidad de aspirantes de la academia de voleibol es de {lista_cant_aspirantes_x_deporte[i]} y la edad promedio es de {edad_promedio_voleibol}")
        else:
            print(f"• #{i+1}: La cantidad de aspirantes de la academia de handball es de {lista_cant_aspirantes_x_deporte[i]} y la edad promedio es de {edad_promedio_handball}")
    

def main(): # Función principal del programa
    print("- Bienvenido/a al Sistema de Gestión de Aspirantes de la Academia de Buenos Aires -")
    
    cant_aspirantes = cargar_cantidad_aspirantes() # 1
    generar_datos_aspirantes(cant_aspirantes) # 2
    
    clasificar_aspirantes_por_deporte() # 3
    print("\n• DNIs de los aspirantes de cada deporte: ")
    
    print("\n| FÚTBOL |")
    print(f"DNIs: {lista_futbol}")
    
    print("\n| NATACIÓN |")
    print(f"DNIs: {lista_natacion}")
    
    print("\n| VOLEIBOL |")
    print(f"DNIs: {lista_voleibol}")
    
    print("\n| HANDBALL |")
    print(f"DNIs: {lista_handball}")
    
    generar_resumen_por_deporte()
    
    
# | MAIN |
if __name__ == "__main__":
    main() # Ejecuta la función main()