#Actividad_1
#Pedimos la edad
edad = int(input("Ingrese su edad: "))
#Verificamos si es mayor de edad o no
if (edad >= 18):
    print("Es mayor de edad")
else:
    pass

#Actividad_2
#Ingresamos la nota
nota = float(input("Ingrese su nota adquirida: "))

#Condicionamos si aprobo o desaprobo
if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

#Actividad_3
#Pedimos un numero par
num = int(input("Ingrese un número par: "))

#Verificamos si el numero es par o impar
if (num % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Actividad_4
#Pedimos al usuario ingresar su edad
print("Hola, a continuacion le pediremos su edad para saber a que grupo pertenece")
edad = int(input("Ingrese su edad: "))

#Clasificamos al usuario dependiendo de su edad
if (edad < 12):
    print("Niño")
elif (edad >=12 and edad < 18):
    print("Adolescente")
elif (edad >= 18 and edad < 30):
    print("Adulto joven")
elif (edad >= 30):
    print("Adulto")
else:
    pass

#Actividad_5
password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

#Determinamos si la contraseña es correcta o no)
if (len(password)>=8 and len(password)<=14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Actividad_6
#Llamamos la biblioteca para poder calcular moda, mediana y media aritmetica
from statistics import mode, median, mean

#Agregamos el codigo para pedir una lista de 50 numeros aleatorios
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

#Calculamos la media, mediana y moda
media= mean(numeros_aleatorios)
mediana= median(numeros_aleatorios)
moda= mode(numeros_aleatorios)

#Imprimimos los resultados
print(moda)
print(mediana)
print(media)

#Determinamos si tienen sesgo positivo, sesgo negativo o no tiene
if (media > mediana and mediana > moda):
    print("Sesgo positivo o a la derecha")

elif(media < mediana and mediana < moda):
    print("Sesgo negativo o a la izquierda")

else:
    print("Sin sesgo")

#Actividad_7
#Pedimos al usuario a que ingrese una frase o palabra
palabra = input("Ingrese una frase o palabra: ")

#localizamos la ubicacion de la ultima letra de la frase
ultima = palabra[-1]

#Verificamos si termina en vocal o no 
if ultima in "aeiou":
    print(f"{palabra}!")
else:
    print(palabra)

#Actividad_8
#Le pedimos al usuario que ingrese su nombre
Nombre= input("Ingrese su nombre por favor: ")

#Imprimimos las diferentes opciones para que eligir
print("Elija una de las siguientes opciones: ")
print("1) Si quiere su nombre en mayusculas.")
print("2) Si quiere su nombre en minusculas.")
print("3) Si quiere su nombre con la primera letra en mayuscula.")

#Pedimos al usuario que ingrese la opcion preferida
num = int(input("Opcion: "))

#Imprimimos la opcion elegida por el usuario
if num == 1:
    print(Nombre.upper())

elif num == 2:
    print(Nombre.lower())

elif num == 3:
    print(Nombre.title())

else:
    pass

#Actividad_9
#Pedimos al usuario que ingrese la magnitud del terremoto
Terremoto = float(input("Ingrese la magnitud del terremoto: "))


print("A continuacion clasificaremos el terremoto en la escala de Ritcher")

#Clasificamos la magnitud del terremoto con la escala de ritcher
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

# Pedimos datos
hemisferio = input("¿En cuál hemisferio se encuentra? (N/S): ").lower()
mes = input("Ingrese el mes: ").lower()
dia = int(input("Ingrese el día: "))

# Función para determinar estación en hemisferio sur
if hemisferio == "s":
    if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):#Rango verano 21 Diciembre - 20 Marzo
        estacion = "Verano"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):#Rango otoño 21 de Marzo - 20 de junio
        estacion = "Otoño"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):#Rango invierno 21 de junio - 20 de septiembre
        estacion = "Invierno"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):#Rango primavera 21 de septiembre - 20 diciembre
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"

# Funcion para determinar estacion en hemisferio norte
if hemisferio == "n":
    if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):#Rango invierno 21 Diciembre - 20 Marzo
        estacion = "Invierno"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):#Rango primavera 21 de Marzo - 20 de junio
        estacion = "Primavera"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):#Rango verano 21 de junio - 20 de septiembre
        estacion = "Verano"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):#Rango otoño 21 de septiembre - 20 diciembre
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
    
    #Impresion de la estacion
    print(f"Te encuentras en {estacion}")

