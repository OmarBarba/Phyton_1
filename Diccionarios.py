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

mostrar = dict(teclado2) #llamamos al diccionario 
print(teclado2)