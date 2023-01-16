
def sumatoria(n):
    """ Calcula el valor de la sumatoria desde 1 hasta n.
    n int > 0
    returns sumatoria"""
    if n >= 1:
        print(n)
        print(f'{n} + {sumatoria(n-1)} = {sumatoria(n)}')
    if n == 1:
        return 1
    return n + sumatoria(n-1)
n = int(input(f'ingrese un entero: '))
print(f'sumatoria = {sumatoria(n)}')