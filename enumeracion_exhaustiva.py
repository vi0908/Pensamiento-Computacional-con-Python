num = int(input('elija un entero: ')) #número a evaluar
respuesta = 0 #contador

while respuesta**2 < num: 
    # no es = porque el número final será respuesta + 1, 
    # entonces, el que se evalua es el siguiente término
    print(respuesta)
    respuesta += 1
    #aquí inicia la enumeración exhaustiva, se elevan todos los 
    # números **2 iniciando desde el contador hasta que se 
    # alcance al num 
if  respuesta**2 == num:
    print(f'{respuesta} -> {num} tiene raíz cuadrada exacta.')
else:
    print(f'{num} no tiene raíz cuadrada exacta')
