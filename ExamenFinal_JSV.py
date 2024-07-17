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
def cargar_edades_aspirantes():
    exit_flag = False
    EDAD_MINIMA = 13
    EDAD_MAXIMA = 80
    lista_edades_aspirantes = []
    cant_aspirantes_validos = 0
    cant_aspirantes_invalidos = 0
    
    while exit_flag == False:
        edad_aspirante = int(input("\n> (Finalizar la carga de edades con '-1') Ingresá la edad de un aspirante: "))
        
        if edad_aspirante != -1:     
            if edad_aspirante < EDAD_MINIMA or edad_aspirante > EDAD_MAXIMA:
                print("\n- Lo sentimos, el aspirante está fuera del rango de edad, no fue registrado.")
                cant_aspirantes_invalidos += 1
            else:
                cant_aspirantes_validos += 1
                lista_edades_aspirantes.append(edad_aspirante)
                print("- Aspirante registrado.")
        elif edad_aspirante == -1:
            exit_flag == True
        else:
            mostrar_error()
            
    return lista_edades_aspirantes, cant_aspirantes_validos, cant_aspirantes_invalidos


def imprimir_lista_edades(lista_edades_aspirantes):
    print("\nLa lista de las edades en el orden en que fueron cargadas es la siguiente: ")
    print(f"{lista_edades_aspirantes}")


def ordenar_e_imprimir_lista_edades(lista_edades_aspirantes): # Ordenar e imprimir la lista de menor a mayor (orden ascendente)
    for i in range(len(lista_edades_aspirantes)): # Ordenar por el método Bubble Sort
        for j in range(len(lista_edades_aspirantes)-i-1):
            if lista_edades_aspirantes[j] > lista_edades_aspirantes[j+1]:
                lista_edades_aspirantes[j], lista_edades_aspirantes[j+1] = lista_edades_aspirantes[j+1], lista_edades_aspirantes[j]
    
    
    
    


def mostrar_error():
    print("\n-! Ha ocurrido un error inesperado, el programa ha finalizado.")
    exit()


def main(): # Función principal
    print("\n- Bienvenido/a al Sistema del Programa de Becas del Club Buenos Aires -")
    print("\nIMPORTANTE: Las edades permitidas para las becas son de 13 a 80 años inclusive.")


# | MAIN |
if __name__ == "__main__":
    main() # Ejecuta la función main()
    

# | TESTS DEL PROGRAMA |