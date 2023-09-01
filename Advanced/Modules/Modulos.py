#Todos los archivos que usan (.py) son modulos 

#importando un modulo y asignandole el nombre: "m_Saludar"
#import Modulo_saludar  as m_Saludar

import Modulo_saludar as m_Saludar 

saludo= m_Saludar.Saludar("Victor")
print(saludo)

#Para importar solamente la funcion de un modulo especifico 
from Modulo_saludar import Saludar
saludo= Saludar("Victor")
print(saludo)

#Para importar varias funciones de un modulo especifico 
from Modulo_saludar import Saludar,Saludar_raro

#creamos las variables con los saludos
saludo= Saludar("Victor")
saludo_raro= Saludar_raro("Petra")

#mostramos los resultados 
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de la funcion 
#print(dir("nombre de funcion"))

#accedemos al nombre de este modulo
#print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)

#Para enroutar funciones (traer de otras carpetas alguna funcion) hacemos esto:

#from (nombre de carpeta).(nombre de modulo) import "Funcion" y si queremos le cambiamos el nombre.
#from funciones_buenas.m_Saludar  import Saludar as m_Saludar 


