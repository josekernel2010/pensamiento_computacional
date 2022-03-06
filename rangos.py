"""rangos en python"""


rango1 = range(0,10)

print("\n",rango1,"\n")

for i in rango1:
    print("Ciclo for: ",i)
    
    
rango2 = range(0,10,2)
print("\n",rango2,"\n")

for i in rango2:
    print("Ciclo for2: ",i)
    
    

"""comparaciones de range"""

ran1 = range(0,7,2)
ran2 = range(0,8,2)
print("\ncomparacion de dos rangos: ",ran1 == ran2)

#utilizando list comprehension para guardar los numeros del rango en una lista
reto1= [i for i in ran1]
reto2 =[i for i in ran2]
print(reto1)
print(reto2)


