'''
Operaciones básicas de las bicolas

+ CrearBicola Inicializa una bicola sin elementos.
+ BicolaVacia Devuelve true si la bicola no tiene elementos.
+ PonerFrente Añade un elemento por el extremo frente.
+ PonerFinal Añade un elemento por el extremo final.
+ QuitarFrente Devuelve el elemento Frente y lo retira de la bicola.
+ QuitarFinal Devuelve el elemento Final y lo retira de la bicola.
+ Frente Devuelve el elemento que se encuentra en el extremo frente.
+ Final Devuelve el elemento que se encuentra en el extremo final.
'''

class BiColaEstatica:
    __tamBiCola = int(0)
    __listaCola = []

    def __init__(self, tamBiCola):
        self.__tamBiCola = tamBiCola

    def BiColaVacia(self):
        return len(self.__listaCola) == 0

    def BiColaLlena(self):
        return self.__tamBiCola == len(self.__listaCola)

    def PonerFrente(self, elemento):
        if self.BiColaLlena():
            return False
        else:
            self.__listaCola.insert(0, elemento)
            return True

    def PonerFinal(self, elemento):
        if self.BiColaLlena():
            return False
        else:
            self.__listaCola.append(elemento)
            return True

    def QuitarFrente(self):
        if self.BiColaVacia():
            return False
        else:
            return self.__listaCola.pop(0)

    def QuitarFinal(self):
        if self.BiColaVacia():
            return False
        else:
            return self.__listaCola.pop()

    def Frente(self):
        if self.BiColaVacia():
            return False
        else:
            return self.__listaCola[0]

    def Final(self):
        if self.BiColaVacia():
            return False
        else:
            f = len(self.__listaCola) - 1
            return self.__listaCola[f]

    def MostrarTamBiCola(self):
        return len(self.__listaCola)

class BiColaDinamica:
    __listaCola = []

    def PonerFrente(self, elemento):
        self.__listaCola.insert(0, elemento)

    def PonerFinal(self, elemento):
        self.__listaCola.append(elemento)

    def QuitarFrente(self):
        if self.BiColaVacia():
            return False
        else:
            return self.__listaCola.pop(0)

    def QuitarFinal(self):
        if self.BiColaVacia():
            return False
        else:
            return self.__listaCola.pop()

    def BiColaVacia(self):
        return len(self.__listaCola) == 0

    def LimpiarBiCola(self):
        self.__listaCola.clear()

    def Frente(self):
        if self.BiColaVacia():
            return False
        else:
            return self.__listaCola[0]

    def Final(self):
        if self.BiColaVacia():
            return False
        else:
            f = len(self.__listaCola) - 1
            return self.__listaCola[f]

    def MostrarTamBiCola(self):
        return len(self.__listaCola)