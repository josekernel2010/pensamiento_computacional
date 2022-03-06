
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    print(n)
    return fibonacci(n-1) + fibonacci(n-2)
""" Funcion de fibonacci para mejorar el rendimiento """

n = int(input("Enter a number: "))

funcion = fibonacci(n)

print(funcion)

suma = lambda a ,b: a+b
print("La suma es: ",suma(22,55))
