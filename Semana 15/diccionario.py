
#Creamos nuestro diccionario en donde vamos a colocar cable - valor
informacion_personal = {"Nombre":"José", "Edad":24,"Ciudad": "Quito","Email":"joseelias@gmail.com","Profesión": "Ingeniero de Software"}

print("Diccionario actual\n",informacion_personal)

#Modificamos el valor Ciudad
informacion_personal["Ciudad"] = "Guayaquil"



#Agregamos una nueva clave-valor al diccionario que represente la "profesion" de la persona.

informacion_personal.update({'Profesión':'Ingeniero en Sistemas'})

#Verificamos si la clave telefono existe
teléfono = 984027196
if teléfono not in informacion_personal :  #Si no existe creamos la clave y valor del telefono
    informacion_personal["teléfono"] = teléfono

else:
    print("Si existe el número de teléfono")

#Eliminamos la clave edad
del informacion_personal["Edad"]

#Imprimimos el diccionario
print(f"Diccionario actualizado\n {informacion_personal}")

