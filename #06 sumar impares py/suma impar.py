def suma():
    lista = sum(i for i in range(100) if i % 2 != 0)
    return lista

print(suma())