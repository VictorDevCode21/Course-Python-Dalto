#usamos el parámetro ¨w¨ que significa write
with open("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos/Puto.txt","w",encoding="UTF-8") as archivo:
    #con esta funcion sobreescribimos el archivo y basicamente nos volamos todo lo que tenga para escribir algo nuevo xd 
    #archivo.write("holi holi")
    
    #agredando dos lineas con writelines y \n para dejar espacios entre lineas
    archivo.writelines(["hola bro, que tal\n","A mimir\n"])
    
    #agregando otras 2 lineas 
    archivo.writelines(["que pasa gente\n","A levantarse\n"])
    
    
    
