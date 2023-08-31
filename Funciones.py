
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

#####datos arbitrarios###


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

    
