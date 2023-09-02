import re 
texto = "Vamos a probar algo mas, 1 2 3 tomar en cuenta que son pruebas"

#########principio de la cadena 
res = re.findall("\AVamos", texto)

print(res)
#########devuelve laor que no conteien digitos  
res = re.findall("\D", texto)
print(res)

#########metacaracteres
##############encuenta sin especificar con el metacaracteer .
 
res2 = re.findall("Va..s", texto)
print(res2)

##############buscar varios resultados  .
 
res3 = re.findall("Vamos|1|tomar", texto)
print(res3)

####buscar caracter por separado#########
res2 = re.findall("[a]", texto)
print(res2)

##########################################
#############EXEPCIONES###################
#########################################

################TRY######################
################Except###################

#probar errores 
variable  = "correcto "
try: 
    print(variable)
except:
    print("hay un error")

#esto no sirve para poder corroborar que lo que estamos haciendo tiene sentido
# de igual forma mostraremos el uso de execpciones de forma practica 

reinicio = True

while reinicio: 
    try:
        num3 = int(input("Introduce un número para sumar"))
        num4 = int(input("Introduce un número para sumar")) 
    except ValueError:
        print("ingresa un número sin caracter")
    else:
        print("El resultado es: ", num3 + num4)
    finally:
        pregunta = input("Quieres seguir sumando? introduce S/N \n ")
        if  pregunta == "N":
            reinicio = False
        elif pregunta == "S": 
            reinicio = True
        else:
            print("Ingresa 'N' para salir o 'S' para seguir")