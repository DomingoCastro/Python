class Coche:
    marca = ""
    modelo = ""
    velocidad = 0
    estado = False
    
    def acelerar(self):
        if (self.estado == False):
            print("El coche no esta arrancado hay que arrancarlo antes")
        else:
            self.velocidad += 20
        print("Velocidad actual " + str(self.velocidad))

    
    def frenar(self):
        if (self.velocidad == 0):
            print("No puedo frenar mas")
        else:
            self.velocidad -= 10
        print ("Velocidad actual " + str(self.velocidad))
    
    def arrancar(self):
        self.estado = True
        print("Coche arrancado")

    def detener(self):
        if self.estado == False:
            print("Ya esta detenido")
        else:
            self.estado = False
            self.velocidad = 0
        print("Coche apagado")