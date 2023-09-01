Diccionario= {
    'Nombre': 'Victor',
    'Apellido': 'Rios',
    'Neth Worth': 10000000000
}

#Keys() -> Devuelve las claves (también nos sirve para iterar)
claves= Diccionario.keys()
#print(claves)

#get() -> Devuelve el valor de una clave 
#obteniendo un elemento con get () (no me lanza una excepción, si no encuentra nada, el programa continua)
claves= Diccionario.get('Neth Worth')
valor_de_Neth_Worth= Diccionario.get('Neth Worth')


#clear()-> elimina todos los elementos 
#eliminando_todo_del_diccionario= 
# Diccionario.clear()

#pop()-> elimina un elemento 
#Diccionario.pop('Nombre')
#print (Diccionario)

#items()-> para iterar el dict
#Obteniendo un elemento dict_items iterable
Diccionario_iterable= Diccionario.items()
print(Diccionario_iterable)