from email.mime import base

# Trabajo_Practico_9.py
# Implementación de funciones recursivas

#Actividad 1
def factorial (n):
    """Calcula el factorial de un número n de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
#Actividad 2
def fibonacci (n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Actividad 3
def calculo_potencia (base, exponente):
    """Calcula la potencia de una base elevada a un exponente de forma recursiva."""
    if exponente == 0:
        return 1
    else:
        return base * calculo_potencia(base, exponente - 1)
    
#Actividad 4
def decimal_a_binario (n):
    """Convierte un número decimal n a su representación binaria de forma recursiva."""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

#Actividad 5
def es_palindromo (cadena):
    """Verifica si una cadena es un palíndromo de forma recursiva."""
    cadena = cadena.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    if len(cadena) <= 1:
        return True
    elif cadena[0] != cadena[-1]:
        return False
    else:
        return es_palindromo(cadena[1:-1])

#Actividad 6
def suma_n_digitos (n):
    """Calcula la suma de los dígitos de un número n de forma recursiva."""
    if n == 0:
        return 0
    else:
        return n % 10 + suma_n_digitos(n // 10)
    

#Actividad 7
def contar_bloques(n):
    if n <= 0:
        return 0
    else: 
        return n + contar_bloques(n - 1)

#Actividad 8
def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito específico en un número dado de forma recursiva."""
    if numero == 0:
        return 0
    else:
        cuenta = 1 if numero % 10 == digito else 0
        return cuenta + contar_digito(numero // 10, digito)
    
if __name__ == "__main__":
# Pruebas rápidas de las funciones
  print("Factorial de 5:", factorial(5))
  print("Fibonacci de 7:", fibonacci(7))
  print("2 elevado a la 3:", calculo_potencia(2, 3))
  print("Decimal 10 a binario:", decimal_a_binario(10))
  print("Verificar que la palabra es un palíndromo:", es_palindromo("anilina"))
  print("Suma de dígitos de 1234:", suma_n_digitos(1234))
  print("Contar bloques para base 4:", contar_bloques(4))
  print("Contar dígito 3 en número 133233:", contar_digito(133233, 3))
  