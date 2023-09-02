##se crea la clase 

class Naves():
    peso = 2500 
    largo = 50
    ancho = 23
    color  = "negro"
    color1  = "blanco"
    motores = 2
    activada = False 
    compuerta_principal = True 
    sistema_defensa = True 
    autodestruccion = False 
    ###se peude agregar una funcion a una clase 
    def encender(self): 
        self.activada = True
    def apagar(self): 
        self.activada = False 
    def abrir_compuerta(self):
        self.compuerta_principal = True 
    def cerrar_compuerta(self): 
        self.compuerta_principal = False 
    def prender_defensa (self):
        self.sistema_defensa = True 
    def apagar_defensa (self):
        self.sistema_defensa = False 
    def activar_autodestruccion(self):
        mensaje  = "Protocolo de auto destruccion fuancionando"
        print(mensaje)
    def estado_motores(self):
        if (self.activada):
            return "motores funcionando al 100%"
        else :
            return "la compuerta esta cerrada "
    def estado_compuerta(self):
        if (self.compuerta_principal):
            return "la compuerta esta abierta"
        else: 
            return "Peligro la compuerta esta abierta"
    
    def estado_escudo(self):
        if (self.sistema_defensa):
            return "Escudo activado"
        else: 
            return "No esta activado el escudo"
        
#se crea el objeto 
nave1 = Naves()

##llamar al objeto 
nave1.encender()

#Comprueba estado de los motores.
print(nave1.estado_motores())

#Apaga nave.
nave1.apagar()

#Comprueba estado de los motores.

print(nave1.estado_motores())

#Abre la compuerta.
nave1.abrir_compuerta()

#Comprueba el estado de la compuerta.
print(nave1.estado_compuerta())

#Cierra compuerta.
nave1.cerrar_compuerta()

#Comprueba el estado de la compuerta.
print(nave1.estado_compuerta())

#Comprueba el estado de la defensas.
print(nave1.estado_escudo())

#Desactiva las defensas.
nave1.apagar_defensa()

#Comprueba el estado de la defensas.
print(nave1.estado_escudo())
nave1.activar_autodestruccion()

 
            