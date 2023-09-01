#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle 
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que reingrese los datos  
        except Exception as e:
            print("Te pedi un numero, no una letra")
            print(f"ERROR: {e}")
        #si todo esta bien terminamos el bucle
        else:
            break
        #el finally se ejecuta siempre
        finally: 
            print("Manejo de excepcion finalizado")  
    #mostrando el resultado   
    return resultado

print(sumar_dos())