#Actividad 1
with open("Productos.txt", "w") as archivo: #Creamos el archivo y escribimos los datos iniciales
    archivo.write("Nombre,Precio,Cantidad\n")
    archivo.write("Manzanas,1.50,100\n")
    archivo.write("Peras,1.20,150\n")
    archivo.write("Naranjas,0.80,200\n")

print("\n")

#Actividad 2
with open("Productos.txt", "r") as archivo: #Leemos y mostramos el contenido del archivo
    encabezado = archivo.readline().strip().split(",")
    print(encabezado)

    Producto1 = archivo.readline().strip().split(",")
    print(Producto1)

    Producto2 = archivo.readline().strip().split(",")
    print(Producto2)

    Producto3 = archivo.readline().strip().split(",")
    print(Producto3)

print("\n")
#Actividad 3

with open("Productos.txt", "a") as archivo: #Agregamos un nuevo producto al archivo
    print("Ingrese los datos del nuevo producto(Nombre, precio, cantidad):") 
    nuevo_producto = input()# Ejemplo de entrada: Uvas,2.00,120
    archivo.write(nuevo_producto + "\n") # Agregamos el nuevo producto al archivo
    print("Producto agregado exitosamente.")

with open("Productos.txt", "r") as archivo: #Mostramos el contenido actualizado del archivo
    contenido = archivo.read() #Leemos todo el contenido del archivo
    print("Contenido actualizado del archivo:")
    print(contenido)

print("\n")

#Actividad 4

productos = [] #Lista para almacenar los productos

with open("productos.txt", "r") as archivo: #Leemos los productos y los almacenamos en la lista
    encabezado = archivo.readline()
    for linea in archivo: #Leemos cada línea del archivo
        nombre, precio, cantidad = linea.strip().split(",") #Separamos los datos por comas y los asignamos a variables
        producto = { 
            "Nombre": nombre,
            "Precio": float(precio),
            "Cantidad": int(cantidad)
        }
        productos.append(producto)#Agregamos el producto a la lista

print(productos)

print("\n")

print("Actividad 5")

producto = input("Ingrese el nombre del producto a buscar: ").strip().lower() #Solicitamos el nombre del producto a buscar
for p in productos:#Buscamos el producto en la lista
    if p["Nombre"].lower() == producto:#Comparamos el nombre del producto ignorando mayúsculas y minúsculas
        print("Producto encontrado:")
        print(f"Nombre: {p['Nombre']}, Precio: {p['Precio']}, Cantidad: {p['Cantidad']}") #Mostramos los detalles del producto

if not p in productos: #Si el producto no se encuentra en la lista
    print("Producto no encontrado.")

print("\n")

print("Actividad 6")

with open("Productos.txt", "w") as archivo: #Reescribimos el archivo con los datos actualizados
    # Escribimos el encabezado
    archivo.write("Nombre,Precio,Cantidad\n")
    
    # Escribimos cada producto en una línea
    for producto in productos:
        linea = f"{producto['Nombre']},{producto['Precio']},{producto['Cantidad']}\n"
        archivo.write(linea)
        print(f"{linea.strip()}") #Mostramos cada línea escrita en el archivo