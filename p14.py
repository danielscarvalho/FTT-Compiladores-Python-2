#import p13lib as p13

from p13lib import último
from p13lib import primeiro

lst = [20, 20, 30, 55]
l3 = [23.3, .5, "Lizard", [10, 8.8], (34, 55), 88]

for i in l3:
    print(type(i), i)

for i in lst:
    print(type(i), i)

print(primeiro(l3))
print(último(l3))
