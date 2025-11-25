from Trabajo_Practico_9 import suma_n_digitos, contar_bloques, contar_digito

from Trabajo_Practico_9 import es_palindromo
from Trabajo_Practico_9 import decimal_a_binario
from Trabajo_Practico_9 import calculo_potencia
from Trabajo_Practico_9 import fibonacci
from Trabajo_Practico_9 import factorial

#Actividad 1
# Calcular el factorial de un número
numero = int(input("Ingrese un número para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#Actividad 2
# Calcular el número de Fibonacci en una posición dada
posicion = int(input("Ingrese un número para calcular su número de Fibonacci: "))
resultado = fibonacci(posicion)
print(f"El número de Fibonacci en la posición {posicion} es {resultado}")

for elemento in range(posicion + 1):
    print(f"Fibonacci({elemento}) = {fibonacci(elemento)}")

# Actividad 3
# Calcular la potencia de una base elevada a un exponente    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = calculo_potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")

# Actividad 4
# Convertir un número decimal a binario
numero_decimal = int(input("Ingrese un número decimal para convertir a binario: "))
resultado_binario = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es {resultado_binario}")

# Actividad 5
# Verificar si una cadena es un palíndromo
cadena = input("Ingrese una cadena para verificar si es un palíndromo: ")
if es_palindromo(cadena):
    print(f"La cadena '{cadena}' es un palíndromo.")
else:
    print(f"La cadena '{cadena}' no es un palíndromo.")

# Actividad 6
# Calcular la suma de los dígitos de un número
numero = int(input("Ingrese un número para calcular la suma de sus dígitos: "))
resultado = suma_n_digitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}")

# Actividad 7
# Contar la cantidad de bloques necesarios para una base dada
base = int(input("Ingrese la base del bloque: "))
resultado = contar_bloques(base)
print(f"En total se necesitan {resultado} bloques para una base de {base}")
    
# Actividad 8
# Contar la cantidad de veces que aparece un dígito específico en un número
numero = int(input("Ingrese un número para contar un dígito específico: "))
digito = int(input("Ingrese el dígito que desea contar: "))
resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")