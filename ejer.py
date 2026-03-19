# 1 suma de listas
numeros1 = [1, 2, 3, 4, 5]
total = sum(numeros1)
print("Suma:", total)


# 2 recorrer listas
lista = [10, 20, 30, 40]
print("\nRecorrido de lista:")
for elemento in lista:
    print(elemento)


# 3 numeros pares
pares = [i for i in range(1, 101) if i % 2 == 0]
print("\nNúmeros pares del 1 al 100:")
print(pares)


# 4 doble ciclo
lista2 = [1, 2, 3, 4]
print("\nCombinaciones:")
for i in lista2:
    for j in lista2:
        print(i, j)


# 5 funciones (promedio, max y min)
numeros2 = [5, 10, 15, 20, 25]

def calcular_promedio(lista):
    return sum(lista) / len(lista)

def encontrar_maximo(lista):
    return max(lista)

def encontrar_minimo(lista):
    return min(lista)

print("\nResultados:")
print("Promedio:", calcular_promedio(numeros2))
print("Máximo:", encontrar_maximo(numeros2))
print("Mínimo:", encontrar_minimo(numeros2))