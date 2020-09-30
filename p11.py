lista = []
val = "E ai mano"

while not len(val) == 0:
    val = input("Entre com um valor: ")
    if len(val) > 0:
        lista.append(float(val))

print(lista)
print(max(lista))
print(min(lista))
print(sum(lista))
print(sum(lista)/len(lista))