#creando una función simple
def saludar():
    print('Hola Victor, ¡eres un crack!, saludos')

#Ejecutando la función simple:  
saludar()

#crear una funcion que tenga parametros(una variable que existe dentro de una función)

def saludar(nombre,sexo):
    sexo= sexo.lower()
    if (sexo== 'mujer'):
        adjetivo= 'guapa!'
    elif(sexo== 'hombre'):
        adjetivo= 'guapo!'
    print(f'Hola {nombre}, mi {adjetivo} ¿cómo estás?')
    
saludar('Victor','HoMbre')
saludar('Victor', 'MuJeR')

#crear una funcion que nos retorne valores

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero= str(num)
    num= int(num_entero[0])
    c1= num - 2
    c2= num
    c3= num -5
    contraseña= f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}' 
    print(contraseña)
    
crear_contraseña_random(10)

#using return (para poder guardar los valores)

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero= str(num)
    num= int(num_entero[0])
    c1= num - 2
    c2= num
    c3= num -5
    contraseña= f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}' 
    return contraseña 
    
password= crear_contraseña_random(5)
frase= f"tu contraseña nueva es: {password}"
print(frase)

#crear una funcion que nos retorne multiples valores 

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero= str(num)
    num= int(num_entero[0])
    c1= num - 2
    c2= num
    c3= num -5
    contraseña= f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}' 
    return contraseña, num 

#desempaquetando la funcion
password, primer_num = crear_contraseña_random(398)

#monstrando los resultados obtenidos y los datos utilizados para obtenerlos 
print(f"tu contraseña nueva es: {password}")
print(f"el número utilizado para crearla fue: {primer_num}")


