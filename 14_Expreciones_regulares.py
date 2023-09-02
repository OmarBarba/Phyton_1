#regEx
#funciones findall() search() slipt() sub()
########################
######search###########
######################
print("##########search######")
import re 
texto = "Hola vamos a hacer pruebas"
#muestra lo primero que encuentra con todo y acentos
busqueda =  re.search("o", texto)

print(busqueda)
################################
#########findall#############
################################
print("##########findall######")
busqueda2 = re.findall("o", texto)
print(busqueda)

################################
#########split#############
################################
#exclue espacios por separado 
#limitamos a 4 el patron de busqueda 
print("##########Split######")
busqueda3 = re.split(" ", texto, 4)
print(busqueda3)

################################
#########sub#############
################################
#exclue espacios por separado 
#limitamos a 4 el patron de busqueda 
print("##########Split######")
#sustituye los valores en este caso cambiamos los espacios por - 
# se puede limitar como en el caso de split 
#  se cambian solo dos 
busqueda4 = re.sub(" ", "-" , texto,2)
print(busqueda4)

