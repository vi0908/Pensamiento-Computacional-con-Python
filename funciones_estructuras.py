def f_operaciones (numero):
    operaciones = [abs, float] #operacion corresponde a las dos funciones contenidas en esta variable
    valores = []
    for operacion in operaciones:
        resultados = operacion(numero) #se llevan a cabo las funciones contenidas en operaciones con el argumento = numero
        valores.append(resultados)
    return(valores)
    
usuario = int(input(f'por favor ingrese un número: '))
print(f'el valor absoluto y el flotante de su número es: {f_operaciones (usuario)}')
