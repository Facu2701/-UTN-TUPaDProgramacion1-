palabra = input("Ingrese una frase o palabra: ")

ultima = palabra[-1]

if ultima in "aeiou":
    print(f"{palabra}!")
else:
    print(palabra)
