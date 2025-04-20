

class Poteza:

    def __init__(self, zacetno, koncno):
        
        # Zacetno in koncno polje
        self.zacetno = zacetno
        self.koncno = koncno

    def __eq__(self, other):

        return self.zacetno == other.zacetno and self.koncno == other.koncno