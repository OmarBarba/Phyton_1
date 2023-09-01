
####Creacion de una funcion####
print("\n######funciones########")
def saludar():
    print("Hola buenas tardes ")

saludar()

print("\n######mandar valores########")
def familia(nombre):
    print(nombre + " Simpson")
 
familia("Homero")
familia("Lisa")
familia("Bart")
familia("Marge")

#########################
#####Funciones args######
#########################
print("\n######funcion args########")

def alumnos(*args):
    print("EL ultimo alumno es: "+ args[2] +" y el primero es: "+ args[0]+ ".")


alumnos("omar", "alex", "Javier")
print("\n######clase mandando valores########")
def alumnos_profesor (profesor, sustituto,*args):
    print("profesor: " + profesor)
    print("sustituto: " + sustituto)
    for x in args: 
        print("Alumno: " + x )

lista_al = ["omar", "alex", "Javier"]
alumnos_profesor("Antonio", "juan", *lista_al)


############################
#####Funciones kwargs#######
############################
print("\n######funcion kwargs########")
#permite meter valores a una funcion sin tener que meter de uno por uno 
def colores (**kawrgs):
    print("este es el color "+ kawrgs["color1"] + ".")

colores(color1= "rojo",color2= "azul",color3="verde",color4= "rosa")

############################
##########Return###########
############################

print("\n######Return########")

def suma(x,y ):
    return x + y 
total = suma(10,10)
print(total)

def resta (x,y):
    return x-y 
total = resta (10,10)
print(total)

def division(x,y):
    return x/y 
total = division (10,10)
print(total)

#pass permite dejar una funcion en blanco 

def carros(color1="rojo"):
    print("mi color favorito para el carro es el: "+ color1)
    
carros("azul")#se le reasigan un valor 
carros()#se deja el preestableciodo 
