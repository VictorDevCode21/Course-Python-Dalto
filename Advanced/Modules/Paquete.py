#un paquete sigue siendo un modulo 
#para usar el paquete debemos crear un archivo llamado "__init__.py" dentro de la carpeta que queremos usar 
# el __init__.py es lo que define al paquete, si no tiene ese archivo es solamente una carpeta y no un paquete

#importamos el paquete y buscamos la ruta:
import Packages

print(type(Packages))
print(Packages.__path__)

#para extraer el modulo y usar la funcion hacemos lo siguiente:

import Packages.salutacion
print(Packages.salutacion.Saludar("Victor"))

import Packages.salutacion_rara
print(Packages.salutacion_rara.Saludar_raro("Victor"))



