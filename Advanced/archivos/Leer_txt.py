#Nota: este metodo es para archivos pequeños, si tratamos de leer un archivo grande nos peta la ram xd 
#usando "open" para abrir un archivo:
#archivo= open("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos\\random.txt")

#para imprimir el archivo sin leerlo hacemos esto:
#print(archivo)

#para poder leer el archivo txt debemos usar (.read())
#print(archivo.read())

#para usar caracteres especiales tales como: '¿' y 'Ñ' usamos encoding=UTF-8:
#open("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos\\random.txt", encoding="UTF-8")

#para optimizar mas el codigo:
archivo_sin_leer= open("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos\\random.txt", encoding="UTF-8")

#leer archivo completo
#archivo=archivo_sin_leer.read()
#print(archivo) 

#Si queremos leer linea por linea usamos: ".readlines":
#lineas= archivo_sin_leer.readlines()
#print(lineas)

#Leer 1 sola linea 
linea= archivo_sin_leer.readline() #si dentro del parantesis ponemos numeros, el programa lee cada caracter hasta completar el numero que le pusimos. NO ES EL NUMERO DE LINEAS

print(linea)

#para cerrar el archivo usamos ".close()"
archivo_sin_leer.close()

#si queremos volver a leer el archivo entonces debemos usar otra vez la funcion open 

                 