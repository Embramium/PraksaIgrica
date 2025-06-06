
import os

class Figura:

    # Definicija figur
    def __init__(self, ime, barva, vrednost, slika = None, slika_rect = None):

        self.ime = ime
        self.barva = barva
        self.poteze = []
        self.premaknjen = False

        znak_vrednosti = 1 if barva == 'bela' else -1
        self.vrednost = vrednost * znak_vrednosti

        self.slika = slika
        self.nastaviSliko()
        self.slika_rect = slika_rect

    # Nastavi primerno sliko iz sredstev
    def nastaviSliko(self, velikost = 80):
        
        self.slika = os.path.join(f'sredstva/slike/slike-{velikost}px/{self.barva}_{self.ime}.png')

    def dodajPotezo(self, poteza):

        self.poteze.append(poteza)

    def pobrisiPoteze(self):

        self.poteze = []

# Inicializacija vseh figur
class Kmet(Figura):

    def __init__(self, barva):

        if barva == "bela":
            self.smer = -1
        else:
            self.smer = 1
        
        self.en_passant = False
        
        super().__init__('kmet',barva, 1.0)

class Skakac(Figura):

    def __init__(self, barva):

        super().__init__('skakac', barva, 3.0)

class Lovec(Figura):

    def __init__(self, barva):

        super().__init__('lovec', barva, 3.0)

class Trdnjava(Figura):

    def __init__(self, barva):

        super().__init__('trdnjava', barva, 5.0)

class Kraljica(Figura):

    def __init__(self, barva):
        
        super().__init__('kraljica', barva, 9.0)

class Kralj(Figura):

    def __init__(self, barva):
        
        self.leva_trdnjava = None
        self.desna_trdnjava = None
        
        super().__init__('kralj', barva, 10000.0)