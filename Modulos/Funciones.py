#Funciones
#Son un conjunto de tareas independientes o semindependientes que realiza una tarea en concreto cuando se le manda llamar.
escrito="Un texto generico"
#Declaracion
def mi_primer_funcion():
	print("Esta es mi primer funcion")

#Asignacion de valores a las funciones
def imprime(texto="Un texto cualquiera"):
	print(texto)

#asignacion detallada de valores en las variables
	#nombre_completo(apeido="Limon",nombre="Fernando")
def nombre_completo(nombre,apeido):
	print(f"Mi nombre es {nombre} {apeido}")

#Asignacion de valores por defecto
def lenguage_fav(lenguage="python"):
	print(f"Mi lenguaje favorito para programar es {lenguage}")

#asignacion de cantidad de valores dinamico
   #number_print(1,2,3,4,5,6,7,8,9)
def number_print(*numeros):
	for numero in numeros:
		print(numero)

#Retorno de valores generadon dentro de la funcion
def suma(num1: int,num2:int):
	if type(num1)==int and type(num2)==int:
		resultado=num1+num2
		return resultado

#Anidado de funciones
def multip(num1,num2):
	if type(num1)==int and type(num2)==int:
		resultado=num1*num2
		imprime(resultado)

def main():
	mi_primer_funcion()

	
	imprime(escrito)
	nombre_completo(apeido="Limon",nombre="Fernando")
	lenguage_fav()
	number_print(1,2,3,4,5,6,7,8,9)

	valor=suma(5,8)
	print(valor)

	multip(3,4)


if __name__ in "__main__":
	main()

