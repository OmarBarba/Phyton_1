
#creacion de la lista
lista= ["cpu", "ram", "disco"]
# de esta forma se presenta la representaicon de la lista 
print (lista)
#podemos obtener solo un valor de la lista se empieza a contar desde el 0
print (lista[2])

#obtner valor final de una lista y su logica 
paises = ['Antigua y Barbuda', 'Argentina', 'Bahamas', 'Barbados', 'Belice', 'Bolivia', 'Brasil', 'Canadá', 'Chile', 'Colombia',
           'Costa Rica', 'Cuba', 'Dominica', 'Ecuador', 'El Salvador', 'Estados Unidos', 'Granada', 'Guatemala', 'Guyana', 'Haití',
             'Honduras', 'Jamaica', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'República Dominicana', 'San Cristobal y Nieves',
               'San Vicente y las Granadinas', 'Santa Lucía', 'Surinam', 'Trinidad y Tobago', 'Uruguay', 'Venezuela']

print(paises[-1])

#eleminar valor de lista 
primos= [1,2,3,5,7,9,10]
#con posicion 
del primos[-1]
print(primos)
#escribiendo el valor 
primos.remove(1)
print(primos)

#eliminar pero guardar en una var lo que se borro 
colores=["rojo", "verde", 'azul','amarillo']
print(colores)
guardado=colores.pop(0)
print ('el color eliinado de la lista y guardado es: ' + guardado)

#añadir elemenotos metodo append se añade al final 
colores.append("morado")
print(colores)
#se puede añadir a una lista vacia 
color=[]
color.append("naranja")
print(color)

#añadir a lista pero en donde quiera 
#insert(pos,lo que agrego)
#si se agrega en este apartado con el -1 se agrega en el penultimo asi sucesivamente de forma inversa
colores.insert(-1,"rosa")
print(colores)

#ordenar alfabeticcamente 
#funcion sort
colores.sort()
print(colores)
#de forma inversa 
colores.sort(reverse=True)
print(colores)

#sort lo cambia de forma definitiva es decir que el orden que le establecimos ya no exiciste 
#el sorted solo lo arregla una ves 
print (sorted(colores)) 
print (colores)
##
##Contar valores de una lista 
print(len(paises))
print(paises[34])
#######################################
###############TUPLA###################
#######################################

lista= ['rojo','azul','verrde','amarillo']
tupla= ('rojo','azul','verrde','amarillo')
#se hace con parentesis
#imprimir normal llamar una especifica con corchete 
print(tupla)
print(tupla[2])

#######operaciones con tupla 
tupla1= (10,20,30,'este es el reusltado')
print(tupla1[3],tupla1[1]+tupla1[0])
#agregar dato no se puede con append 

###convertir de lista a tupla
tupla2=tuple(lista)
print (tupla2)
##convertir de lista a tupla 
lista1=list(tupla2)
print (lista)
print (tupla2)

