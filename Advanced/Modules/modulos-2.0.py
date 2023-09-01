#Si el modulo estuviera en una carpeta en la misma ruta:

#import funciones_buenas.salutacion
#print(funciones_buenas.salutacion.Saludar("Victor"))


#si esta fuera de la misma ruta o carpeta que nuestro nuevo modulo entonces:

import sys

#para que nos devuelva el nombre de todos los modulos:
#print (sys.builtin_module_names)

#para conocer la ruta del modulo:
sys.path.append("c:\\Users\\NB 3300\\Documents\\Programming\\Curso de Python Dalto\\funciones_buenas")

#import salutacion as modulo_saludo #asi parezca que va a dar error no lo da 
#print(modulo_saludo.Saludar("Victor"))




