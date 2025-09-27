password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

if (len(password)>=8 and len(password)<=14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")