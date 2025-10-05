#Primer parcial
#Biblioteca escolar
#Catalogo de libro


#Listas
titulos = []
ejemplares = []

#Inicializamos
opcion = 1
i=0

#Iniciamos el while
while (1 <= opcion <= 7):
    print("\n--- MENÚ ---")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares")
    print("8. Salir")

#Pedimos al usuario que ingrese la opcion deseada
    opcion = int(input("Elegí una opción: "))

#Opcion 1
    if opcion == 1:
        print("1. Ingresar títulos")
        n = int(input("¿Cuántos títulos querés ingresar? ")) #Ingresamos la cantidad inicial de titulos
        for i in range(n): #Usamos este for para ingresar la cantidad de titulos ya dichos
            nombre = input(f"Ingresá el título {i+1}: ") #este bloque se repetira hasta colocar los nombres de la cantidad dicha
            titulos.append(nombre) 
            ejemplares.append(0)
         

#Opcion 2
    elif opcion == 2:
            print("2. Ingresar ejemplares")
            for i in range(len(titulos)): #Este for nos sirve para leer la lista titulos y tomar el rango de la lista
                cantidades = int(input(f"Ingrese la cantidad de ejemplares {titulos[i]}: ")) #Aca se ingresa las cantidades de cada ejemplar
                ejemplares[i]= cantidades

    elif opcion == 3:
        print("3. Mostrar catálogo")
        for i in range(len(titulos)):#Se muestra cada elemento de la lista 
            print(titulos[i])

    elif opcion == 4:
        print("4. Consultar disponibilidad") 
        Libro = input("Titulo del libro: ") #Ingresamos el nombre del libro que queremos averiguar si esta disponible
        if Libro in titulos:
            idex = titulos.index(Libro) #buscamos su ubicacion en la lista titulos
            print(f"'{Libro}' tiene {ejemplares[idex]} ejemplares")#sincronizamos el libro con la cantidad de ejemplares

    elif opcion == 5:
          print("5. Listar agotados")
          agotados = [titulos[i] for i in range(len(ejemplares)) if ejemplares[i] == 0]#creamos una lista con una condicion dentro donde busca cuales ejemplares tienen 0 cantidad
          if agotados:#si existe una lista con libros agotados, a continuacion los imprimira
            print("Libros agotados:")
            for libro in agotados:
                print(f"- {libro}")
    
    elif opcion == 6:
        print("6. Agregar título") 
        nuevo = input("Ingrese el título del libro: ") #Ingresamos un libro nuevo
        cantidad_nuevo = int(input("Ingrese la cantidad de ejemplares: ")) #Ingresamos la cantidades
        titulos.append(nuevo) #Agregamos al final de la lista sin modificar el index
        ejemplares.append(cantidad_nuevo)#Agregamos al final de la lista sin modificar el index

    elif opcion == 7:
        print("7. Actualizar ejemplares")
        libro = input("Titulo: ") #Pedimos el nombre del libro
        if libro in titulos: #Si el libro se encuentra en los titulos
         idex = titulos.index(libro) #localizamos su index dentro de la lista
         print("1) Prestamo")
         print("2) Devolucion")
         accion = int(input("Ingrese la opcion deseada:")) #Damos a elegir una de las opciones mostradas
         if accion == 1:    
             ejemplares[idex]=ejemplares[idex]-1 #Restamos 1 del ejemplar si esta en prestamo
         elif accion == 2:
             ejemplares[idex]=ejemplares[idex]+1 #Sumamos 1 del ejemplar si lo devuelven
             
        





           


    
   