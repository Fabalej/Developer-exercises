# Escribir una clase en python llamada círculo que contenga un radio, con un método que
# devuelva el área y otro que devuelva el perímetro del círculo.
# Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
# usuario e impidiendo la instanciación.
# Si printeamos el objeto creado debe mostrarse una representación amigable.
# El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
# mostrar un error y no permitir modificación.
# Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
# multiplicado por n. No permitir la multiplicación por números <= 0

from math import pi

#Creo la clase circulo que calcula el area y el perimetro del mismo
class circulo:

    def __init__ (self, radio):
        self.radio = radio
    
    #Funcion para calcular el area del circulo
    def area(self):
        area = round((self.radio**2) * pi, 2)
        print(f"El area del circulo es = {area} cm2")

    #Funcion para calcular el perimetro del circulo
    def perimetro(self):
        perimetro = round(self.radio * 2 * pi, 2)
        print(f"El perimetro del circulo es = {perimetro} cm")

#Decalro variables que usare a continuación
radio_ing = 0
bandera = True

#Pide el ingreso de un valor positivo para el radio
radio_ing = float(input("Ingrese un valor positivo para el radio, en cm: "))

#Condicional que impide el instancioado del objeto si se ingresar un cero o números negativos
if radio_ing > 0:
    circulo1 = circulo(radio_ing)
    circulo1.area()
    circulo1.perimetro()
    
#En caso de ingresar un cero o número negativo, se muestra un mensaje advirtiendolo
else:
    print()
    print("Ha ingresado Cero o un número Negativo!!!")
    print()
    bandera = False

#Print par generar solamente un espacio
print()

#Condicional que solicita un valor por el cual se multiplicara el radio antes ingresado
#siempre y cuando el valor del radio sea positivo; si es cero o un número negativo
#se pondra la variable bandera el falso y no se ejecutara el siguiente condicional
if bandera == True:
    multiplo = float(input("Ingrese un valor positivo por el cual multiplicara el radio: "))
else:
    bandera = False
    
#Condicional que se ejecuta siempre y cuando se haya ingresado un número positivo para el radio
#y multiplica el valor del radio por el número ingresado
if bandera == True:
    if multiplo > 0 and bandera == True:
        radio_multiplo = radio_ing * multiplo
        circulo2 = circulo(radio_multiplo)
        circulo2.area()
        circulo2.perimetro()
    
    #En caso de ingresar un cero o número negativo, se impide la instanciación, 
    #se muestra un mensaje y se pide que ingrese nuevamente un valor positivo
    else:
        print()
        print("Ha ingresado Cero o un número Negativo!!!")
    



#Con el codigo que sigue se pide el inreso de un valor, y si se ingresa un cero o número negativo
#se le advierte al usuario, y se le solcita que intente nuevamente.
#El bucle no terminara hasta que ingrese un número positivo
""" #Bucle que pide el ingreso del valor del radio con un condicional que impide ingresar un cero o números negativos
while True:
    radio_ing = float(input("Ingrese un valor positivo para el radio, en cm: "))
    if radio_ing > 0:
        circulo1 = circulo(radio_ing)
        circulo1.area()
        circulo1.perimetro()
        break

    #En caso de ingresar un cero o número negativo, se impide la instanciación, 
    #se muestra un mensaje y se pide que ingrese nuevamente un valor positivo
    else:
        print()
        print("Ha ingresado Cero o un número Negativo!!!")
        print("Ingrese un número mayor que Cero")
        print()

#Print par generar solamente un espacio
print()

#Bucle que pide el ingreso de un valor por el cual se multiplicara el radio antes ingresado
while True:
    multiplo = float(input("Ingrese un valor positivo por el cual multiplicara el radio: "))
    if multiplo > 0:
        radio_multiplo = radio_ing * multiplo
        circulo2 = circulo(radio_multiplo)
        circulo2.area()
        circulo2.perimetro()
        break

    #En caso de ingresar un cero o número negativo, se impide la instanciación, 
    #se muestra un mensaje y se pide que ingrese nuevamente un valor positivo
    else:
        print()
        print("Ha ingresado Cero o un número Negativo!!!")
        print("Ingrese un número mayor que Cero")
        print() """

