""" PRÁCTICA FINAL IBM
Generación de la matriz tamaño NxN, con números aleatorios del 0 al 9,
manejo de excepciones y suma de los valores de cada fila y cada columna"""

from random import randint #para llenar la matriz con numeros aleatorios

#  Excepciones
while True:
    try: 
        n = int(input("Ingresa un número para determinar la cantidad de filas y columnas de la matriz: "))
        if n<2 or n>100:
            print("Valor incorrecto. Debe ingresar un número entero entre 2 y 100")
        else:
            print("la matriz es de", n,"filas por", n, "columnas")
            break
    except ValueError:
        print("Valor incorrecto. Debe ingresar un número entero entre 2 y 100")
 
        

def llenar_matriz(n):
    matriz =[] #la variable matriz será completada una vez que se llena i y j

    for i in range(n):  #i fila
        fila = []

        for j in range (n):  #j columna
            fila.append(randint(0,9)) #llenar la fila con numeros aleatorios
        matriz.append(fila) 

    return matriz


resultado = llenar_matriz (n)

for fila in resultado:  #esto es para imprimir en forma de matriz
    for i in fila:
        print (i, end='  ')
    print('')

print ("\n")

matriz= resultado

# Suma de cada fila
suma_filas = []
for fila in matriz:
    suma_filas.append(sum(fila))
print("La suma de cada fila es:", suma_filas)

# Suma de cada columna
suma_columnas = []
for j in range(n):
    suma_columna = 0 #variable temporal 
    for i in range(n):
        suma_columna += matriz[i][j]
    suma_columnas.append(suma_columna)
print("La suma de cada columna es:", suma_columnas)






