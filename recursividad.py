

def factorial(n):
    
    if n == 0:
        return 1
    print(n)
    return n * factorial(n-1)

"""Funcion que calcula el factorial de un numero"""

n = int(input("Ingrese un numero: "))

funcion = factorial(n)

print(funcion)