#cambiar el tipo de dato de una columna 
import pandas as pd

df=pd.read_csv("archivos_problemas\\datos.csv")

#convirtiendo a string los datos de una columna
df["Age"] = df["Age"].astype(str)

#mostrando el tipo de dato del primer elemento de la columna edad
#print(type(df["Age"][0]))

#reemplazando los datos "mamagueva" por "perra"
df["Lastname"].replace("mamagueva","Perra",inplace=True)

#eliminando las filas con datos vacios
df= df.dropna()

#eliminando las filas con datos repetidos
df= df.drop_duplicates()

#Creando un CSV con el dataframe resultante(limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")

