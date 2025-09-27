Terremoto = float(input("Ingrese la magnitud del terremoto: "))
print("A continuacion clasificaremos el terremoto en la escala de Ritcher")

if Terremoto < 3:
    print("Muy leve")

elif Terremoto >=3 and Terremoto<4:
    print("Leve")

elif Terremoto >=4 and Terremoto<5:
    print("Moderado")

elif Terremoto >=5 and Terremoto<6:
    print("Fuerte")

elif Terremoto >=6 and Terremoto<7:
    print("Muy fuerte")

elif Terremoto > 7:
    print("Extremo")

else:
    pass