# Pedimos datos
hemisferio = input("¿En cuál hemisferio se encuentra? (N/S): ").lower()
mes = input("Ingrese el mes: ").lower()
dia = int(input("Ingrese el día: "))

# Función para determinar estación en hemisferio sur
if hemisferio == "s":
    if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
        estacion = "Verano"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "Otoño"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "Invierno"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"

if hemisferio == "n":
    if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
        estacion = "Invierno"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "Primavera"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "Verano"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
    
    print(f"Te encuentras en {estacion}")

