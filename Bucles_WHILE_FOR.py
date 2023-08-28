
  #########################################
  #################While##################
  #######################################
#se crea un bucle para aumentar el valor de x hasta 10 

x = 1 
while x < 10: 
    x += 1
    print(x)
## bucle inf hasta que el usuario lo quiera 

frase = "lo que escribas lo repito"
frase += "\nIntroducie 'salir' para teminar\n"  #agrega a la cadena 
mensaje = ""
while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)
