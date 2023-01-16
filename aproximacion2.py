objetivo = int(input('escoja un número: '))
epsilon = 0.00
paso = 1
respuesta = 0.0
while abs(respuesta**2 - objetivo) > epsilon and respuesta**2 <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso
if  abs((respuesta)**2 - objetivo) > epsilon:
    print(f'no hay raíz exacta')
else:
    print(f'{objetivo} tiene raíz exacta y es {respuesta}') 
    

# if abs(respuesta**2 - objetivo ) >= epsilon:
#     print(f'la raiz es: no hay raíz')
# elif (respuesta**2 - objetivo) == 0:
#     print(f'la raíz de {objetivo} es {respuesta}')
# else:
#     print(f'la raíz de {objetivo} es {respuesta}')