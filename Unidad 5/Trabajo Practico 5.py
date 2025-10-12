# Actividad 1
from statistics import mean
max_nota= 0
min_nota= 10
# Creamos una lista con las notas de 10 alumnos
Notas = [6.2,7.8,5.4,9.6,8.3,4.5,3.2,6.6,7.2,10]

# Imprimimos las notas una por una usando un bucle for
for i in Notas:
    print(i)

# Calculamos la media de las notas usando la función
mean(Notas)
print ("La media es: ", mean(Notas))

for aux in Notas:
    if aux > max_nota:
        max_nota = aux
    if aux < min_nota:
        min_nota = aux

print("La nota máxima es: ", max_nota)
print("La nota mínima es: ", min_nota)

# Actividad 2
# Crear una lista vacía para almacenar los nombres de productos
Productos = []
opcion = 0
while opcion != 3:
    print ("////MENU////")
    print("Eliga la opcion que desea realizar:")
    print("1- Crear lista de productos")
    print("2- Eliminar un producto de la lista")
    print("3- Salir")
    opcion = int(input("Ingrese su opción (1, 2 o 3): "))

    if opcion == 1:
    # Pedir al usuario que ingrese 5 nombres de productos y agregarlos a la lista
        for i in range(5):
            producto = input("Ingrese el nombre del producto: ")
            Productos.append(producto) # Agregar el producto a la lista
            Productos.sort() # Ordenar la lista alfabéticamente
            print("Lista de productos actualizada: ", Productos) # Imprimir la lista actualizada
    elif opcion == 2:
        producto_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
        if producto_eliminar in Productos:
            Productos.remove(producto_eliminar)
            print("Producto eliminado. Lista de productos actualizada: ", Productos)
        else:
            print("El producto no se encuentra en la lista.")
    elif opcion == 3:
        print("Saliendo del programa...")  

# Actividad 3
import random
# Crear una lista vacía para almacenar los números aleatorios
Lista = []
# Generar 15 números aleatorios entre 1 y 100 y agregarlos a la lista
for i in range(15):
    numero = random.randint(1,100)
    Lista.append(numero)
    # Imprimir la lista completa
print("Lista de números aleatorios: ", Lista)
# Numeros pares e impares
# Mostrar cuantos numeros son pares e impares
pares = [num for num in Lista if num % 2 == 0]
impares = [num for num in Lista if num % 2 != 0]
print("Cantidad de números pares: ", len(pares))
print("Cantidad de números impares: ", len(impares))

#Actividad 4
# Lista de numeros repetidos
Numeros = [1, 3, 5, 3, 7, 1, 9, 5, 3]

Num_sinrepetir = []
for i in Numeros:
    if i not in Num_sinrepetir:
        Num_sinrepetir.append(i)
print("Lista sin números repetidos: ", Num_sinrepetir)

# #Actividad 5
#Lista de alumnos
Clase = ["Juan", "Ana", "Luis", "Maria", "Carlos","Sofia", "Elias", "Lucia"]
print("Lista de alumnos: ",Clase)
#Pedimos al usuario si quiere ingresar un alumno
print("///MENU///")
print("1- Agregar alumno")
print("2- Eliminar alumno")
print("3- Salir")
opcion = int(input("Ingrese la opcion deseada: "))
while opcion == 1:
    alumno = input("Ingrese el nombre del alumno que desea agregar : ")
    Clase.append(alumno)
    print("Lista actualizada: ", Clase)
    print("///MENU///")
    print("1- Agregar alumno")
    print("2- Eliminar alumno")
    print("3- Salir")
    opcion = int(input("Ingrese la opcion deseada: "))
while opcion == 2:
    alumno = input("Ingrese el nombre del alumno que desea eliminar: ")
    Clase.remove(alumno)
    print("Lista actualizada: ", Clase)
    print("///MENU///")
    print("1- Agregar alumno")
    print("2- Eliminar alumno")
    print("3- Salir")
    opcion = int(input("Ingrese la opcion deseada: "))

#Actividad 6
#Lista de numeros dados
Numeros = [2, 15, 27, 56, 37, 48, 95]   

