
lista= cosas_que_tengo_en_mi_cuarto= ['laptop','televisor','playstation','vaso contigo','router']
numbers= [0,10,20,30,40]

#recorriendo la lista objetos en mi cuarto
for objeto in lista:
    print(f'ahora la variable objeto es igual a: {objeto}')
    
#recorriendo la lista de números
for number in numbers:
    print(f'ahora el número del 0-40 sumados por 10 consiguiente va a ser {number}')
    
#recorriendo la lista de números y multiplicando cada valor por 10 
    for number in numbers:
        result = number *10
        print(f' ahora el resultado de multiplicar estos número por 10 nos da {result}')
        
#Para iterar ambas listas: (deben tener la misma cantidad de elementos)

for number, objeto in zip (cosas_que_tengo_en_mi_cuarto,numbers):
    print(f'recorriendo lista 1: {number}')
    print(f'recorriendo lista 2: {objeto}')

#para iterar un rango que establecemos iniciando en el primer valor pero sin llegar al último
for num in range(5,10):
    print(num)
    
#para iterar hasta el número que digamos:
for num in range(10):
    print(num)
    
#Forma correcta de recorrer una lista por su índice:
for num in enumerate (numbers):
    índice= num[0]
    value= num[1]
    print(f'el índice es: {índice} y el value is: {value}')
    
#Using For/Else 
for num in numbers: 
    print(f'ejecutando el ultimo bucle, valor actual: {num}')
    
else:
    print(f'el bucle terminó')
    
#Funciona igual para listas y sets.