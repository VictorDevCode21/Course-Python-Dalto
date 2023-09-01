
frutas= ['banana','manzana','ciruela','pera','naranja','granada','durazno']
cadena= 'Hola Victor'
numeros=[2,5,8,10]

for fruta in frutas:
    #si no quiero alguna uso el if/continue
    if fruta== 'granada':
        continue
    print(f'me voy a comer una {fruta}')
    
#Evitar que el bucle siga ejecutándose (el else no se ejecuta tampoco)

for fruta in frutas: 
    print(f'me voy a comer una {fruta}')
    if fruta == 'pera':
       break
   
print(f'bucle terminado')

#recorrer (iterar) una cadena de texto 

for letra in cadena:
   print(letra) 
   
#For en una sola línea de código (duplicamos los números)
numeros_duplicados= [x+2 for x in numeros]
print(numeros_duplicados)


    