#For para la linea
for i in range(0, 1):
    for j in range(len(Numeros)): #For para las columna
        if i != j:
            Numeros[i],Numeros[j]=Numeros[j],Numeros[i]
            print (Numeros)

#Actividad 7
#Listas anidadas
temperaturas = [
    [12, 25],  # Lunes
    [14, 28],  # Martes
    [10, 26],  # Miércoles
    [13, 29],  # Jueves
    [15, 31],  # Viernes
    [11, 24],  # Sábado
    [9, 22]    # Domingo
    ]

minimas = []
for dia in temperaturas:
    minimas.append(dia[0])
maximas = []    
for dia in temperaturas:
    maximas.append(dia[1])

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

print("Promedio de mínimas:", promedio_min)
print("Promedio de máximas:", promedio_max)

amplitud_termica = []
for i in range(len(temperaturas)):
    amplitud = maximas[i] - minimas[i]
    amplitud_termica.append(amplitud)
    print(amplitud_termica)

for i in range(len(temperaturas)-1):
    if amplitud_termica[i] > amplitud_termica[i+1]:
        amplitud_max = amplitud_termica[i]
        print ("La amplitud termina maxima es: ",amplitud_max)

#Actividad 8
# #Matriz de los alumnos con las notas 5x3
Libreta = [
    [60,85,75],
    [52,77,95],
    [86,72,40],
    [35,58,96],
    [64,29,86],
]
Total_notas1 = 0
Total_notas2 = 0
Total_notas3 = 0
Total_notas4 = 0
Total_notas5 = 0
#Promedio de cada estudiante
for n in Libreta[0]:
    Total_notas1 += n # Suma de las notas del alumno 1, es decir, la suma de los elementos de la primera sublista
    prome_alumno1 = Total_notas1/len(Libreta[0])
    
for n in Libreta[1]:
    Total_notas2 += n
    prome_alumno2 = Total_notas2/len(Libreta[1])

for n in Libreta[2]:
    Total_notas3 += n
    prome_alumno3 = Total_notas3/len(Libreta[2])

for n in Libreta[3]:
    Total_notas4 += n
    prome_alumno4 = Total_notas4/len(Libreta[3])

for n in Libreta[4]:
    Total_notas5 += n
    prome_alumno5 = Total_notas5/len(Libreta[4])
#Promedio de cada alumno
print("Promedio del alumno 1: ",prome_alumno1)
print("Promedio del alumno 2: ",prome_alumno2)
print("Promedio del alumno 3: ",prome_alumno3)
print("Promedio del alumno 4: ",prome_alumno4)
print("Promedio del alumno 5: ",prome_alumno5)
#Calculo de la suma de las notas de cada materia
total_materia1 = 0
total_materia2 = 0
total_materia3 = 0
for i in Libreta: # Recorre cada sublista (alumno) en la lista principal (Libreta)
    total_materia1 += i[0] # Suma el primer elemento (nota de la materia 1) de cada sublista
       
for j in Libreta:
    total_materia2 += j[1] # Suma el segundo elemento (nota de la materia 2) de cada sublista
        
for k in Libreta:
    total_materia3 += k[2] # Suma el tercer elemento (nota de la materia 3) de cada sublista
# suma de las notas de cada materia
print (total_materia1)
print (total_materia2)
print (total_materia3)

#Promedio de cada materia
promedio_materia1 = total_materia1 / len(Libreta)
promedio_materia2 = total_materia2 / len(Libreta)
promedio_materia3 = total_materia3 / len(Libreta)
print("Promedio de la materia 1: ", promedio_materia1)
print("Promedio de la materia 2: ", promedio_materia2)
print("Promedio de la materia 3: ", promedio_materia3)

#Actividad 9
#Matriz para el juego TaTeTi
TaTeTi = [
      ['-', '-', '-'],
      ['-', '-', '-'],
      ['-', '-', '-']
    ]

#Ingresar turnos



