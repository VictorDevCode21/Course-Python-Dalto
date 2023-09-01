#Un método es una función aplicada a objetos

cadena1= 'Hola, Soy Victor'
cadena2= 'bienvenido'

result= dir(cadena1)
#dir me da direcciones acerca de que puedo hacer con esto 
result= cadena1.upper() #convierte todo a mayúscula el upper 
#El esquema es el siguiente:
#DATO.MÉTODO(PARÁMETRO)
#print(result)

#Para Mayúsculas: .upper()
#Para minúsculas: .lower()
#Primera letra en mayúscula: .capitalize (convierte todo en minúscula excepto la primera)

#FIND (buscamos una cadena en otra cadena) (nos dice la posición en la que está desde el 0)
busqueda_find= cadena1.find('Hola') 
#nos devuelve -1 cuando no encuentra un valor

#Index (si no encuentra nada nos devuelve una excepción)
#buscamos una cadena en otra cadena
#busqueda_index= cadena1.index()

#ISNUMERIC (si es numérico nos devuelve True, si no, devuelve False)
#es_numérico= cadena1.isnumeric()

#Si es alfanumérico devolvemos True, si no, False
es_alfanumerico= cadena1.isalpha()
#El espacio no es alfanumérico, solo va desde la A-Z

#Count (contamos las coincidencias de una cadena, devuelve la cantidad de coincidencias)
contar_coincidencias= cadena1.count("la soy")
#si no se encuentra nada da 0 

#Len (contamos cuantos caracteres tiene una cadena 
contar_caracteres= len(cadena1)

#Startswith
#verificamos si una cadena empieza con otra cadena dada, si es así devuelve True
empieza_con= cadena1.startswith('Hola')

#Endswith
#verificamos si una cadena termina con otra cadena dada, si es así devuelve True
termina_con= cadena1.startswith('Victor')

#Replace
#Reemplaza un pedazo de una cadena dada por otra cadena dada
#Si el valor 1 se encuentra en la cadena original reemplaza el valor 1 por el valor 2
cadena_nueva = cadena2.replace('o','a')
cadena_nueva2= cadena_nueva.capitalize()
#print(cadena_nueva2)

#SPLIT (separa cadenas con la cadena que le pasemos)
cadena_separada = cadena1.split(',')
#print(cadena_separada[0])







