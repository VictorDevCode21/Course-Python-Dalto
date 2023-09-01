#datos
#1 alumno es profesor
#1 alumno es asistente 

#a) pedir la edad de los partners que vinieron hoy a clase y ordenar los datos de mayor a menor 
#b) El mayor es el profesor y el menor es el asistente quien es quien?

#funcion para obtener el asistente y el profesor segun la edad
def obtener_partners(cantidad_de_partners):
    #creando lista con partners
    name= []
    #Ejecutando un for para pedir info de los partners
    for i in range(cantidad_de_partners):
        nombre = input("escribir el nombre de los que vinieron: ")
        edad = int(input("introducir la edad de los partners que vinieron hoy a clase: "))
        partner= (nombre, edad)
        #agregando info a la lista
        name.append(partner)
    #ordenandolos de menor a mayor segun su edad 
    name.sort(key=lambda x:x[1])
    #partners[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    #para definir al asistente y al profesor:
    asistente= name[0][0]
    profesor= name[-1][0]
    #retornamos una tupla
    return asistente, profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_partners(5)
print(f"El asistente es: {asistente} y el profesor es: {profesor}")





