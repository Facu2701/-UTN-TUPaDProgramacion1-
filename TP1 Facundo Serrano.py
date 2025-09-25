#ACTIVIDAD N°1
print("Hola Mundo")

#ACTIVIDAD N°2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

#ACTIVIDAD N°3
nombre = input("Ingrese su nombre y apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Por ultimo ingrese su lugar de residencia:")
print(f"Hola soy {nombre}, tengo {edad} y vivo en {residencia}")

#ACTIVIDAD N°4
import math

radio = int(input("Ingrese el radio del circulo en m: "))
Perimetro = 2 * math.pi * radio
Area = math.pi * (radio ** 2)

print(f"El perimetro del circulo es {Perimetro}m y su area es de {Area}m**2")

#ACTIVIDAD N°5
seg = float(input("Ingrese la cantidad de segundos que desea: "))

hs = seg / 3600

print(f"En total la cantidad de segundos ({seg}) ingresados equivalen a {hs} hs")

#ACTIVIDAD N°6
num = int(input("ingrese un numero para saber su tabla de multiplicacion: "))

a1= num*1
a2= num*2
a3= num*3
a4= num*4
a5= num*5
a6= num*6
a7= num*7
a8= num*8
a9= num*9
a10= num*10

print(f"La tabla de multipliaccion de {num} es: ")
print (a1)
print (a2)
print (a3)
print (a4)
print (a5)
print (a6)
print (a7)
print (a8)
print (a9)
print (a10)

#ACTIVIDAD N°7
print ("A continuacion se le pedira ingresar 2 numeros distintos de 0 para calcular la suma, resta, multiplicacion y division entre ellos")
num1 = int(input(""))
num2 = int(input(""))

suma = num1 + num2
resta= num1 - num2
div= num1/num2
mult= num1*num2

print(f"Suma = {num1} + {num2} = {suma}")
print(f"Resta = {num1} - {num2} = {resta}")
print(f"Multiplicacion = {num1} * {num2} = {mult}")
print(f"Division = {num1} / {num2} = {div}")

#ACTIVIDAD N°8
print("Ingrese los siguientes datos: ")
Altura = float(input("Altura(en m): "))
Peso = float(input("Peso(en kg): "))

IMC= Peso/(Altura**2)

print(f"Su indice de masa corporal es de: {IMC} kg/m2 ")

#ACTIVIDAD N°9
tempc = float(input("Ingrese la temperatura en grados celsius: "))

tempf = (5/9)*tempc + 32

print(f"El equivalente de la temperatura {tempc}°C en grados Farenheit es de {tempf}°F")

#ACTIVIDAD N°10
print("A continuacion se les pedira ingresar 3 numeros para el calculo de su promedio")
num1 = float(input(""))
num2 = float(input(""))
num3 = float(input(""))

prom = (num1+num2+num3)/3

print(f"El promedio entre {num1}, {num2} y {num3} es de {prom}")