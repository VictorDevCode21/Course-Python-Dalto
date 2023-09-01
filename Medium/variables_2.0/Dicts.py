#creando diccionarios con dict()
diccionario= dict(nombre= 'Victor', apellido='Rios')

#las listas no pueden ser claves (las tuplas si) 
diccionario= {('victor','rios'): 'jaja'}

#para hacer un diccionario con un conjunto usamos frozenset

diccionario= {frozenset(['victor','rios']): 'jaja'}

#creando diccionarios con fromkeys
diccionario= dict.fromkeys('ABCDE','LetrasDelAbecedario')


print(diccionario)