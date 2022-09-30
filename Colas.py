class ColaEstatica:
    __tamCola = int(0)
    __listaCola = []

    def __init__(self, tamCola):
        self.__tamCola = tamCola

    def Insertar(self, elemento):
        if self.ColaLlena():
            return False
        else:
            self.__listaCola.append(elemento)
            return True

    def Quitar(self):
        if self.ColaVacia():
            return False
        else:
            return self.__listaCola.pop(0)

    def ColaVacia(self):
        return len(self.__listaCola) == 0

    def ColaLlena(self):
        return self.__tamCola == len(self.__listaCola)

    def LimpiarCola(self):
        self.__listaCola.clear()

    def MostrarFrente(self):
        return self.__listaCola[0]

    def MostrarTamCola(self):
        return len(self.__listaCola)

class ColaDinamica:
    __listaCola = []

    def Insertar(self, elemento):
        self.__listaCola.append(elemento)
        return True

    def Quitar(self):
        if self.ColaVacia():
            return False
        else:
            return self.__listaCola.pop(0)

    def ColaVacia(self):
        return len(self.__listaCola) == 0

    def LimpiarCola(self):
        self.__listaCola.clear()

    def MostrarFrente(self):
        return self.__listaCola[0]

    def MostrarTamCola(self):
        return len(self.__listaCola)