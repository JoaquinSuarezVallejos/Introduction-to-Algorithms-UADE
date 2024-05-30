# Introducción a la Algoritmia - Clase 8

# Búsqueda Binaria

def busquedaBinaria(lista, elemento):
    izquierda = 0
    derecha = len(lista)-1
    indice = -1
    
    while indice == -1 and izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        if lista[centro] == elemento:
            indice = centro
        elif lista[centro] < elemento:
            izquierda = centro + 1
        else:
            derecha = centro - 1
    return indice

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(busquedaBinaria(lista, 5))
    