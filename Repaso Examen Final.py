# Introducción a la Algoritmia - Repaso para el Examen Final

# EJERCICIO 1): 
# Leer los números de legajo de los alumnos de un curso y su nota de examen final. 

# El fin de la carga se determina ingresando un -1 como legajo.
# Se debe validar que la nota ingresada esté entre 1 y 10. Terminada la lectura de datos, informar:
# 1. Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
# 2. Cantidad de alumnos que desaprobaron el examen. Nota menor a 4.
# 3. Promedio de notas y los legajos que superan el promedio.

# Luego, se solicita mostrar un listado de legajos y calificaciones ordenado de manera ascendente (menor a mayor) según el número de legajo. 

def Ejercicio1():
    
    def cargar_datos_alumnos(): # Cargar datos de los alumnos (legajos y notas)
        flag = True
        matriz_alumnos = [
            [], # Fila de Legajos: matriz_alumnos[0]
            [] # Fila de Notas: matriz_alumnos[1]
        ]

        while flag == True:
            legajo_alumno = int(input("\n> (-1 para finalizar la carga de datos) Introducí el legajo de un alumno: "))
            if legajo_alumno == -1:
                flag = False
            else:
                nota_final_alumno = int(input("> Ahora, la nota del examen final (1-10): "))
                while nota_final_alumno < 1 or nota_final_alumno > 10:
                    nota_final_alumno = int(input("> Por favor, ingresá una nota válida del 1 al 10: "))
                matriz_alumnos[0].append(legajo_alumno)
                matriz_alumnos[1].append(nota_final_alumno)
        return matriz_alumnos
                
                    
    def calcular_alumnos_aprobados_y_desaprobados(matriz_alumnos):
        alumnos_aprobados = 0
        alumnos_desaprobados = 0
        
        for i in range(len(matriz_alumnos[1])): # range(0, longitud de la fila de notas)
            if matriz_alumnos[1][i] >= 4:
                alumnos_aprobados += 1
            else:
                alumnos_desaprobados += 1
        return alumnos_aprobados, alumnos_desaprobados


    def calcular_promedio_y_mejores_legajos(matriz_alumnos):
        suma_notas = 0
        promedio = 0
        legajos_superan_promedio = []
        
        for i in range(len(matriz_alumnos[1])):
            suma_notas += matriz_alumnos[1][i]
        
        promedio = suma_notas / len(matriz_alumnos[1])
        
        for i in range(len(matriz_alumnos[0])):
            if matriz_alumnos[1][i] > promedio:
                legajos_superan_promedio.append(matriz_alumnos[0][i])

        return promedio, legajos_superan_promedio
            
            
    def mostrar_datos_ordenados(matriz_alumnos):
        for i in range(len(matriz_alumnos[0])): # Bubble Sort: ordenar legajos de forma ascendente (menor a mayor)
            for j in range(0, len(matriz_alumnos[0])-i-1):
                if matriz_alumnos[0][j] > matriz_alumnos[0][j+1]:
                    matriz_alumnos[0][j], matriz_alumnos[0][j+1] =  matriz_alumnos[0][j+1], matriz_alumnos[0][j]
                    matriz_alumnos[1][j], matriz_alumnos[1][j+1]= matriz_alumnos[1][j+1], matriz_alumnos[1][j]
        
        print("Listado de legajos y calificaciones (orden ascendente según número de legajo): ")
        for i in range(len(matriz_alumnos[0])):
            print(f"Legajo: {matriz_alumnos[0][i]} - Nota: {matriz_alumnos[1][i]}")
        
        
    def main():
        print("\n- Aula B101: Legajos de los alumnos y notas del examen final -")
        print("A continuación, vas a ingresar uno por uno el legajo y la nota del final de cada alumno: ")
        matriz_alumnos = cargar_datos_alumnos()
        aprobados, desaprobados = calcular_alumnos_aprobados_y_desaprobados(matriz_alumnos)
        promedio_notas, mejores_legajos = calcular_promedio_y_mejores_legajos(matriz_alumnos)
        
        print("\n- Informe del Aula B101 -")
        print(f"\n• Alumnos aprobados: {aprobados}")
        print(f"• Alumnos desaprobados: {desaprobados}")
        print(f"• Promedio de notas: {promedio_notas}")
        print(f"• Legajos que superan el promedio: {mejores_legajos}")
        print("")
        
        mostrar_datos_ordenados(matriz_alumnos)
        
        
    if __name__=="__main__":
        main()






############################################################################################################

xCheck = False

while xCheck == False:
    ejercicioSeleccionado = int(input("\nIngresá el número del ejercicio que querés ejecutar (del 1 al 4) o '0' para salir del programa: "))
    if ejercicioSeleccionado == 1:
        Ejercicio1()
    elif ejercicioSeleccionado == 2:
        pass
    elif ejercicioSeleccionado == 3:
        pass
    elif ejercicioSeleccionado == 4:
        pass
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 4 o '0' para salir del programa: ")