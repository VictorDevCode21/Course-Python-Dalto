#los datos compuestos son datos que tienen adentro otros datos
list = ['Victor Rios', 35, True, 'Money']
print(list[0])

#tupla (la diferencia es que la tupla no se puede modificar)
tupla = ('Victor Rios', 35, True, 'Money')
print(tupla[3])

#Esto es válido: 
#lista[3]= máquina

#Esto no:
#tupla[3]=máquina

#Creando un conjunto (set) la diferencia con la lista es que no puedo acceder por un índice 
#No puede haber duplicados
set = {'Victor Rios', 35, True, 'Money'}
print (set)
#print (set[3]) -> no puede acceder al elemento

#creando un dato dict (diccionario) (la estructura es key : 'value' y separamos con comas)
dict = {
    'nombre' : 'victor rios',
    'profesión' : 'millonario',
    'está_generando_muchos_ingresos' : True,
    'dato_duplicado' : 'millonario'   
}
print (dict['nombre'])
