
#Actividad 1

Precios_frutas = {'Banana': 1200, 'Anana' : 2500, 'Melón' : 3000, 'Uva' : 1450}
#Añadir frutas 'naranja'=1200, 'Manzana'=1500, 'Pera'=2300
print(Precios_frutas)
Precios_frutas["Naranja"] = 1200
Precios_frutas["Manzana"] = 1500
Precios_frutas["Pera"] = 2300
print(Precios_frutas)


#Actividad 2
#Siguiendo con el diccionario Precios_frutas, actualizar los precios de las siguientes frutas:
#Banana = 1330
#Manzana = 1700
#Melón = 2800
Precios_frutas["Banana"]= 1330
Precios_frutas["Manzana"] = 1700
Precios_frutas["Melón"] = 2800
print(Precios_frutas)

#Actividad 3
#Siguiendo con el diccionario Precios_frutas, crear una lista que contenga unicamente las frutas sin los precios
frutas = ["Banana", "Anana", "Melón", "Uva", "Naranja", "Manzana", "Pera"]
print(frutas)

#Actividad 4
#Programa que permita almacenar y consultar número telefónicos
contactos={}

#Ingreso de 5 contactos
for i in range(5):
    nombre =input("Ingrese el nombre de la persona: ")
    numero_telefono= int(input("Ingrese el numero de telefono: "))
    #Guardamos los datos en el diccionario
    contactos[nombre] = numero_telefono

#Mostramos la lista de contactos    
print("\nLista de contactos: ") 
for nombre, numero in contactos.items():
    print(f"{nombre} : {numero}")

#Busqueda de un contacto
nombre_buscado = input("Ingrese el nombre que desea buscar: ")
if nombre_buscado in contactos: #Verificamos si el nombre existe en el diccionario
    print(f"El numero de {nombre_buscado} es {contactos[nombre_buscado]}")
else:
    print("Ese nombre no se encuentra en la lista")
    


#Actividad 5
from collections import Counter
#Programa que permita ingresar una frase y luego muestre las palabras únicas y la frecuencia de cada palabra
texto = input("Ingrese una frase: ")
lista_texto = texto.split()#Dividimos el texto en palabras usando el espacio como separador
palabras_unicas= set()#Conjunto para almacenar las palabras únicas
palabras_unicas.update(lista_texto)#Agregamos las palabras de la lista al conjunto (automáticamente elimina duplicados)
print (palabras_unicas)#Mostramos las palabras únicas   

#Contamos la frecuencia de cada palabra usando Counter
frecuencia = Counter(lista_texto)
print(frecuencia)

#Actividad 6
Libreta = {}
Alumnos = []
Notas = []
for i in range(3):#Cantidad de alumnos
    Nombre6 = input("Ingrese el nombre del alumno: ")
    Alumnos.append(Nombre6)#Agregamos el nombre a la lista de alumnos
    notas_alumno=[]#Lista para almacenar las notas del alumno
    for e in range(3):#Cantidad de notas por alumno
        Nota = float(input("Ingrese las notas del alumno: "))
        notas_alumno.append(Nota)#Agregamos la nota a la lista de notas del alumno
        print (notas_alumno)
    Notas.append(notas_alumno)#Guardamos la lista de notas del alumno en la lista de notas

#Creamos el diccionario Libreta usando zip para emparejar alumnos con sus notas
Libreta = dict(zip(Alumnos,Notas))
print (Libreta)

#Actividad 7
#Conjuntos de alumnos que aprobaron los parciales
Parcial_1 = {1,5,4,7,8,9,6}
Parcial_2 = {3,4,9,2,1,10,11}

#Alumnos que aprobaron las 2 materias
Aprobados = Parcial_1 & Parcial_2
print(f"Los alumnos que aprobaron los 2 parciales son: {Aprobados}")

#Alumnos que aprobaron solo uno de los 2
aprobados_solo_uno = Parcial_1 ^ Parcial_2
print(f"Los alumnos que aprobaron por lo menos un parcial son: {aprobados_solo_uno}")

#Alumnos que aprobaron al menos un parcial
aprobados_al_menos_uno = Parcial_1 | Parcial_2
print(f"Los alumnos que aprobaron al menos un parcial son: {aprobados_al_menos_uno}")


#Actividad 8
Inventario = {'Fideos': 100, 'Arroz': 250, 'Lenteja' : 75, 'Atun' : 60}
while True:#Bucle infinito hasta que el usuario decida salir
    print("///MENU///")
    print("----------")
    print("1) Consultar stock")
    print("2) Ingresar unidades al stock")
    print("3) Agregar un nuevo producto")
    print("4) Salir")

    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:#Consultar stock
        producto = input("Ingrese el nombre del producto que quieres consultar: ")
        if producto in Inventario:#Verificamos si el producto existe en el inventario
            print(f"El stock de {producto} es: {Inventario[producto]}")
        else:
            print(f"El producto ingresado no se encuentra en el inventario")
    
    if opcion ==2:#Ingresar unidades al stock
        producto = input("Ingrese el nombre del producto que quieres modificar su stock: ")
        if producto in Inventario:#Verificamos si el producto existe en el inventario
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))
            Inventario[producto] += cantidad#Actualizamos el stock sumando la cantidad ingresada
            print(f"El stock de {producto} ahora es {Inventario[producto]}")
    else:
        print(f"El producto ingresado no se encuentra en el inventario")
    
    if opcion == 3:#Agregar un nuevo producto
        Nuevo_producto = input("Ingrese el producto nuevo: ")
        cantidad = int(input("Ingrese su cantidad: "))
        Inventario[Nuevo_producto] = cantidad#Agregamos el nuevo producto al inventario
        print(f"El producto {Nuevo_producto} con {cantidad} unidades de stock, ha sido ingresado con exito")

    if opcion == 4:#Salir
        print("Hasta luego!")
        break


#Actividad 9

Agenda = {
    ("Lunes","9:00") : "Gimnasio",
    ("Martes","10:00") : "Clase de Matemática",
    ("Miércoles","11:00") : "Clase de Inglés",
    ("Jueves" , "16:00") : "Gimnasio",
    ("Viernes","12:00") : "Clase de Física"
        }
#Función para consultar la actividad en un día y hora específicos
def consultar_actividad(dia, hora):
    clave = (dia, hora)
    if clave in Agenda:#Verificamos si la clave existe en la agenda
        return f"A las {hora} del {dia} tenés: {Agenda[clave]}"
    else:
        return f"No hay actividades registradas el {dia} a las {hora}."

print(consultar_actividad("Lunes", "9:00"))#Actividad: Gimnasio
print(consultar_actividad("Miércoles", "11:00"))#Actividad: Clase de Inglés

#Actividad 10
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

invertido = {}
#Invertimos las claves y valores del diccionario original
for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)