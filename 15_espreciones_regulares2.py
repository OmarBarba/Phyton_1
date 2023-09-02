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

####buscar caracter por separado 
res2 = re.findall("[a]", texto)
print(res2)
