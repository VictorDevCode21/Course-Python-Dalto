import pandas as pd

#usando la funcion "read_csv" para leer el archivo CSV

#df= archivo= pd.read_csv("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos/datos.csv")

#obteniendo los datos de la columna nombre 
#nombres = df["nombre"]

#print(nombres)

#para poder poner un encabezado con todos los datos lo hacemos asi:
df= archivo= pd.read_csv("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos/datos.csv",names=["name","lastname","age"])
#nombres= df["name"]
#print(df)

#usando este archivo para concatenar luego mas abajo
df2= archivo= pd.read_csv("c:/Users/NB 3300/Documents/Programming/Curso de Python Dalto/Advanced/archivos/datos.csv",names=["name","lastname","age"])

#creando una cadena para luego usar slicing:
#cadena= "0123456789"

#usando slicing ":" para determinar un rango en la lista o cadena que queremos obtener
#explicacion en ingles: Get the characters from position 2 to position 8 (not included):
#print(cadena[2:8])

#ordenando el dataframe por edad "df" de forma ascendente 
df_orden_ascendente = df.sort_values("age")

#ordenandolo de forma descendente "ascending=False" ya que de forma predeterminada viene puesto para que sea ascendente;
#al introducir un false el codigo lo ordena de forma descendente 
df_orden_descendente = df.sort_values("age", ascending= False)

#print(df_orden_descendente)

#concatenando los 2 df "concat" (el parametro que nos pide es una lista con lo que queremos concatenar): 
#df_concatenado= pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
#primeras_filas= df.head(3)

#accediendo a las ultimas 3 filas con tail()
#ultimas_filas= df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
#filas_y_columnas_totales= df.shape

#si quiero accedes a las filas totales uso:
#filas_totales= filas_y_columnas_totales[0]

#para obtener las columnas totales:
#columnas_totales= filas_y_columnas_totales[1]

#optimizandolo podria poner:
filas_totales,columnas_totales= df.shape 

#print(columnas_totales)
#print(filas_totales)

#obteniendo data estadistica del dataframe:
df_info= df.describe()
print(df_info)

#accediendo a un elemento especifico del dataframe con loc
#accediendo a la edad de la fila 2:
elemento_especifico_loc = df.loc[2,"age"]

#accediendo a un elemento especifico del dataframe con iloc (i=index)
#accediendo a la edad de la fila 2 con iloc:
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todas las filas de una columna (lastnames) con loc
lastnames_loc= df.loc[:,"lastname"]

#accediendo a todas las filas de una columna (lastnames) con iloc
lastnames_iloc= df.iloc[:,1]

#accediendo a la fila 3 con loc 
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc 
fila_3 = df.iloc[2,:]

#accediendo a filas donde la edad es mayor a "numero especifico"
mayor_que_30 = df.loc[df["age"]>30,:]

print(mayor_que_30)
    
