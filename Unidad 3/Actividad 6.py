from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
media= mean(numeros_aleatorios)
mediana= median(numeros_aleatorios)
moda= mode(numeros_aleatorios)
print(moda)
print(mediana)
print(media)
if (media > mediana and mediana > moda):
    print("Sesgo positivo o a la derecha")

elif(media < mediana and mediana < moda):
    print("Sesgo negativo o a la izquierda")

else:
    print("Sin sesgo")
