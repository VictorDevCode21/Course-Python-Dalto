#2 listas, una con nombres, otra con apellidos

names= ["Victor","Aurora","Carlos","Paola","Samuel"]
lastnames= ["Rios","Varela","Aigster","Torres","Gapo"]

#Registrando esta informacion en un archivo txt de forma optima 

with open ("archivos_problemas\\names_and_lastnames.txt","w") as close_people:
    close_people.writelines("The data is:\n\n")
    [close_people.writelines(f"Name: {n}\nLastname: {last}\n--------\n")for n,last in zip(names,lastnames)]

