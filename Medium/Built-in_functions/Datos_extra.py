#creando una funcion de 3 parametros 
def frase(nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante =frase("Victor","Rios","crack")
print(frase_resultante)

#utilizando keyword arguments (obligamos a la funcion a cambiar el adjetivo)
frase_resultante= frase(adjetivo= "maquina", nombre= "Victor", apellido="Rios")
print(frase_resultante)

