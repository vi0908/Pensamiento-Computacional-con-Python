objetivo = int(input(f'Por favor ingrese un número: '))
respuesta = 0
while respuesta**2 < objetivo: #no es igual porque se evalúa respuesta + 1
    print(respuesta, respuesta**2)
    respuesta +=1
if respuesta**2 == objetivo:
    print(f'{objetivo} tiene raíz exacta y es: {respuesta}')
else:
    print(f'{objetivo} no tiene raíz exacta :(')
    


