def sumatoria (n):
    return n + 2

def multiplicacion(n):
    return n * 2

def operacion(funcion, numeros):
    resultados = [] # aquí iremos guardando los valores
    for numero in numeros:
        resultado = funcion(numero) # a cada número de la lista se le realiza la operación
        resultados.append(resultado) # método de lista
    print(resultados)


valores = [1, 2, 3]
operacion(sumatoria, valores)
operacion(multiplicacion, valores)  