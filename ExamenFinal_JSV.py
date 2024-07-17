# Examen Final Regular (17/07/2024) - Introducción a la Algoritmia
# Docente: Julia Monasterio
# Alumno: Joaquín Suárez Vallejos
# Aula: B101
# UADE Sede Belgrano

# TÍTULO: Programa de Becas de un Club

# ENUNCIADO:
# Un club tiene un programa de becas y, entre otras cosas, requiere un programa para poder determinar la 
# cantidad de aspirantes que tienen para ese año. Tener en cuenta que las edades permitidas para 
# las becas son de 13 a 80 años inclusive.

# Se requiere entonces lo siguiente:
# 1. Leer por teclado las edades de los aspirantes. Finaliza la lectura con -1.
# 2. Determinar cuántos aspirantes totales hay. Imprimir por pantalla.
# 3. Determinar cuántos aspirantes fuera del rango de edades intentaron inscribirse. Imprimir por pantalla.
# 4. Imprimir la lista total de las edades, primero en el orden en que fueron cargadas y luego nuevamente,
# ordenada de menor a mayor (ascendente).
# 5. Informar el promedio de edades que se inscribieron (con edades válidas) y luego informar cuántos
# aspirantes se encuentran por encima del promedio y cuántos por debajo.

# Desarrollar el enunciado modularizando el código, es decir, se deben incluir funciones.
# Se debe realizar el código en Python, y tres ejemplos de datos de entrada y datos de salida esperados.

# PROGRAMA: Ejercicio 1

# | FUNCIONES |
def cargar_edades_aspirantes(): # Cargar las edades que ingrese el usuario por consola, diferenciar entre edades válidas e inválidas
    exit_flag = False
    una_edad_cargada = False
    EDAD_MINIMA = 13
    EDAD_MAXIMA = 80
    lista_edades_aspirantes = []
    cant_aspirantes_validos = 0
    cant_aspirantes_invalidos = 0
    
    while exit_flag == False:
        edad_aspirante = int(input("\n> (Finalizar la carga de edades con '-1') Ingresá la edad de un aspirante: "))
        
        if una_edad_cargada == False and edad_aspirante == -1:
            print("- Por favor, cargá al menos una edad antes de finalizar el programa.")
            
        elif edad_aspirante != -1:     
            if edad_aspirante < EDAD_MINIMA or edad_aspirante > EDAD_MAXIMA:
                print("- Lo sentimos, el aspirante está fuera del rango de edad, no fue registrado.")
                cant_aspirantes_invalidos += 1
            else:
                cant_aspirantes_validos += 1
                lista_edades_aspirantes.append(edad_aspirante)
                print("- Aspirante registrado.")
                una_edad_cargada = True
                
        elif edad_aspirante == -1:
            exit_flag = True
            
        else:
            mostrar_error()
            
    return lista_edades_aspirantes, cant_aspirantes_validos, cant_aspirantes_invalidos


def imprimir_cantidades_aspirantes(cant_aspirantes_validos, cant_aspirantes_invalidos): # Imprimir la cantidad total de aspirantes válidos e inválidos
    print(f"\n• La cantidad total de aspirantes válidos que decidieron inscribirse es de {cant_aspirantes_validos}.")
    print(f"\n• Y la cantidad total de aspirantes inválidos que intentaron inscribirse es de {cant_aspirantes_invalidos}.")


def imprimir_lista_edades(lista_edades_aspirantes): # Imprimir la lista de edades en el orden original de carga
    print("\n• La lista de las edades en el orden en que fueron cargadas es la siguiente: ")
    print(f"{lista_edades_aspirantes}")


def ordenar_e_imprimir_lista_edades(lista_edades_aspirantes): # Ordenar e imprimir la lista de edades de menor a mayor (orden ascendente)
    for i in range(len(lista_edades_aspirantes)): # Ordenar por el método Bubble Sort
        for j in range(len(lista_edades_aspirantes)-i-1):
            if lista_edades_aspirantes[j] > lista_edades_aspirantes[j+1]:
                lista_edades_aspirantes[j], lista_edades_aspirantes[j+1] = lista_edades_aspirantes[j+1], lista_edades_aspirantes[j]
                
    lista_ordenada_aspirantes = lista_edades_aspirantes
    
    print("\n• La lista de las edades en orden ascendente (de menor a mayor) es la siguiente: ")
    print(f"{lista_ordenada_aspirantes}")


def informar_edad_promedio(lista_edades_aspirantes): # Informar el promedio de edades que se inscribieron (con edades válidas)
    suma_edades = 0
    
    for i in range(len(lista_edades_aspirantes)):
        suma_edades += lista_edades_aspirantes[i]
        
    edad_promedio = suma_edades / len(lista_edades_aspirantes)
    
    print(f"\n• La edad promedio entre todos los aspirantes es de {edad_promedio} años.")
    
    return edad_promedio


