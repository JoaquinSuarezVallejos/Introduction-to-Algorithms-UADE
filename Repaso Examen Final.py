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
        sin_legajos = True
        matriz_alumnos = [
            [], # Fila de Legajos: matriz_alumnos[0]
            [] # Fila de Notas: matriz_alumnos[1]
        ]

        while flag == True:
            legajo_alumno = int(input("\n> (-1 para finalizar la carga de datos) Introducí el legajo de un alumno: "))
            while legajo_alumno == -1 and sin_legajos == True:
                legajo_alumno = int(input("\n> Por favor, ingresá al menos un legajo para ver el informe: "))
                if legajo_alumno != -1:
                    sin_legajos = False
            sin_legajos = False
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


# EJERCICIO 2): 
# Una Administradora de Consorcios necesita un sistema para poder gestionar el cobro de las expensas de un edificio de 20 unidades.

# En dos listas almacena la siguiente información:
# • Número de unidad y superficie en metros cuadrados.
# Validar que no se ingresen números de unidades duplicadas. Cada unidad paga de expensas un valor fijo por metro cuadrado, el que se ingresa por teclado.

# Se pide:
# • Informar el promedio de expensas del mes.
# • Ordenar los listados de mayor a menor según la superficie.
# • Mostrar por pantalla el listado ordenado informando el número de unidad y la superficie en metros cuadrados.

def Ejercicio2():
    
    numero_unidades = []
    superficie_unidades = []
    
    def cargar_datos_edificio():
        exit_flag = False
        duplicado_flag = False
        isDuplicado = False
        VALOR_EXPENSAS_M2 = 0

        while exit_flag == False:
            while duplicado_flag == False:
                unidad = int(input("\n> (-1 para finalizar la carga de datos) Ingresá un número de unidad: "))
                if unidad == -1:
                    exit_flag = True
                    
                isDuplicado = False
                for i in range(len(numero_unidades)):
                    if unidad == numero_unidades[i]:
                        isDuplicado = True
                        print("\n! Ingresaste un número de unidad duplicado por error, no se registró.")
                if isDuplicado == False:
                    duplicado_flag = True
            
            if unidad != -1:     
                duplicado_flag = False
                superficie = int(input("> Ahora ingresá su superficie en m2: "))
                while superficie < 1:
                    superficie = int(input("\n> Por favor, ingresá un número válido: "))
                
                numero_unidades.append(unidad)
                superficie_unidades.append(superficie)

        VALOR_EXPENSAS_M2 = int(input("\n> Por último, ingresá el valor de expensas por m2: "))
        while VALOR_EXPENSAS_M2 < 1:
            VALOR_EXPENSAS_M2 = int(input("\n> Por favor, ingresá un valor válido: "))
        
        return numero_unidades, superficie_unidades, VALOR_EXPENSAS_M2
    
    
    def informar_promedio_expensas(VALOR_EXPENSAS_M2):
        promedio_expensas = 0
        suma_total_m2 = 0
        for i in range(len(superficie_unidades)):
            suma_total_m2 += superficie_unidades[i]
        
        promedio_expensas = (suma_total_m2 * VALOR_EXPENSAS_M2) / len(numero_unidades)
        
        print(f"\nEl promedio de expensas que paga el propietario/a de una unidad mensualmente es de: ${promedio_expensas}")
    
    
    def ordenar_listado():
        for i in range(len(superficie_unidades)): # Bubble Sort en orden descendente (de mayor a menor)
            for j in range(len(superficie_unidades)-i-1):
                if superficie_unidades[j] < superficie_unidades[j+1]:
                    superficie_unidades[j], superficie_unidades[j+1] = superficie_unidades[j+1], superficie_unidades[j]
                    numero_unidades[j], numero_unidades[j+1] = numero_unidades[j+1], numero_unidades[j]
    
    
    def mostrar_listado_ordenado():
        print("\nListado de todas las unidades (orden descendente según superficie en m2): ")
        for i in range(len(numero_unidades)):
            print(f"Número de unidad: {numero_unidades[i]} - Superficie: {superficie_unidades[i]}m2")
            
        
    def main():
        print("\n- Sistema de Gestión de las Expensas del Edificio 'Albarellos' -")
        print("A continuación, vas a introducir uno por uno cada número de unidad en el edificio, junto con su superficie en m2:")
        unidades, superficie, VALOR_EXPENSAS_M2 = cargar_datos_edificio() # 1
        ordenar_listado() # 2
        mostrar_listado_ordenado() # 3
        informar_promedio_expensas(VALOR_EXPENSAS_M2) # 4
        
    
    if __name__ == "__main__":
        main()
        
        
