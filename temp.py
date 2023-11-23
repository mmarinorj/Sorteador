
import random

lista = [[2104, "Marcelo Marino"], [1107, "Ricardo Argueles"]]
print(lista)
temp = random.choice(lista)
lista.remove(temp)
print(lista)
temp = random.choice(lista)
lista.remove(temp)
print(lista)
