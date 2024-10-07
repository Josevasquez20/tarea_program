#Lectura de Archivo de Texto
archivo = open("my_notes.txt","r")  # Abrimos las notas con el argumento r de (read)
ver = archivo.readlines()  #Llamamos al metodo ver
print(ver)  #Imprimimos

archivo.close() #Cerramos