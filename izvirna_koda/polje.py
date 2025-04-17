
# Definicija polj (kvadratkov) - Eman
class Polje:

    def __init__(self, vrstica, stolpec, figura = None):
        
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.figura = figura

    def imaFiguro(self):

        return self.figura != None
    
    def jePrazno(self):

        return not self.imaFiguro()

    def imaPrijatelj(self, barva):

        return self.imaFiguro() and self.figura.barva == barva

    def imaNasprotnik(self, barva):

        return self.imaFiguro() and self.figura.barva != barva

    def praznoAliNasprotnik(self, barva):
        return self.jePrazno() or self.imaNasprotnik(barva)

    @staticmethod
    def vDosegu(*args):

        for arg in args:
            if arg < 0 or arg > 7:
                return False
        
        return True