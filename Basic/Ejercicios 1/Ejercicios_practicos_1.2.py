#Datos: 
# 1 segundo son 2 palabras
# ¿cuantos segundos? ¿cuantas palabras?

#a) 
#Calcular cuánto tardaría en decir esa palabras
#¿Cúantas palabras dijo?

Frase= input('dime una frase y te digo cuánto tardarías en decirla: ')
palabras_separadas = Frase.split(' ')
cantidad_de_palabras= len(palabras_separadas)

print(f'Dijiste {cantidad_de_palabras} palabras y tardarías {cantidad_de_palabras/2} segundos')
print(f'Dalto lo diría en {cantidad_de_palabras *100 //2 /100 *0.70} segundos ')

#En caso de que tarde mas de 1 minuto significaría que son mas de 120 palabras, por tanto, le diremos que pare un poco
if (cantidad_de_palabras)> 120:
    print('para, tampoco te pedí un testamento')
    
