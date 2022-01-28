from os import system
from pyfiglet import Figlet

system("cls")


titulo = Figlet(font='standard')
titulo = titulo.renderText('Funciones Anidadas')
print(titulo)

# función que recibe un argumento y una función
def func1(un_arg, una_func):
    
    # función anidada que recibe un argumento
    def func2(otro_arg):
        return otro_arg * 2
    
    # variable que almacena el resultado de la función anidada
    valor = func2(un_arg)    
    return una_func(valor)


# función que recibe un solo argumento y devuelve el argumento mas 5
def cualqueir_func(cualquier_arg):
    return cualquier_arg + 5


valor1 = int(input("Escoge un numero: "))
# aplicando función con un argumento númerico y una función como argumento
a  = func1(valor1, cualqueir_func)

print( "El valor de la función anidada es: ", a)

