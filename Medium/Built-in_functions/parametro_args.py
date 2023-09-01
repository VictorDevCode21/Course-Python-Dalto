#forma no optima 
#def sum(a,b):
#result= sum(5,3)
#print(result)

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

result2= suma_total([5,3,9,10,20,3])


#lo mismo que arriba pero utilizando el operador * como parametro (*args)

def suma (name,*numeros):
    return f"{name}, la suma de los numeros es: {sum(numeros)}"

result = suma("Victor", 4,5,6,7,9)
print(result)




    
