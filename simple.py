# Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
# edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
# elementos. retornar la lista.

import random

#Declaro el diccionario
diccionario = {}

#Declaro la funcion para crear el diccionario en forma automatica
def lista_diccionario():
    #El for me va a dar la clave del diccionario desde el 0 al 9, y random un numero aleatorio entre 1 y 100 que sera el valor
    for id in range(0, 10):
        edad = random.randint(1, 100)
        diccionario[id]=[edad]

    return diccionario


print("DICCIONARIO SIN ORDEN")
#Llamo e imprimo el diccionario creado
print(lista_diccionario())
print("-----------------------------------------------------------------------")

# Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
# menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.

#Creo una lista
lista_dicc = ()

#Creo la funcion que ordena de mayor a menor el diccionario y lo imprimo
#Imprimo el indice de la menor y mayor edad
def ordenar_diccionario(diccionario):
    print("DICCIONARIO ORDENADO POR EDAD DE MAYOR A MENOR")
    print(sorted(diccionario.items(), key = lambda x: x[1], reverse=True))
    lista_dicc = sorted(diccionario.items(), key = lambda x: x[1], reverse=True)
    print(f"El Indice de la menor edad es:", lista_dicc[-1][0])
    print(f"El Indice de la mayor edad es:", lista_dicc[0][0])
        
ordenar_diccionario(diccionario)




