
while True:
    
    number = input("Entre com um valor: ")

    if len(number) == 0:
        break
    
    number = float(number)

    if number > 2:
        print("Number is bigger than 2.")
    elif number < 2:  # Optional clause (you can have multiple elifs)
        print("Number is smaller than 2.")
    else:  # Optional clause (you can only have one else)
        print("Number is 2.")

    