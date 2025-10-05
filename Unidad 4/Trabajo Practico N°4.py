#Activdad 1

for i in range(1,101):#Este for hace que la variable i inicie en 1 y termine en 100
    print(i,end=" ")  #Aca los imprimimos uno por uno

#Activdad 2

numero = (input("Ingrese un numero entero: ")) #Pedimos al usuario que ingrese un numero

print("La cantidad de digitos que tiene el numero es",len(numero)) #Con la funcion len logramos que imprima la cantidad de digitos ya que el numero ingresado es tomado como una cadena de texto

#Actividad 3

numero1=int(input("Ingrese el numero inicial: "))#Pedimos al usuario que ingrese el numero inicial
numero2=int(input("Ingrese el numero final: "))#Pedimos al usuario que ingrese el numero final
Sumatoria = 0

#con estos if lo que hacemos es ver cual es mas grande para ver si tenemos que modificar el paso hacia atras o que vaya hacia adelante
#Luego de ingresar a un if, tenemos los for que iteran los numeros comprendidos entre los valores ingresados
#Cada valor se va sumando por cada vuelta del for hasta llegar a la sumatoria de todos los valores comprendidos excluyendo los valores ingresados
if numero1 >= 0 and numero2 >=0 and numero2 > numero1: 
    for i in range(numero1+1,numero2+1):
        Sumatoria = Sumatoria + i
        print(Sumatoria)
elif numero1 >= 0 and numero2 >=0 and numero1 > numero2:
    for i in range(numero1+1,numero2+1,-1):
        Sumatoria = Sumatoria + i
        print(Sumatoria)
elif numero1 <= 0 and numero2 <= 0 and numero2 > numero1:
     for i in range(numero1-1,numero2+1):
        Sumatoria = Sumatoria + i
        print(Sumatoria)
elif numero1 <= 0 and numero2 <= 0 and numero1 > numero2:
     for i in range(numero1-1,numero2-1,-1):
        Sumatoria = Sumatoria + i
        print(Sumatoria)

print("La sumatoria de todos los numeros entre",numero1,"y",numero2,"es",Sumatoria)

#Actividad 4
#Inicializamos variables
numero = 1
sumatoria = 0
while numero !=0: #Mientras el numero sea diferente de 0 el while funcionara
    numero = int(input("Ingrese un numero entero: "))
    sumatoria += numero

#Indicamos al usuario que si quiere salir del while debe ingresar el 0
    print("Para salir ingrese el numero 0")
    print("Para continuar con la suma de numeros enteros ingrese cualquier numero menos el 0")

print("El total de la sumatoria de numeros enteros es",sumatoria)

#Actividad 5
import random #llamamos la biblioteca de numeros aleatoreos

print("Bienvenido al juego donde tienes que adivinar un numero elegido al azar entre 0 y 9")
print("Una vez adivinado el numero el juego termina. Buena suerte")

#Ingresamos la seleccion de un numeros aleatorios entre 0 y 9
numero_aleatorio = random.randint(0,9)
#Inicializamos las variables
numero = 10
intentos = 0

#Usamos un while porque es indefinido la cantidad de veces que funcionara el programa
while numero_aleatorio != numero:
   #Pedimos al usuario ingresar un numero
    numero = int(input("Ingrese su numero: "))
    #Condicionamos que el numero ingresado por el usuario este dentro del rango pedido
    if numero >=10 or numero <= -1:
        print("Su numero esta fuera de rango")
    #Avisamos al usuario que el numero ingresado no es correcto
    if numero != numero_aleatorio:
        print("Numero equivocado, intente de nuevo")
    #colocamos un contador hasta que adivine el numero
    intentos += 1 

print("Cantidad de intentos:",intentos)#Imprimimos la cantidad de intentos

#Actividad 6

for i in range(100,-1,-1): #Este for nos permite iniciar del 100 hasta el 0 con un paso de -1 es decir hacia atras 
    if i % 2 == 0: #El if en cambio nos verifica que numero es par
        print(f"{i}") #Aca imprimos a cada numero par

#Actividad 7

#Pedimos al usuario que ingrese un numero
print("Ingrese un numero para calcular la suma entre los numeros comprendidos entre 0 y su numero")
print("El numero ingresado tiene que ser entero positivo")
numero = int(input(""))
#Inicalizamos variable
sumatoria = 0

#Este while restringe el ingreso de numeros enteros negativos
while numero < 0:
    print("Ha ingresado un numero entero negativo. Ingrese porfavor un numero entero positivo")
    #Aca actualizamos la variable num para que sea correcta
    numero = int(input())

#Con este for hacemos la sumatoria entre el numero 0 y el numero ingresado
for i in range(0,numero+1):
    sumatoria += i

#En este print pedimos que nos muestre el resultado
print("El total de la sumatoria es:",sumatoria)

#Actividad 8
#Inicilizamos variables
numeros_positivos = 0
numeros_negativos = 0
numeros_pares = 0
numero_impares = 0

#pedimos al usuario a traves del for que ingrese 100 numeros
for i in range(1,101):
    print("Ingrese el numero",i,":" ,end="")
    numero = int(input())

#Con estos if podemos lograr contar dependiendo que condicion cumple cada numero ingresado si es par, impar, negativo o positivo
    if numero > 0:
        numeros_positivos += 1
    if numero < 0:
        numeros_negativos += 1
    if numero % 2 == 0:
        numeros_pares += 1
    if numero % 2 != 0:
        numero_impares += 1

#Imprimimos resultados
print("Numeros positivos:",numeros_positivos)
print("Numeros negativos:",numeros_negativos)
print("Numeros pares:",numeros_pares)
print("Numeros impares:",numero_impares)

#Actividad 9
#Inicializamos
sumatoria = 0
cont = 0

#Pedimos al usuario ingresar 100 numeros
for i in range(1,101):
    print("Ingrese el numero",i,":",end="")
    numero = int(input(""))

#Usamos una sumatoria para obtener el total de la suma entre los numeros ingresados y colocamos un contador
    sumatoria += numero
    cont += 1

#Calculamos la media
media = sumatoria / cont 

#Imprime el resultado
print("La media de los numeros ingresados es:",media)

#Actividad 10
#Inicializamos y pedimos al usuario ingresar el numero que desea invertir
numero = int(input("Ingrese el numero que desea invertir:")) #Por ejemplo: 735
digito=0
numero_invertido=0

#La condicion del while nos permitira salir del bloque cuando el ultimo digito a dividir sea 0
while numero > 0:
        #Con este calculo logramos obtener el ultimo digito del numero ingresado. Por ejemplo 735 % 10 = 5 obtenemos el digito 5
        digito = numero % 10
        #Aca guardamos el digito obtenido anteriormente
        numero_invertido = numero_invertido * 10 + digito # Ejemplo: numero invertido = 0 * 10 + 5
        #Luego truncamos el numero para iniciar el bloque con el numero truncado
        numero = numero // 10 #Ej: 735 //10 = 73 y con este numero inicia el bloque de nuevo hasta que 0//10=0  

#Este bloque de codigo se repetira dependiendo de la cantidad de digitos ingresados
print("El numero invertido es:",numero_invertido)

