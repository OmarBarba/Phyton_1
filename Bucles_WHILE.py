
  #########################################
  #################While##################
  #######################################
#se crea un bucle para aumentar el valor de x hasta 10 

x = 1 
while x < 10: 
    x += 1
    print(x)
## bucle inf hasta que el usuario lo quiera 
"""
frase = "lo que escribas lo repito"
frase += "\nIntroducie 'salir' para teminar\n"  #agrega a la cadena 
mensaje = ""
while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)
    """
#se comenta para seguir trabajando los bucles 

#salir cuando queramos 

v = 1 
while v <= 10:
    print (v)
    if v == 5:
        break 
    v += 1 
# avisar cuando termina un proceso 
else: 
    print("saliendo del bucle while")

#continue salta partes 
z = 0
while z < 10: 
    x += 1
    if z == 5 or z == 9:
      continue # se salta los valores del if 
    print(z)
    