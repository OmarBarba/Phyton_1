##if ->booleano
#>mayor que <menor que  >=menor o igual <= menor o igual 
#== igual y != diferete 

num = 10 
num2 =20 

if num != num2 :
   print("se ejecuto el if")

###if else 
##aqui pasa que si el valor de edad deve de ser mayor a 18 para que se cumpla el if si no es asi pasa al else 

edad = 20 
if edad >18 :
  print('puedes acceder')
else:
 print('no puedes acceder')
##aqui pasa que si el valor de edad deve de ser mayor o igual a 18 para que se cumpla el if si no es asi pasa al else 

if edad >=18 :
 print('puedes acceder')
else:
 print('no puedes acceder')

#valor por el usuario int(input())
edad1= int(input('Cual es tu edad?    ...   '))
if edad1<= 0:
   print ('Nadie puede tener esa edad')
elif edad1 >=1 edad1 <=17:
 print('Eres menor de edad')
elif edad <=100:
 print('Eres mayor de edad')
else:
  print('Edad no valida')