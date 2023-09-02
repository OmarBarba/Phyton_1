###########################
##########INIT#############
###########################

class personal():
#error comun el init lleva doble guion bajo

    def __init__(self, nombre, pin): 
        self.nombre = nombre 
        self.pin = pin 

    def saludo (self):
        print("saludos "+ self.nombre + " iniciaste sesíon correctamente. ")

    def despedida(self):
        print(self.nombre + " cerraste la sesión. " )
##se agraga esta liena para seguir parcticando 
    def muestra(self):
        print("El nombre de usuario es: " + self.nombre + " su pin es: " + self.pin)


persona1=personal("toni","123")

persona2=personal("juan  ", "3432")

persona1.saludo()
persona2
persona2.saludo()

persona1.muestra()

#cambiar un registro 
persona1.pin = "1234"

#dejar una clase vacia 

class carros:
    pass 

#elminar un valor de una clase 

del persona1.pin 

persona1.muestra

#eliminar un objeto 

"""del persona1 
"""

#se comenta para poder seguir trabajando 
persona1.pin = "1234"

############################
#####clase hijo de otra#####
############################
class personal_admn(personal):
    #se hizo una herencia 
    #para agregar valores es necesarios de volver a establecer el init para 
    #tomar las caracteristicas nuevas junto con un self cómo se mostrara 
    def __init__(self, nombre, pin, pago): 
        personal.__init__(self,nombre , pin)
        self.pago = pago 
    
    def muestra_amnd(self): 
        print("el nombre del usaurio admn es: " + self.nombre, "su pin es " + self.pin, "el paga " + self.pago)
    
    

persona4=personal_admn("francisco", "5434", "32")
persona4.muestra_amnd()
