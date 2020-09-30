print(range(10)) #Lazy load...
print(list(range(10)))

outlist = [] # Lista, vetor

for item in range(10):
    outlist.append(item**2)
    print(item)

print(outlist)

