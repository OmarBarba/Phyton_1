import math
#importar libreria

def area(radio):
    res = round(math.pi *radio*radio,2)
    print(res)

area(2)

area = lambda radio : round(math.pi *radio*radio,2)
print (area(2))

#agregar fechas
import datetime, locale
locale.setlocale(locale.LC_ALL, "es-Es")
fecha = datetime.datetime.now()
print(fecha)
fecha = datetime.datetime(2020,9,29,10,50,45)
print(fecha)
print("año: ", fecha.year)

fecha1 = datetime.datetime.now()
#dia del mes 
#dia de la smena entero 
print(fecha1.strftime("\n%d"))
#dia de la smena numero 
#dia de la smena entero 
print(fecha1.strftime("%w"))
#dia de la smena entero 
print(fecha1.strftime("%A"))
#dia de la smena corto 
print(fecha1.strftime("%a"))
#minutos
print(fecha1.strftime("%M"))
#año
print(fecha1.strftime("%Y"))
#numreo del mes
print(fecha1.strftime("%m"))
#mes corto 
#dia de la smena entero 
print(fecha1.strftime("%b"))
#mes 
print(fecha1.strftime("%B"))
#año cort
print(fecha1.strftime("%y"))
#hora 
print(fecha1.strftime("%H"))
#fecha local 
print(fecha1.strftime("%x"))
print(fecha1.strftime("%X"))