for turno in range(9):
    if turno % 2 == 0: # Turno del jugador X en los turnos pares
        jugador = 'X'
    else:
        jugador = 'O' # Turno del jugador O en los turnos impares
    print(f"Turno del jugador {jugador}") # Indicar de quién es el turno
    fila = int(input("Ingrese la fila (0, 1 o 2): ")) # Pedir al jugador que ingrese la fila y columna donde quiere colocar su ficha
    columna = int(input("Ingrese la columna (0, 1 o 2): "))
    if TaTeTi[fila][columna] == '-': # Verificar si la posición está vacía
        TaTeTi[fila][columna] = jugador 
    else: # Si la posición ya está ocupada, pedir al jugador que ingrese otra posición
        print("Esa posición ya está ocupada. Intente de nuevo.")
    for fila in TaTeTi: # Imprimir el tablero después de cada turno
        print(fila)

#Actividad 10
#Matriz de productosxventas 4x7
Productos = [
    [5, 7, 15, 20, 10, 2, 14],
    [5, 17, 22, 4, 15, 30, 21],
    [22, 14, 15, 31, 28, 4, 2],
    [7, 16, 13, 19, 24, 0, 26]
]
#Producto 1 total vendido
total_producto1 = 0
for i in Productos[0]:
    total_producto1 += i
print("Total vendido del producto 1: ", total_producto1)
#Producto 2 total vendido
total_producto2 = 0
for i in Productos[1]:
    total_producto2 += i
print("Total vendido del producto 2: ", total_producto2)
#Producto 3 total vendido
total_producto3 = 0
for i in Productos[2]:
    total_producto3 += i
print("Total vendido del producto 3: ", total_producto3)
#Producto 4 total vendido
total_producto4 = 0
for i in Productos[3]:
    total_producto4 += i
print("Total vendido del producto 4: ", total_producto4)

#Dia con mayor venta
dia1 = 0
dia2 = 0
dia3 = 0
dia4 = 0
dia5 = 0
dia6 = 0
dia7 = 0
for i in range(len(Productos)): #Recorre las filas
    dia1 += Productos[i][0]
    dia2 += Productos[i][1]
    dia3 += Productos[i][2]
    dia4 += Productos[i][3]
    dia5 += Productos[i][4]
    dia6 += Productos[i][5]
    dia7 += Productos[i][6]
if dia1 > dia2 and dia1 > dia3 and dia1 > dia4 and dia1 > dia5 and dia1 > dia6 and dia1 > dia7:
    print("El día con mayor venta es el día 1 con: ",dia1)
elif dia2 > dia1 and dia2 > dia3 and dia2 > dia4 and dia2 > dia5 and dia2 > dia6 and dia2 > dia7:
    print("El día con mayor venta es el día 2 con: ",dia2)
elif dia3 > dia1 and dia3 > dia2 and dia3 > dia4 and dia3 > dia5 and dia3 > dia6 and dia3 > dia7:
    print("El día con mayor venta es el día 3 con: ",dia3)
elif dia4 > dia1 and dia4 > dia2 and dia4 > dia3 and dia4 > dia5 and dia4 > dia6 and dia4 > dia7:
    print("El día con mayor venta es el día 4 con: ",dia4)
elif dia5 > dia1 and dia5 > dia2 and dia5 > dia3 and dia5 > dia4 and dia5 > dia6 and dia5 > dia7:
    print("El día con mayor venta es el día 5 con: ",dia5)
elif dia6 > dia1 and dia6 > dia2 and dia6 > dia3 and dia6 > dia4 and dia6 > dia5 and dia6 > dia7:
    print("El día con mayor venta es el día 6 con: ",dia6)
else:
    print("El día con mayor venta es el día 7 con: ",dia7)

#Producto mas vendido de la semana
if total_producto1 > total_producto2 and total_producto1 > total_producto3 and total_producto1 > total_producto4:
    print("El producto más vendido de la semana es el producto 1 con: ",total_producto1)
elif total_producto2 > total_producto1 and total_producto2 > total_producto3 and total_producto2 > total_producto4:
    print("El producto más vendido de la semana es el producto 2 con: ",total_producto2)
elif total_producto3 > total_producto1 and total_producto3 > total_producto2 and total_producto3 > total_producto4:
    print("El producto más vendido de la semana es el producto 3 con: ",total_producto3)
else:
    print("El producto más vendido de la semana es el producto 4 con: ",total_producto4)