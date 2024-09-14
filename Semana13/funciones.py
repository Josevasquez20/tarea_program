#Declaramos nuestra lista 3D
temp = [
    [  #Ciudad 1
    [23,15,14,15,18,19,21],
    [15,12,14,25,22,23,26],
    [15,18,19,20,22,26,27],
    [17,19,29,22,22,29,18]
],
    [ #Ciudad 2
    [25,27,22,23,24,25,26],
    [21,23,24,25,19,18,15 ],
    [24,25,26,23,21,22,25]
    ],
[    #Ciudad 3
    [25,27,22,23,24,30,25],
    [21,29,24,29,12,18,15 ],
    [34,25,31,23,21,26,25]
    ]
]

def calcular_prom (ciud,sem):  #Creamos la función calcular_prom y unos argumentos que son la ciudad y la semana que escogeremos
    suma = 0 # Declaramos la variable suma en cero
    cont = 0 # Declaramos nuestro contador en cero



    for i in range(len(temp)): #Recorremos nuestra lista
     if i == ciud : # Comprobamos si nuestra iteración es igual a a la semana que elejimos
        for j in range(len(temp[i])): # Recorremos los dias dentro de nuestra lista ciudad actual
            if j == sem :# Comprobamos si nuestro iterador j es igual a la variable dia
             for k in range(len(temp[i][j])):  #La iteración temperatura recorre cada temperatura registrada en el día actual.
                suma = suma + temp[i][j][k] #sumamos
                cont+=1 #Aumentamos en uno nuestro contador


# Calcular el promedio
    if cont > 0: #Verificamos si nuestro contador se cambio y sumo uno
        promedio = suma / cont # Realizamos el promedio de la suma y dividimos para las veces que nuestro contador sumo uno
        return f"El promedio de la ciudad {ciud} de la semana {sem} es: {promedio:.2f}"  #Retornamos un mensaje con la ciudad,semana y promedio el cual agregamos 2f para que nos muestre solo dos decimales
    else:  #Si nuestro contador se quedo en cero quiere decir que los numero ingresados no se ecnotraron dentro de la lista
        return "No se pudo calcular el promedio."

#Imprimimos nuestra función y en los argumentos colocamos la ciduad y semana que queremos saber el promedio

print(calcular_prom(0,1))