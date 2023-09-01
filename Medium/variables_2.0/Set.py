#creando un conjunto con set
conjunto=set(['dato1','dato2'])

#metiendo un conjunto dentro de otro set
conjunto1= frozenset(['dato1','dato2'])
conjunto2= {conjunto1,'dato3'}
print(conjunto2)

#teoría de conjuntos 
conjunto1= {1,3,5,7}
conjunto2={1,3,7}

#Verificando si es un subconjunto
result= conjunto2.issubset(conjunto1)

#Otra forma de verificar es:
result= conjunto2 <= conjunto1

#verificamos si es un superconjunto
result= conjunto1.issuperset(conjunto2)
result= conjunto1 > conjunto2

#verificar si hay algún número en común (si tira True es que no hay números en común)
result= conjunto2.isdisjoint(conjunto1)


print(result)