numeros= [4,7,1,42,15]

#encontrando el numero mayor de una lista (max)
numero_mas_alto= max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista (max)
numero_mas_bajo= min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero= round(12.345,2)
print(numero)

#retorna False -> 0, vacío, False, ninguno/True-> distinto de 0 o cadena 
result= bool(0)
print(result)

#retorna True si todos los valores son verdaderos (o sea si hay 1 que es 0 nos devuelve False)
result= all([234,'true',[344,23]])
print(result)

#suma todos los valores de un iterable (si es letra nos devuelve excepciones)
suma= sum(numeros)
print(suma)



