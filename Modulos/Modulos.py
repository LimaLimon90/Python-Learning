#Modulos
#Son fragmentos de codigo que se pueden mandar a llamar desde otros ficheros o archivos

#Declaracion
#import Calculadora
import Funciones
Funciones.imprime()

#Asinasion de valores
Funciones.imprime("Este es un modulo")

#retorno de valores
suma=Funciones.suma(5,8)
print("El resultado es ",suma)

#Llamado de funciones anidadas
Funciones.multip(3,7)
Funciones.imprime(Funciones.suma(3,4))

#Llamado de funciones especificas de un modulo
from Calculadora import rest, mult
print(rest(8,3))
print(mult(2,4))

#Llamado de variables gloables del modulo
texto=Funciones.escrito
print(texto)

#Importado y renombre de modulos
import math	as mate
print(mate.pi)

#Renombrado de funciones de modulos
from math import sqrt as raiz
print(raiz(25))
