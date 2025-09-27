Nombre= input("Ingrese su nombre por favor: ")
print("Elija una de las siguientes opciones: ")
print("1) Si quiere su nombre en mayusculas.")
print("2) Si quiere su nombre en minusculas.")
print("3) Si quiere su nombre con la primera letra en mayuscula.")
num = int(input("Opcion: "))

if num == 1:
    print(Nombre.upper())

elif num == 2:
    print(Nombre.lower())

elif num == 3:
    print(Nombre.title())

else:
    pass