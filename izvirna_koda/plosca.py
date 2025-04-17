
from konst import *
from polje import Polje
from figura import *
from poteza import Poteza


class Plosca:

    # Definicija plosce - Eman
    def __init__(self):
        
        self.polja = [[0, 0, 0, 0, 0, 0, 0, 0] for stolpec in range(STOLPCI)]

        self._ustvari()
        self._dodajFigure('bela')
        self._dodajFigure('crna')

    def zracunajPoteze(self, figura, vrstica, stolpec):
        
        # Zracunaj vse mozne poteze dolocene figure na dolocenem mestu - Eman
        
        def skakacPoteze():
            
            # 8 moznih potez
            mozne_poteze = [
                (vrstica -2, stolpec +1),
                (vrstica -1, stolpec +2),
                (vrstica +1, stolpec +2),
                (vrstica +2, stolpec +1),
                (vrstica +2, stolpec -1),
                (vrstica +1, stolpec -2),
                (vrstica -1, stolpec -2),
                (vrstica -2, stolpec -1)
            ]

            for mozna_poteza in mozne_poteze:
                mozna_poteza_vrstica, mozna_poteza_stolpec = mozna_poteza

                if Polje.vDosegu(mozna_poteza_vrstica, mozna_poteza_stolpec):
                    if self.polja[mozna_poteza_vrstica] [mozna_poteza_stolpec].praznoAliNasprotnik(figura.barva):

                        # Ustvari objekte iz polj v vprasanju
                        zacetno = Polje(vrstica, stolpec)
                        koncno = Polje(mozna_poteza_vrstica, mozna_poteza_stolpec)

                        # Ustvari nove objekte "poteze" in dodaj
                        poteza = Poteza(zacetno, koncno)
                        figura.dodaj_potezo(poteza)



        if isinstance(figura, Kmet):
            pass

        elif isinstance(figura, Skakac):
            skakacPoteze()

        elif isinstance(figura, Lovec):
            pass

        elif isinstance(figura, Trdnjava):
            pass

        elif isinstance(figura, Kraljica):
            pass

        elif isinstance(figura, Kralj):
            pass


    def _ustvari(self):

        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                self.polja[vrstica][stolpec] = Polje(vrstica, stolpec)

    def _dodajFigure(self, barva):
        
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