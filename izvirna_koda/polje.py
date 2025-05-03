
# Definicija polj (kvadratkov) - Eman
class Polje:

    ALFAOZNAKA = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    
    def __init__(self, vrstica, stolpec, figura = None):
        
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.figura = figura
        self.alfaoznaka = self.ALFAOZNAKA[stolpec]

    def __eq__(self, other):
        
        return self.vrstica == other.vrstica and self.stolpec == other.stolpec

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
    
    @staticmethod
    def pridobiAlfaoznako(stolpec):
        
        ALFAOZNAKA = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALFAOZNAKA[stolpec]