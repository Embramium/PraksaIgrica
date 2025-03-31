
# Definicija polj (kvadratkov) - Eman
class Polje:

    def __init__(self, vrstica, stolpec, figura = None):
        
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.figura = figura

    def ima_figuro(self):

        return self.figura != None