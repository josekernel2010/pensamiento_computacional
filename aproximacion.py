from os import system
from pyfiglet import Figlet

system("cls")

titulo = Figlet(font='standard')
titulo = titulo.renderText('Aproximacion')

print(titulo)
objetivo = int(input('Escoge un numero: '))

# variable epsilon para determinar la precision
epsilon = 0.01
# variable paso para determinar el incremento
paso = epsilon**2
respuesta = 0.0

# while para determinar la aproximacion de la raiz cuadrada
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso


# convierte respuesta**2 - objetivo a un numero entero con abs()
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
