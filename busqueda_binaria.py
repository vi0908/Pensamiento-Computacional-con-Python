objetivo = int(input('escoja un número: '))
#número al que se le calculará la raíz cuadrada
epsilon = 0.01
#precisión del algoritmo
bajo = 0.0
#valor mínimo para calcular el largo del conjunto
alto = max(1.0, objetivo)
#valor máximo aceptado, corresponderá al valor ingresado por el usuario, el uno es por si se ingresa un número negativo
respuesta =(alto + bajo) / 2
#generación del valor medio de nuestro conjunto

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
    if respuesta**2 < objetivo:
     #si el valor de la mitad**2 es menor que el objetivo, quiere decir que lo que buscamos es un número mayor
        bajo = respuesta
     #el valor menor valor del nuevo conjunto ahora corresponde al valor de la mitad del conjunto inicial
    else:
        alto = respuesta
     #si nos pasamos, este valor corresponderá al mayor del nuevo conjunto
    respuesta = (alto + bajo) / 2
    #se vuelve a buscar la mitad del nuevo conjunto

print(f' la raíz cuadrada de {objetivo} es {respuesta}')

## este algoritmo se utiliza un método númerico llamado MÉTODO DE LA BISECCIÓN
## solo podrá utilizarse en CONJUNTOS ORDENADOS

