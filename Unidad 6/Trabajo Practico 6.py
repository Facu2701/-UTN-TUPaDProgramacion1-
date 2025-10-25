
# Trabajo Practico 6.py
#Actividad 1
#Creamos la funcion imprimir_hola_mundo
def imprimir_hola_mundo():
   Saludo =print("Hola Mundo!")
   return Saludo
#Llamamos a la funcion desde el programa principal
imprimir_hola_mundo()

#Actividad 2

def saludar_usuario(nombre):
   Saludo = print(f"Hola {nombre}!")
   return Saludo
#Solicitamos el nombre del usuario
nombre_usuario = input("Por favor, ingresa tu nombre: ")
#Llamamos a la funcion con el nombre proporcionado
saludar_usuario(nombre_usuario)

#Actividad 3
#creamos la funcion informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
   Saludo = print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
   return Saludo
#Solicitamos los datos al usuario
nombre_usuario3 = input("Ingrese su nombre: ")
apellido_usuario= input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
#Llamamos a la funcion con los datos proporcionados
Saludo = informacion_personal(nombre_usuario3,apellido_usuario,edad,residencia)
print(Saludo)

#Actividad 4
#Importamos la constante pi desde el modulo math
from math import pi
#Creamos la funcion calcular_area_circulo y calcular_perimetro_circulo
def calcular_area_circulo(radio):
   Area = ( pi * ( radio ** 2 ) )
   return Area
def calcular_perimetro_circulo(radio):
   Perimetro = 2 * pi * radio
   return Perimetro

#Solicitamos el radio, area y perimetro al usuario
Radio = int(input("Ingrese el radio del circulo: "))
Area=calcular_area_circulo(Radio)
Perimetro = calcular_perimetro_circulo(Radio)
#Mostramos los resultados
print(f"El circulo de radio {Radio} tiene un area de {Area} y un perimetro de {Perimetro}")

#Actividad 5
#Creamos la funcion segundos_a_horas
def segundos_a_horas(segundos):
   horas= segundos/3600 #1 hora = 3600 segundos 
   return horas
#Solicitamos la cantidad de segundos al usuario
seg = int(input("Ingrese la cantidad de segundos que quiere pasar a horas: "))
hs = segundos_a_horas(seg) #Llamamos a la funcion y mostramos el resultado
print(f"{seg} segundos son {hs} horas")


#Actividad 6
#Creamos la funcion tabla_multiplicar
def tabla_multiplicar(numero):
    for i in range(1,11):#Iteramos del 1 al 10
        print(f"{numero} x {i} = {numero*i}")#Mostramos la tabla de multiplicar

#Solicitamos el numero al usuario
num = int(input("Ingrese el numero que desea saber su tabla de multiplicar: "))
tabla_multiplicar(num)#Llamamos a la funcion para mostrar la tabla de multiplicar


#Actividad 7 
#Creamos la funcion operaciones_basicas
def operaciones_basicas(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    if b!=0:#Verificamos que b no sea cero para evitar division por cero
      division = a/b
    else:#Si b es cero, mostramos un mensaje de error
       print("No se puede dividir por cero")
    resultados = (suma, resta, multiplicacion, division)#Devolvemos los resultados como una tupla
    return resultados

#Solicitamos los numeros al usuario
num1 = int(input("Ingrese la primer variable: "))
num2 = int(input("Ingrese la segunda variable: "))
total = operaciones_basicas(num1,num2)#Llamamos a la funcion y mostramos los resultados

print(f"Los resultados de sumar, restar, multiplicar y dividir {num1} y {num2}, son {total} respectivamente")


#Actividad 8
#Inicializamos las variables peso y altura
peso=0
altura=0
#Creamos la funcion calcular_imc
def calcular_imc(peso, altura):
    imc = round(peso / (altura ** 2), 2)#Calculamos el IMC y lo redondeamos a 2 decimales
    return imc
#Solicitamos el peso y la altura al usuario
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
resultado = calcular_imc(peso, altura)#Llamamos a la funcion y mostramos el resultado
print(f"Tu IMC es {resultado} kg/m2")


#Actividad 9
#Creamos la funcion celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius):
    F = (celsius*(9/5))+32#Formula para convertir Celsius a Fahrenheit
    return F
#Solicitamos la temperatura en grados Celsius al usuario
Temp_Celsius = float(input("Ingrese la temperatura en grados Celsius: "))
resultado_9 = celsius_a_fahrenheit(Temp_Celsius)#Llamamos a la funcion y mostramos el resultado
print(f"Su temperatura en grados Farenheit es:",resultado_9)

#Actividad 10
#Creamos la funcion calcular_promedio
def calcular_promedio(a, b, c):
    prom = (a + b + c)/3 #Calculamos el promedio de los tres numeros
    return prom
#Solicitamos los tres numeros al usuario
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
resultado10 = calcular_promedio(num1,num2,num3)#Llamamos a la funcion y mostramos el resultado
print(f"El promedio de los tres numeros ingresado es:",resultado10)