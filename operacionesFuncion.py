"""funciones lamnda en expresiones"""

suma = lambda a, b: a + b
print(suma(21,35))


"""funciones como objetos"""

def multiplicar_x_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f,numeros):
    result = []
    
    for num in range(numeros):
        resultado = f(num)
        result.append(resultado)
    return result
        
        
funcion = aplicar_operacion(multiplicar_x_dos, 5)
print(funcion)
        
for n in funcion:
    print("Este es el ciclo for: ",n)    



"""Funciones en estructura de datos"""
# funcion donde se puede pasar una lista de funciones

def aplicar_operaciones(num):
    operaciones =[abs,float]
    resultado = []
    
    for operacion in operaciones:
        resultado.append(operacion(num))    
    return resultado
    
    
print(aplicar_operaciones(-5))
    





        