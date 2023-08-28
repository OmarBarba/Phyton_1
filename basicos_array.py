
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