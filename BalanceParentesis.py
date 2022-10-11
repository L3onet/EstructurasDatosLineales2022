from Pila import *

class BalanceParentesis:
    __linea = ""

    def balancear(self, linea):
        self.__linea = linea
        pila = PilaDinamica()
        #quitar espacios
        elementos = list(self.__linea)
        for x in elementos:
            if (x == '(' or x == '[' or x == '{'):
                pila.push(x)
            if (x == ')' or x == ']' or x == '}'):
                apertura = ord(pila.pop())
                cierre = ord(x)
                if (cierre - apertura > 2 ):
                    return "Error de parentesis"
        print(pila.stackempty())
        if not (pila.stackempty()):
            return "Falta cerrar un parentesis"


if __name__==  '__main__':
    balance = BalanceParentesis()
    linea = input()
    print(balance.balancear(linea))