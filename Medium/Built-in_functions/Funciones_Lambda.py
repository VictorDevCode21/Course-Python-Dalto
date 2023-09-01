#Lambda crea funciones anonimas

#Creando una funcion lambda para multiplicar por 2:
multiplicar_por_2 = lambda x : x*2
print(multiplicar_por_2(5))

#seria lo mismo que: (pero mas facil y optimizado)
#def multiplicar_por_2(x):
   # return x*2

#creando funcion comun que diga si es par o no 
numeros= [1,2,3,4,5,6,7,8,9,11,13,14,15,20]
def es_par(num):
    if(num%2==0):
        return True 
    
#creando funcion comun que diga si es impar 
numeros= [1,2,3,4,5,6,7,8,9,11,13,14,15,20]
def es_impar(num):
    if(num%2==1):
        return True 

#usando filter con una funcion comun para numeros pares e impares 
#numeros_pares= filter(es_par,numeros)
#numeros_impares= filter(es_impar, numeros)

#print(list(numeros_impares))

#creando lo mismo que arriba con Lambda
numeros_pares= filter(lambda numero: numero%2 == 1,numeros)
print(list(numeros_pares))