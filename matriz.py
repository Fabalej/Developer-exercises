# Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
# números consecutivos horizontal o vertical y si se encuentra mostrar la posición
# inicial y final.

#GENERAR UNA MATRIZ ON NUMPY

import random
import numpy as np

#Genero la matriz de números enteros de 5x5 y la relleno con 1
matriz = np.ones((5,5), dtype = np.integer)

#Cargo la matriz con numeros enteros generados aleatoriamente, y la imprimo con los numeros entre conchetes
#para que quede bien visible
for i in range(5):
    for j in range(5):
        matriz[i][j] = random.randint(1, 5)
        print("[", matriz[i][j], "]", end=" ")
    print()

# Rellena la matriz con numeros consecutivos en las filas solo par la prueba
""" cont = 0

for i in range(5):
    for j in range(5):
        matriz[i][j] = cont
        print("[", matriz[i][j], "]", end=" ")
        cont += 1
    cont = 0
    print() """

# Rellena la matriz con numeros consecutivos en las columnas solo par la prueba
""" cont = 0

for i in range(5):
    for j in range(5):
        matriz[i][j] = cont
        print("[", matriz[i][j], "]", end=" ")
        #cont += 1
    cont += 1
    print() """

#Creo una variable que usare en caso de no encontrar números consecutivos en las filas
bandera_fila = False

#Con en bucle y los 2 if conprueo si existen números consecutivos desde la posicion 0 a la 3, 
#y desde la posicion 1 a la 4 en cada fila de la matriz
for i in range(5):
    #Chequea si hay úmeros consecutivos ascendentes
    if matriz[i][0] == (matriz[i][1]-1) and (matriz[i][1]) == (matriz[i][2]-1) and (matriz[i][2]) == (matriz[i][3]-1):
        print(f"La posició inicial es {i},{0}")
        print(f"La posició final es {i},{3}")
        bandera_fila = True

    if matriz[i][1] == (matriz[i][2]-1) and (matriz[i][2]) == (matriz[i][3]-1) and (matriz[i][3]) == (matriz[i][4]-1):
        print(f"La posició inicial es {i},{1}")
        print(f"La posició final es {i},{4}")
        bandera_fila = True

    #Chequea si hay números consecutivos descendentes
    if matriz[i][0] == (matriz[i][1]+1) and (matriz[i][1]) == (matriz[i][2]+1) and (matriz[i][2]) == (matriz[i][3]+1):
        print(f"La posició inicial es {i},{0}")
        print(f"La posició final es {i},{3}")
        bandera_fila = True

    if matriz[i][1] == (matriz[i][2]+1) and (matriz[i][2]) == (matriz[i][3]+1) and (matriz[i][3]) == (matriz[i][4]+1):
        print(f"La posició inicial es {i},{1}")
        print(f"La posició final es {i},{4}")
        bandera_fila = True

#En casode no haber números consecutivos en las filas se imprimira la leyenda dentro del if
if bandera_fila == False:
    print("----------------------------------------------")
    print("No hay números consecutivos en las Filas!!!")
    print("----------------------------------------------")

#Creo una variable que usare en caso de no encontrar números consecutivos en las colimnas
bandera_columna = False

#Con en bucle y los 2 if conprueo si existen números consecutivos desde la posicion 0 a la 3, 
#y desde la posicion 1 a la 4 en cada columna de la matriz
for j in range(5):
    #Chequea si hay úmeros consecutivos ascendentes
    if matriz[0][j] == (matriz[1][j]-1) and (matriz[1][j]) == (matriz[2][j]-1) and (matriz[2][j]) == (matriz[3][j]-1):
        print(f"La posició inicial es {0},{j}")
        print(f"La posició final es {3},{j}")
        bandera_columna = True

    if matriz[1][j] == (matriz[2][j]-1) and (matriz[2][j]) == (matriz[3][j]-1) and (matriz[3][j]) == (matriz[4][j]-1):
        print(f"La posició inicial es {1},{j}")
        print(f"La posició final es {4},{j}")
        bandera_columna = True

    #Chequea si hay números consecutivos descendentes
    if matriz[0][j] == (matriz[1][j]+1) and (matriz[1][j]) == (matriz[2][j]+1) and (matriz[2][j]) == (matriz[3][j]+1):
        print(f"La posició inicial es {0},{j}")
        print(f"La posició final es {3},{j}")
        bandera_columna = True

    if matriz[1][j] == (matriz[2][j]+1) and (matriz[2][j]) == (matriz[3][j]+1) and (matriz[3][j]) == (matriz[4][j]+1):
        print(f"La posició inicial es {1},{j}")
        print(f"La posició final es {4},{j}")
        bandera_columna = True

#En casode no haber números consecutivos en las columnas se imprimira la leyenda dentro del if
if bandera_columna == False:
    print("-------------------------------------------------")
    print("No hay números consecutivos en las Columnas!!!")
    print("-------------------------------------------------")
