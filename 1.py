lista = [1, 2, 3, 4, 5, 4, 4, 8, 9]


for element in lista:
    if element == 4:
        del lista[element]


print(lista)
