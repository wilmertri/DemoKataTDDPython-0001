__author__ = 'Wilmer Fabian Triana'

class Calculadora:
    def sumar(self, cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            return int(cadena[0]) + int(cadena[2])
        else:
            return int(cadena)