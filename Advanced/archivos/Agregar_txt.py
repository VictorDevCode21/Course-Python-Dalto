#usamos el parámetro ¨a¨ que significa append (agrega mas texto sin sobreescribir el anterior)
with open("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos/Puto.txt","a",encoding="UTF-8") as archivo:
    
    #agregando el archivo (agrega un archivo tras otro sin sobreescribir)
    archivo.write("holi holi\n")
    archivo.write("hola hola")
    
    #usando un bucle para agregar varias lineas 
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"linea {i+1} agregada\n")
        
    
    