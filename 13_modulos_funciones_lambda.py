import math
#importar libreria

def area(radio):
    res = round(math.pi *radio*radio,2)
    print(res)

area(2)

area = lambda radio : round(math.pi *radio*radio,2)
print (area(2))
