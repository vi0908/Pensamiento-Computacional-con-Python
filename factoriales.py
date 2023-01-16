
def factorial(n):
    """calcula el factorial de n.

    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1 # límite de la función
    return n * factorial(n-1)


n = int(input('ingrese un entero: '))
print(f'factorial: {factorial(n)}')



