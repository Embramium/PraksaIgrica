
from konst import *
from polje import Polje
from figura import *


class Plosca:

    # Definicija plosce - Eman
    def __init__(self):
        
        self.polja = [[0, 0, 0, 0, 0, 0, 0, 0] for stolpec in range(STOLPCI)]

        self._ustvari()
        self._dodaj_figure('bela')
        self._dodaj_figure('crna')

    def _ustvari(self):

        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                self.polja[vrstica][stolpec] = Polje(vrstica, stolpec)

    def _dodaj_figure(self, barva):
        
        if barva == 'bela':
            kmeti_vrstica, vrstica_ostalo = 6, 7
        else:
            kmeti_vrstica, vrstica_ostalo = 1, 0

        # - Ustvari vse kmete
        for stolpec in range(STOLPCI):
            self.polja[kmeti_vrstica][stolpec] = Polje(kmeti_vrstica, stolpec, Kmet(barva))

        # - Ustvari vse skakace
        self.polja[vrstica_ostalo][1] = Polje(vrstica_ostalo, 1, Skakac(barva))
        self.polja[vrstica_ostalo][6] = Polje(vrstica_ostalo, 6, Skakac(barva))

        # - Ustvari vse lovce
        self.polja[vrstica_ostalo][2] = Polje(vrstica_ostalo, 2, Lovec(barva))
        self.polja[vrstica_ostalo][5] = Polje(vrstica_ostalo, 5, Lovec(barva))

        # - Ustvari vse trdnjave
        self.polja[vrstica_ostalo][0] = Polje(vrstica_ostalo, 0, Trdnjava(barva))
        self.polja[vrstica_ostalo][7] = Polje(vrstica_ostalo, 7, Trdnjava(barva))

        # - Ustvari kraljico
        self.polja[vrstica_ostalo][3] = Polje(vrstica_ostalo, 3, Kraljica(barva))

        # - Ustvari kralja
        self.polja[vrstica_ostalo][4] = Polje(vrstica_ostalo, 4, Kralj(barva))


p = Plosca()
p._ustvari()