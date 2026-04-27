
import csv
import os

# Funciones para manejar el archivo CSV de la biblioteca escolar
def agregar_producto(Productos):
    with open("Biblioteca escolar.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
        escritor.writerow(Productos)

# Obtener la lista de productos desde el archivo CSV
def ObtenerProductos():
    productos = []
    if not os.path.exists("Biblioteca escolar.csv"):
        with open("Biblioteca escolar.csv", "w", newline="", encoding="utf-8") as archivo:
            crear_archivo = csv.DictWriter(archivo, fieldnames=(["Titulo", "Cantidad"]))
            crear_archivo.writeheader()
       

    with open("Biblioteca escolar.csv", newline="", encoding="utf-8") as archivo:
        lector_csv = csv.DictReader(archivo)

        for fila in lector_csv:
            productos.append(
                {
                    "Titulo": fila["Titulo"],
                    "Cantidad": int(fila["Cantidad"])
                }
            )
    return productos

# Verificar si un título ya existe en el catálogo
def existe_titulo(titulo):
    productos = ObtenerProductos()

    for p in productos:
        if p["Titulo"].lower() == titulo.strip().lower():
            return True
    return False

# Validar que la entrada sea un número entero positivo
def validar_numero(entrada):
    
    entrada_limpia = entrada.strip()
    if not entrada_limpia.isdigit():
        return False
    return True

# Funciones del menú de la biblioteca escolar
# Agregar libros al catálogo
def agregar_libros():

    print("---Agregar nuevos libros al catalogo---")
    Cantidad = input("Indique la cantidad de libros a ingresar: ")

    if not validar_numero(Cantidad):
        print("Cantidad invalida. Intente de nuevo.")
        print("-----------------------------")
        return
    
    Cantidad = int(Cantidad)

    if Cantidad > 0:
        for i in range(Cantidad):
            while True:
                Titulo = input(f"Ingrese el titulo del libro {i+1}: ").strip()

                if Titulo.lower() == "salir":
                    return

                if existe_titulo(Titulo):
                    print("El titulo ya existe en el catalogo. Intente de nuevo.")
                    print("Si desea salir escriba 'salir'")
                    print("-----------------------------")
                    continue

                ejemplares = input(f"Ingrese la cantidad de ejemplares para '{Titulo}': ")

                if not validar_numero(ejemplares):
                    print("Cantidad invalida. Intente de nuevo.")
                    print("-----------------------------")
                    continue

                ejemplares = int(ejemplares)

                agregar_producto({"Titulo": Titulo, "Cantidad": ejemplares})
                break
    print("Libros agregados exitosamente.")
    print("-----------------------------")

# Mostrar el catálogo de libros
def mostrar_catalogo():

    productos = ObtenerProductos()

    if not productos:
        
        print("El catalogo esta vacio.")
    else:
        print("-----------------------------")
        print("Catalogo de libros:")
        for producto in productos:
            print(f"Titulo: {producto['Titulo']}, Cantidad: {producto['Cantidad']}")
    print("-----------------------------")    

# Ingresar ejemplares de libros existentes
def ingresar_ejemplares():

    print("---Ingresar ejemplares de libros---")
    print("Ingrese el titulo del libro al que desea agregar ejemplares:")
    Titulo = input("Titulo: ").strip()

    if not existe_titulo(Titulo):
        print("El titulo no existe en el catalogo.")
        print("-----------------------------")
        return
    
    ejemplares = input(f"Ingrese la cantidad de ejemplares a agregar para '{Titulo}': ")
    if not validar_numero(ejemplares):
        print("Cantidad invalida. Intente de nuevo.")
        print("-----------------------------")
        return
    
    ejemplares = int(ejemplares)
    productos = ObtenerProductos()
    for producto in productos: #buscamos el producto en la lista
        if producto["Titulo"].lower() == Titulo.lower():
            producto["Cantidad"] += ejemplares #una vez encontrado le sumamos los ejemplares
            break
        print(f"Se han agregado {ejemplares} ejemplar/es a '{Titulo}'.")
        print("-----------------------------")

    with open("Biblioteca escolar.csv", "w", newline="", encoding="utf-8") as archivo: #reescribimos el archivo con los nuevos datos
        escritor = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
        escritor.writeheader()
        escritor.writerows(productos)

# Consultar disponibilidad de un libro
def consultar_disponibilidad():
    productos = ObtenerProductos()
    print("-----------------------------")
    print("Consultar disponibilidad de un libro")
    print("-----------------------------")

    if not productos:
        print("El catálogo está vacío. No hay libros para consultar.")
        print("-----------------------------")
        return
    
    Titulo_consulta = input("Ingrese el titulo del libro a consultar: ").strip()

    if not existe_titulo(Titulo_consulta):
        print("El titulo no existe en el catalogo.")
        print("-----------------------------")
        return

    for producto in productos: #buscamos el producto en la lista
        if producto["Titulo"].lower().strip() == Titulo_consulta.lower():
            cantidad = producto["Cantidad"] #una vez encontrado obtenemos la cantidad de ejemplares

            print(f"Disponibilidad del {producto['Titulo']}:")

            # Mostramos la disponibilidad segun la cantidad
            if cantidad > 0: 
                print(f"Hay {cantidad} ejemplares disponibles.")
            else:
                print("No hay ejemplares disponibles.")
            return
        
    print("El titulo no existe en el catalogo.")
    print("-----------------------------")   

# Listar libros agotados
def lista_de_agotados():
    productos = ObtenerProductos()
    print("-----------------------------")
    print("Lista de libros agotados:")
    agotados = [p for p in productos if p["Cantidad"] == 0] #creamos una lista con una condicion dentro donde busca cuales ejemplares tienen 0 cantidad

    if not agotados:
        print("No hay libros agotados.")
    else:
        for producto in agotados:
            print(f"- {producto['Titulo']}")
    print("-----------------------------")

# Agregar un nuevo título al catálogo
def agregar_titulo():
    print("-----------------------------")
    print("-Agregar un nuevo titulo al catalogo-")
    Titulo = input("Ingrese el titulo del libro: ").strip()

    if existe_titulo(Titulo):
        print("El titulo ya existe en el catalogo.")
        print("-----------------------------")
        return

    ejemplares = input(f"Ingrese la cantidad de ejemplares para '{Titulo}': ")

    if not validar_numero(ejemplares):
        print("Cantidad invalida. Intente de nuevo.")
        print("-----------------------------")
        return

    ejemplares = int(ejemplares)

    agregar_producto({"Titulo": Titulo, "Cantidad": ejemplares}) # Agregamos al final de la lista sin modificar el index
    print(f"Titulo '{Titulo}' agregado exitosamente con {ejemplares} ejemplares.") 
    print("-----------------------------")

# Actualizar ejemplares de un libro
def actualizar_ejemplares():
    print("-----------------------------")
    print("-Actualizar ejemplares de un libro-")
    Titulo = input("Ingrese el titulo del libro: ").strip()

    if not existe_titulo(Titulo):
        print("El titulo no existe en el catalogo.")
        print("-----------------------------")
        return

    productos = ObtenerProductos()
    for producto in productos:
        if producto["Titulo"].lower() == Titulo.lower(): #buscamos el producto en la lista
            print("1) Prestamo")
            print("2) Devolucion")
            accion = input("Ingrese la opcion deseada (1 o 2): ").strip()

            if accion == "1": #Prestamo
                if producto["Cantidad"] > 0:
                    producto["Cantidad"] -= 1 #Restamos 1 del ejemplar si esta en prestamo
                    print(f"Se ha prestado un ejemplar de '{Titulo}'.") 
                else:
                    print(f"No hay ejemplares disponibles para prestar de '{Titulo}'.")
            elif accion == "2": #Devolucion
                producto["Cantidad"] += 1 #Sumamos 1 del ejemplar si lo devuelven
                print(f"Se ha devuelto un ejemplar de '{Titulo}'.")
            else:
                print("Opcion invalida. Intente de nuevo.")
                print("-----------------------------")
                return
            break

    with open("Biblioteca escolar.csv", "w", newline="", encoding="utf-8") as archivo: #reescribimos el archivo con los nuevos datos
        escritor = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
        escritor.writeheader()
        escritor.writerows(productos)
    print("-----------------------------")

def menu_biblioteca():    
    while True:
        print("Bienvenido a la Biblioteca Escolar")
        print("/////MENU/////")
        print("1. Agregar libros")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catalogo")
        print("4. Consultar disponibilidad")
        print("5. Lista de agotados")
        print("6. Agregar titulo")
        print("7. Actualizar ejemplares")
        print("8. Salir")
        opcion = input("Seleccione una opcion (1-8): ")
        match opcion:
            case "1":
                agregar_libros()
            case "2":
                ingresar_ejemplares()
            case "3":
                mostrar_catalogo()
            case "4":
                consultar_disponibilidad()
            case "5":
                lista_de_agotados()
            case "6":
                agregar_titulo()
            case "7":
                actualizar_ejemplares()
            case "8":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida, por favor intente de nuevo.")
                print("-----------------------------")


menu_biblioteca()