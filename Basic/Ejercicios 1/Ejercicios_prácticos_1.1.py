#Datos

#Promedio de duración

Otros_cursos_min= 2.5
Otros_cursos_max= 7
Otros_cursos_promedio= 4
Dalto_curso= 1.5

# Diferencias de duración (Ejercicio A)
Diferencia_con_min= 100 - Dalto_curso/Otros_cursos_min *100
Diferencia_con_max= 100 - Dalto_curso * 1000 //Otros_cursos_max /10
Diferencia_con_promedio= 100 - Dalto_curso/Otros_cursos_promedio *100

#mostrando las diferencias de duración (Ejercicio A)

print(f'El curso de Dalto dura un {Diferencia_con_max} % menos que el más lento')
print(f'El curso de Dalto dura un {Diferencia_con_min} % menos que el más rápido')
print(f'El curso de Dalto dura un {Diferencia_con_promedio} % menos que el promedio')
print('------------------')

#Cual es material que se pierde

#calculando el % de tiempo vacio (Ejercicio B)

crudo_promedio= 5
crudo_dalto= 3.5

tiempo_vacio_promedio= 100 - Otros_cursos_promedio * 1000 //crudo_promedio /10
tiempo_vacio_curso_dalto= 100- Dalto_curso * 1000 //crudo_dalto/10
tiempo_vacio_dalto_promedio= 100- crudo_dalto * 1000 // crudo_promedio /10 

#Mostrando en promedio la cantidad de tiempo perdido en los videos (Ejercicio B)

print(f'un curso promedio elimina el {tiempo_vacio_promedio} % menos de tiempo vacío')
print(f'este curso eliminó {tiempo_vacio_curso_dalto} % menos de tiempo vacío')
print(f'el curso de dalto tiene un crudo promedio de {tiempo_vacio_dalto_promedio} % menos que el crudo promedio')
print('------------------')
#¿Ver 10 horas de este curso a cuánto equivaldría de otros cursos? (Ejercicio C)

print(f'ver 10 horas del Curso de Dalto equivale a ver {Otros_cursos_promedio *100//Dalto_curso/10} horas de otros cursos')
print(f'ver 10 horas del Curso de otros cursos equivale a ver {Dalto_curso *100//Otros_cursos_promedio/10} horas de este curso')
print('------------------')







