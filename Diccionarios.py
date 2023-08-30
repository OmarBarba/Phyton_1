# creacion de diccionario 
teclado = {
    "categoria" : "Teclados",
    "switch" : "mx red",
    "Calidad" : "8.5",
}
teclado2 = {
    "categoria" : "Teclados",
    "switch" : "mx blue",
    "Calidad" : "8.9",
}
#se peude acceder a los atributos de manera separada 

consulta = teclado["Calidad"], teclado["switch"], teclado2["Calidad"], teclado2["switch"]
print(consulta)

#mostrar todo el contenido 
print("\n#####mostrar contenido######")
mostrar = dict(teclado2) #llamamos al diccionario 
print(teclado2)

# de igual forma se puede hacer con un print 
print(teclado)

#obtenrlo por separado get 
consultar = teclado.get("switch"),
print(consultar)

#definir valor 
print("\n#####definir valor######")
teclado["Calidad"] = "9.1"
print(teclado.get("Calidad"))

#bucle for en diccionario 
print("\n#####bucle for######")
#mostrar la categoria sin atributos
for s in teclado2:
    print(s)

#mostrar los atributos
for r in teclado2.values():
    print(r)

for f in teclado:
    print(teclado[f])

#mostrando elementos y variebles 
for x, y in teclado.items():
    print(x,":", y)

#################################
#############metodos#############
#################################
#####obtener longitud####
print("\n#####obtener long######")
print(len(teclado2))

print("\n#####eliminar######")
#####eliminar por competo un elemento#####
teclado.pop("categoria")
print(teclado)

del teclado2["categoria"]
print(teclado2)
#del pude eliminar todo el diccionario####
"""
#se comenta para no perder todas las variables 
del teclado 
#de esta manera se borra todo

## otra manera pero deja rastro 
teclado2.clear()
print(teclado2)
##lo que se ve en la consola seria {}
"""
#####agregar al diccionario######
print("\n#####agregar al diccionario######")
teclado2["color"] = "blanco" 
print (teclado2)

#####crear copia######
print("\n#####crear copia######")
copiaTeclado = teclado.copy()
print(copiaTeclado)

#tambien se puede hacer con el dict 
copiaTeclado2 = dict(teclado2)
print(copiaTeclado2)

#autogenerar valores repetitivos ##
print("\n######autogenerar valores repetitivos########")
teclado3 = ("categoria", "switch", "Calidad")
vacia = "valor valor vacio"
teclado3 = dict.fromkeys(teclado3,vacia)

#mostrar elemento y atributos tipo sql 
print("\n######mostrar elemento y atributos########")
vistaTeclado = teclado3.keys()
print(vistaTeclado)

##añadir con update###
print("\n######añadir con update########")
teclado.update({ "color" : "negro"} )
print(teclado)


##########################################
################CICLOS####################

###################if##################### 
print("\n######if ########")
if "ID" in teclado: 
    print("el producto no tiene id")
else : 
    print("el teclado no tiene id")

###anidar diccionarios 
print("\n######anidar diccionarios ########")
mouses = {
"mouse1" : {
    "categoria" : "Teclados",
    "switch" : "mx red",
    "Calidad" : "8.5",
    },
"mouse2" : {
    "categoria" : "Teclados",
    "switch" : "mx blue",
    "Calidad" : "8.9",
    }
}
print(mouses)
## ver la cantidad de diccionarios dentro del diccionarios 
print("\n######ver la cantidad de dicccionarios########")
print(len(mouses))