def informar_encima_o_debajo_del_promedio(lista_edades_aspirantes, edad_promedio): # Informar cuántos aspirantes se encuentran por encima del promedio y cuántos por debajo
    aspirantes_encima_promedio = 0
    aspirantes_debajo_promedio = 0
    
    for i in range(len(lista_edades_aspirantes)):
        if lista_edades_aspirantes[i] > edad_promedio:
            aspirantes_encima_promedio += 1
        elif lista_edades_aspirantes[i] < edad_promedio:
            aspirantes_debajo_promedio += 1
        else:
            mostrar_error()
            
    print(f"\n• Hay {aspirantes_encima_promedio} aspirantes que están encima de la edad promedio, y {aspirantes_debajo_promedio} aspirantes que se encuentran por debajo de la edad promedio.")
    print("")

    return aspirantes_encima_promedio, aspirantes_debajo_promedio


def mostrar_error(): # Mostrar un mensaje de error / excepción
    print("\n-! Ha ocurrido un error o una exepción inesperada, el programa ha finalizado.")
    exit()


def main(): # Función principal
    print("\n- Bienvenido/a al Sistema del Programa de Becas del Club Buenos Aires -")
    print("\nIMPORTANTE: Las edades permitidas para las becas son de 13 a 80 años inclusive.")
    lista_edades_aspirantes, cant_aspirantes_validos, cant_aspirantes_invalidos = cargar_edades_aspirantes() # Punto 1
    
    print("\n| INFORME COMPLETO |")
    imprimir_cantidades_aspirantes(cant_aspirantes_validos, cant_aspirantes_invalidos) # Punto 2 y 3
    imprimir_lista_edades(lista_edades_aspirantes) # Punto 4
    ordenar_e_imprimir_lista_edades(lista_edades_aspirantes) # Punto 4
    edad_promedio = informar_edad_promedio(lista_edades_aspirantes) # Punto 5
    informar_encima_o_debajo_del_promedio(lista_edades_aspirantes, edad_promedio) # Punto 5


# | MAIN |
if __name__ == "__main__":
    main() # Ejecuta la función main()
    

# | TESTS DEL PROGRAMA |

# | CASO 1 |
# Dato de entrada: 2
# Salida esperada del programa: - Lo sentimos, el aspirante está fuera del rango de edad, no fue registrado.

# Dato de entrada: 21
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: 75
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: -1
# Salida esperada del programa: 
# | INFORME COMPLETO |
# • La cantidad total de aspirantes válidos que decidieron inscribirse es de 2.
# • Y la cantidad total de aspirantes inválidos que intentaron inscribirse es de 1.
# • La lista de las edades en el orden en que fueron cargadas es la siguiente: [21, 75]
# • La lista de las edades en orden ascendente (de menor a mayor) es la siguiente: [21, 75]
# • La edad promedio entre todos los aspirantes es de 48.0 años.
# • Hay 1 aspirantes que están encima de la edad promedio, y 1 aspirantes que se encuentran por debajo de la edad promedio.


# | CASO 2 |
# Dato de entrada: -1
# Salida esperada del programa: - Por favor, cargá al menos una edad antes de finalizar el programa.

# Dato de entrada: 34
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: 20
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: -1
# Salida esperada del programa:
# | INFORME COMPLETO |
# • La cantidad total de aspirantes válidos que decidieron inscribirse es de 2.
# • Y la cantidad total de aspirantes inválidos que intentaron inscribirse es de 0.
# • La lista de las edades en el orden en que fueron cargadas es la siguiente: [34, 20]
# • La lista de las edades en orden ascendente (de menor a mayor) es la siguiente: [20, 34]
# • La edad promedio entre todos los aspirantes es de 27.0 años.
# • Hay 1 aspirantes que están encima de la edad promedio, y 1 aspirantes que se encuentran por debajo de la edad promedio.


# | CASO 3 |
# Dato de entrada: 50
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: 24
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: 19
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: 75
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: 30
# Salida esperada del programa: - Aspirante registrado.

# Dato de entrada: -1
# Salida esperada del programa:
# | INFORME COMPLETO |
# • La cantidad total de aspirantes válidos que decidieron inscribirse es de 5.
# • Y la cantidad total de aspirantes inválidos que intentaron inscribirse es de 0.
# • La lista de las edades en el orden en que fueron cargadas es la siguiente: [50, 24, 19, 75, 30]
# • La lista de las edades en orden ascendente (de menor a mayor) es la siguiente: [19, 24, 30, 50, 75]
# • La edad promedio entre todos los aspirantes es de 39.6 años.
# • Hay 2 aspirantes que están encima de la edad promedio, y 3 aspirantes que se encuentran por debajo de la edad promedio.