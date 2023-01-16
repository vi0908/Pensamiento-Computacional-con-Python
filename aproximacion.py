num = int(input('escoja un número: '))
# número que analizaremos

epsilon = 0.01 
#incertidumbre con la que se trabajará

paso = 0.01**2
# a medida que el algoritmo avanza aumentaremos el valor del resultado (no necesariamente tiene que ser
# epsilon**2)

respuesta = 0.0 
# donde guardaremos la respuesta en cada iteración, número que se empezará a evaluar en el recorrido

while (num - respuesta**2) >= epsilon and respuesta <= num:
# conforme la resta se acerque a la precisión que se desea obtener 
# y conforme la respuesta sea menor al número a analizar (pues no tiene sentido analizar un número mayor a num)
 
    print(num - respuesta**2, respuesta)
    #se imprime el valor de la resta y la respuesta que se está evaluando
    respuesta += paso
    #se aumenta el valor de la respuesta

if (num - respuesta**2) <= epsilon:
     print(f'la raiz cuadrada de {num} es {respuesta}') 
     #aquí se muestra la raíz, cuya diferencia será menor a epsilon
else:
     print(f'no se encontró la raiz cuadrada') 