# EJERCICIO 3):
# En una carrera de ciclistas participan N competidores, donde N se ingresa por teclado.
# Desarrollar un programa que permita cargar, por cada competidor, su número de identificación y el tiempo que tardó en terminar 
# la carrera en horas, minutos y segundos.
# Luego se solicita:
# • Mostrar el número del ganador de la carrera y el tiempo que empleó.
# • Ingresando por teclado el tiempo récord registrado para dicha carrera, informar si el ganador batió el récord anterior.
# • Calcular y mostrar el tiempo promedio entre todos los ciclistas.
# Los ciclistas se identifican con números enteros, no necesariamente correlativos.

def Ejercicio3():
    
    identificaciones_ciclistas = []
    tiempo_horas = []
    tiempo_minutos = []
    tiempo_segundos = []
    
    def check_numero_natural1(num):
        while num < 1: 
            num = int(input("\n> Por favor, ingresá un número válido: "))
            
    def check_numero_natural2(num):
        while num < 0:
            num = int(input("\n> Por favor, ingresá un número válido: "))
    
    def check_num_identificacion():
        exit_flag = False
        num_valido = True
        num_duplicado = False
        
        while exit_flag == False:
            num_duplicado = False
            num_identificacion = int(input("> Número de identificación: "))
            
            while num_identificacion < 1:
                num_valido = False
                num_identificacion = int(input("\n> Por favor, ingresá un número válido: "))
                
                if num_identificacion >= 1:
                    num_valido = True
            
            for i in range(len(identificaciones_ciclistas)):
                if num_identificacion == identificaciones_ciclistas[i]:
                    num_duplicado = True
                    print("\n! Ingresaste un número de identificación duplicado por error, no se registró.")
                
            if num_valido == True and num_duplicado == False:
                exit_flag = True
        
        return num_identificacion
            
        
    def cargar_datos_carrera():
        cantidad_ciclistas = int(input("\n> Para empezar, ingresá la cantidad de ciclistas que compiten en esta carrera: "))
        check_numero_natural1(cantidad_ciclistas)
        
        print("\nA continuación, vas a introducir uno por uno el número de identificación de cada competidor")
        print("y el tiempo que tardó en terminar la carrera en horas, minutos y segundos. ")
        
        for i in range(cantidad_ciclistas):
            print(f"\nCiclista N°{i+1}: ")
            numero_identificacion = check_num_identificacion()
            
            print("Tiempo que tardó en llegar a la meta...")
            horas = int(input("> Horas: "))
            check_numero_natural2(horas)
            
            minutos = int(input("> Minutos: "))
            check_numero_natural2(minutos)
            
            segundos = int(input("> Segundos: "))
            check_numero_natural2(segundos)
            
            identificaciones_ciclistas.append(numero_identificacion)
            tiempo_horas.append(horas)
            tiempo_minutos.append(minutos)
            tiempo_segundos.append(segundos)
    
    
    def mostrar_ganador_y_tiempo():
        # • Mostrar el número del ganador de la carrera y el tiempo que empleó.
        
            
            
    def main():
        print("\n- Bienvenido/a al Sistema del Gran Fondo de Argentina -")
        cargar_datos_carrera()
        
        
    if __name__ == "__main__":
        main()


############################################################################################################

xCheck = False

while xCheck == False:
    ejercicioSeleccionado = int(input("\nIngresá el número del ejercicio que querés ejecutar (del 1 al 4) o '0' para salir del programa: "))
    if ejercicioSeleccionado == 1:
        Ejercicio1()
    elif ejercicioSeleccionado == 2:
        Ejercicio2()
    elif ejercicioSeleccionado == 3:
        Ejercicio3()
    elif ejercicioSeleccionado == 4:
        pass
    elif ejercicioSeleccionado == 0:
        xCheck = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 4 o '0' para salir del programa: ")