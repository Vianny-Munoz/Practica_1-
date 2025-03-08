from Persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, edad, direccion, area, cargo):
        super().__init__(nombre, edad, direccion)
        self.__area = area
        self.__cargo = cargo
    
    def getarea(self):
        return self.__area
        
    def setarea(self, area):
        self.__area=area

    def getcargo(self):
        return self.__cargo
        
    def setcargo(self, cargo):
        self.__cargo=cargo

    def __str__(self):
    
        print(f"Los datos del Administrativo son: \n", super().__str__(), "\n Ubicado en el area: ", self.getarea, "\n Con cargo: ", self.getcargo)

class GestorAdministrativos:
    def __init__(self):
        self.administrativos = {}

    def eliminar(self, nombre):
        if nombre not in self.administrativos:
            return False
        del self.administrativos[nombre]
        return True
 