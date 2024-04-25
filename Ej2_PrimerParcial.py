# Primer Parcial - Ejercicio 2:

# Teorema: 
# A + B sea mayor a C
# B + C sea mayor a A
# C + A sea mayor a B

print("\nEjercicio 2:")
esTriangulo = False
segmento1 = 0 #A
segmento2 = 0 #B
segmento3 = 0 #C

print("| Vamos a verificar si 3 segmentos conforman un triángulo o no |")
    
segmento1 = int(input("Ingresá la longitud del primer segmento (número natural): "))
while segmento1 <= 0:
    segmento1 = int(input("Por favor, ingresá un número natural válido: "))
    
segmento2 = int(input("Ahora la del segundo segmento: "))
while segmento2 <= 0:
    segmento2 = int(input("Por favor, ingresá un número natural válido: "))
    
segmento3 = int(input("Por último, la del tercer segmento: "))
while segmento3 <= 0:
    segmento3 = int(input("Por favor, ingresá un número natural válido: "))
    
print("")

if (segmento1 + segmento2) > segmento3 and (segmento2 + segmento3) > segmento1 and (segmento3 + segmento1) > segmento2:
    esTriangulo = True
    print("Se puede formar un triángulo con estos tres segmentos.")
else: 
    esTriangulo = False
    print("NO se puede formar un triángulo con estos tres segmentos.")

if esTriangulo == True:
    if (segmento1 == segmento2 == segmento3):
        print("El triángulo es equilátero.")
    elif (segmento1 == segmento2 or segmento2 == segmento3 or segmento1 == segmento3):
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")


# | Test 1 |

# Datos de entrada esperados: 
# Ingresá la longitud del primer segmento (número natural): 5
# Ahora la del segundo segmento: 5
# Por último, la del tercer segmento: 5

# Datos de salida esperados:
# Se puede formar un triángulo con estos tres segmentos.
# El triángulo es equilátero.


# | Test 2 |

# Datos de entrada esperados: 
# Ingresá la longitud del primer segmento (número natural): 10
# Ahora la del segundo segmento: 10
# Por último, la del tercer segmento: 5

# Datos de salida esperados:
# Se puede formar un triángulo con estos tres segmentos.
# El triángulo es isósceles.


# | Test 3 |

# Datos de entrada esperados: 
# Ingresá la longitud del primer segmento (número natural): 7
# Ahora la del segundo segmento: 8
# Por último, la del tercer segmento: 9

# Datos de salida esperados:
# Se puede formar un triángulo con estos tres segmentos.
# El triángulo es escaleno.


# | Test 4 |

# Datos de entrada esperados: 
# Ingresá la longitud del primer segmento (número natural): -1
# Por favor, ingresá un número natural válido: 2
# Ahora la del segundo segmento: 0
# Por favor, ingresá un número natural válido: 2
# Por último, la del tercer segmento: 2

# Datos de salida esperados:
# Se puede formar un triángulo con estos tres segmentos.
# El triángulo es equilátero.