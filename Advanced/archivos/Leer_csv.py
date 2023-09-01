

import csv

with open("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos/datos.csv")as archivo:
    
    #usamos "csv.reader(name)" y nos indica el objeto
    #print(csv.reader(archivo))
    
    
    reader=csv.reader(archivo)
    #para recorrerlo usamos row 
    for row in reader:
        print(row) 
    
    
    

