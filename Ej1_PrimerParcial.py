# Primer Parcial - Ejercicio 1:

print("\nEjercicio 1:")
flag = True
edadAlumno = -1
cantAlumnosInicial = 0
cantAlumnosPrimario = 0
cantAlumnosSecundario = 0
montoSubsidioInicial = 0
montoSubsidioPrimario = 0
montoSubsidioSecundario = 0

while flag == True:
    edadAlumno = int(input("Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: "))
    
    if edadAlumno == 0:
        flag = False
    elif edadAlumno >= 1 and edadAlumno <= 5:
        cantAlumnosInicial += 1
        montoSubsidioInicial += 800
    elif edadAlumno >= 6 and edadAlumno <= 12:
        cantAlumnosPrimario += 1
        montoSubsidioPrimario += 1200
    elif edadAlumno >= 13 and edadAlumno <= 17:
        cantAlumnosSecundario += 1
        montoSubsidioSecundario += 2100
    else:
        print("La edad ingresada no es válida, tiene que ser entre 1 y 17.")
    
print("")

print(f"Nivel Incial:")
print(f"Cantidad de alumnos: {cantAlumnosInicial} | Monto total de subsidio mensual: {montoSubsidioInicial}")

print(f"Nivel Primario:")
print(f"Cantidad de alumnos: {cantAlumnosPrimario} | Monto total de subsidio mensual: {montoSubsidioPrimario}")

print(f"Nivel Secundario:")
print(f"Cantidad de alumnos: {cantAlumnosSecundario} | Monto total de subsidio mensual: {montoSubsidioSecundario}")


# | Test 1 |

# Datos de entrada esperados:
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: 3
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: 15
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: 16
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: 0

# Datos de salida esperados:
# Nivel Incial:
# Cantidad de alumnos: 1 | Monto total de subsidio mensual: 800
# Nivel Primario:
# Cantidad de alumnos: 0 | Monto total de subsidio mensual: 0
# Nivel Secundario:
# Cantidad de alumnos: 2 | Monto total de subsidio mensual: 4200 


# | Test 2 |

# Datos de entrada esperados:
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: 0 

#Datos de salida esperados:
# Nivel Incial:
# Cantidad de alumnos: 0 | Monto total de subsidio mensual: 0
# Nivel Primario:
# Cantidad de alumnos: 0 | Monto total de subsidio mensual: 0
# Nivel Secundario:
# Cantidad de alumnos: 0 | Monto total de subsidio mensual: 0


# | Test 3 |

# Datos de entrada esperados:
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: 17
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: -1
# La edad ingresada no es válida, tiene que ser entre 1 y 17
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: 13
# Para finalizar el programa, escribir '0'. Ingresá la edad de un alumno: 0

# Datos de salida esperados:
# Nivel Incial:
# Cantidad de alumnos: 0 | Monto total de subsidio mensual: 0
# Nivel Primario:
# Cantidad de alumnos: 0 | Monto total de subsidio mensual: 0
# Nivel Secundario:
# Cantidad de alumnos: 2 | Monto total de subsidio mensual: 4200