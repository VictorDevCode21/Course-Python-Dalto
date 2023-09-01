#Abriendo el archivo con "with open"
with open("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos/random.txt", encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido=archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#no es necesario cerrarlo al usar with open