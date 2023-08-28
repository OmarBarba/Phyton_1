#if ->booleano
#>mayor que <menor que  >=menor o igual <= menor o igual 
#== igual y != diferete 

num = 10 
num2 =20 

if num != num2 :
   print("se ejecuto el if")

###if else 
##aqui pasa que si el valor de edad deve de ser mayor a 18 para que se cumpla el if si no es asi pasa al else 

edad = 20 
if edad > 18 :
  print('puedes acceder')
else:
 print('no puedes acceder')
##aqui pasa que si el valor de edad deve de ser mayor o igual a 18 para que se cumpla el if si no es asi pasa al else 

if edad >= 18 :
 print('puedes acceder')
else:
 print('no puedes acceder')

#valor por el usuario int(input()) 
edad1 = int(input('Cual es tu edad?    ...   '))
if edad1 <= 0:
   print ('Nadie puede tener esa edad')
elif edad1 >= 1 and edad1 <= 17:
 print('Eres menor de edad')
elif edad1 <= 100:
 print('Eres mayor de edad')
else:
  print('Edad no valida')
  

  #############################################
  #################APLICACION##################
  #############################################
entrada = input("introduce el nombre de un carro hyundai: \n")
hyundai =  ['elantra','sonata','tucson','creta', 'i10','santa fe']
'sonata' in hyundai #internamente muestra un true 
print ('sonata' in hyundai)# de esta manera lo muestra 
if entrada in hyundai: #in coteja que este a la lista
  print("Hay existencia hyundai")
else : 
  print("No hay exisitencia actualmente" )


#####################################################
#################ESpacios y sangria################## 
#####################################################
  
  #sangria 
#en el caso de los if o while o cualquier termino deven de tener una sangria
#para su funcionamiento 

  x = 100
  y = 200
  if x < y: 
    print("x es menor que y")
#se peude escribir todo en una linea pero no es lo recomendado

print("x es menor que y") if x < y else print("else")



  ##################################################
  #################operador or and##################
  ##################################################
#and = a que se deben de cumplir varias condiciones simultaneas 
#or solo se tiene que cumplir una de las funciones
z= 200

if x < y and z > y:
 print("Se cumple la condicion1")

else:
   print("no se cumple1")

if x < y or z > y:
 print("Se cumple la condicion2")

else:
   print("no se cumple2")