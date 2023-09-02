import math
#importar libreria

def area(radio):
    res = round(math.pi *radio*radio,2)
    print(res)

area(2)

area = lambda radio : round(math.pi *radio*radio,2)
print (area(2))

#agregar fechas
import datetime

fecha = datetime.datetime.now()
print(fecha)
fecha = datetime.datetime(2020,9,29,10,50,45)
print(fecha)
print("año: ", fecha.year)
