# -*- coding: utf-8 -*- 

cursos = ["c", "c+", "c#"]

for x in "Python":
    print(x)
    
for s in cursos: 
    if s == "c#":
        continue # lo salta 
    print(s)

############bucle for basio "pass"#######
 
for d in []:
    pass

############funcion range#############
for t in range(5, 25,2): #lo ejecuta 10 veces contando desde el 0 se ejcuta desde el 5 el tercer 
    #, es el incremento que quier
    print(t)


#######creacion de lista y bucle for#######
print("lista de números")
numeros = [2,4,6,8,10,12,14,16]

for f in range(len(numeros)):
    print( "# de op ->", f, "multiplicacion-> ", numeros[f], "resultados: ->", numeros[f]*numeros[f])


###############funcion  else################

for r in range(10): #lo ejecuta 10 veces contando desde el 0 se ejcuta desde el 5 el tercer 
    #, es el incremento que quier
    print(r)
else: 
     print("se termino el for")

#############bucle anidado################

num = ["1","2","3","4","5"]
num2 = "0"

for h in num:
    for g in num2:
        print (h + g)


