import random
import math

#Python standard libs: https://docs.python.org/3/library/index.html

dado = dict()

print(dado, type(dado))

dado["nome"]="Maria Silva"
dado["idade"]=25
dado["valore"]=[random.random()*i for i in range(10)] #List compreension

for i in range(10):
    dado["v" + str(i)]=math.ceil(random.random()*100)

print(dado)
