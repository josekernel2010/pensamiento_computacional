# Busqueda binaria se utiliza para encontrar un elemento en una lista ordenada

objetivo = int(input('Escoge un numero: '))

epsilon = 0.01
bajo = 0.0
# variable de alto
alto = max(objetivo, 1.0)

respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
