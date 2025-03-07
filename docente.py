from Persona import Persona

class Docente(Persona):
    def __init__(self, nombre, edad, direccion, contrato):
        super().__init__(nombre, edad, direccion)
        self.__contrato=contrato

    def getcontrato(self):
        return self.__contrato
        
    def setcontrato(self, contrato):
        self.__contrato=contrato

    def __str__(self):
        print ("Bienvenidos")
        print(f"Los datos del docente son: \n", super().__str__(), "\n Con tipo de contrato: ", self.getcontrato)


