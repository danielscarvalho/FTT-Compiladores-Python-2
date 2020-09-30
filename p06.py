val = 0

while True: #Loop infinito
    inv = float(input("Informe o valor: "))
    val += inv
    if inv < 0:
        break
    print("Valor: ", val)
    
print("Valor final:", val)