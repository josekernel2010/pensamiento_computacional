"""definiendo tuplas():"""
#son un tipo de estructura de dato que no se puede modificar
#solo se pueden reasignar pero eso ya hace que apunte a otro lugar en memoria
mi_tupla = (1)

print("tipo de dato: ",type(mi_tupla))

#utilizamos la coma para definir la tupla de un solo elemento
mi_tupla = (1,)

print("tipo de dato: ",type(mi_tupla))


"""desempaquetado de tuplas"""

tupla_2 = (1,2,3)

a,b,c = tupla_2

print("\nAsignacion de \nvarias variables a \nelementos de una tupla\n")
print("Variable a: ",a)
print("Variable b: ",b)
print("Variable c: ",c)


"""desempaquetado utilizando una funcion"""

def tupla_desempaquetado():
    return (5,8)

z,x = tupla_desempaquetado()

print("\nAsignando variables con una funcion\n")
print("Variable z: ",z)
print("Variable x: ",x)
