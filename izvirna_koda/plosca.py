
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
        
        def kmetPoteze():
            
            # Koliko korakov lahko kmet naredi
            if figura.premaknjen:
                mozni_koraki = 1
            else:
                mozni_koraki = 2

            # Vertikalni premiki
            zacetek = vrstica + figura.smer
            konec = vrstica + (figura.smer * (1+ mozni_koraki))

            for mozni_premik_vrstica in range(zacetek, konec, figura.smer):
                if Polje.vDosegu(mozni_premik_vrstica):
                    if self.polja[mozni_premik_vrstica][stolpec].jePrazno():

                        # Ustvari "polje" objekta za zacetno in koncno polje
                        zacetno = Polje(vrstica, stolpec)
                        koncno = Polje(mozni_premik_vrstica, stolpec)

                        # Ustvari nov "poteza" objekt in ga dodaj
                        poteza = Poteza(zacetno, koncno)
                        figura.dodajPotezo(poteza)
                    
                    # Ce polje ni prazno
                    else:
                        break
                # Ce polje ni v dosegu
                else:
                    break

            # Diagonalni premiki
            mozni_premik_vrstica = vrstica + figura.smer
            mozni_premik_stolpci = [stolpec - 1, stolpec + 1]

            for mozni_premik_stolpec in mozni_premik_stolpci:
                if Polje.vDosegu(mozni_premik_vrstica, mozni_premik_stolpec):
                    if self.polja[mozni_premik_vrstica][mozni_premik_stolpec].imaNasprotnik(figura.barva):

                        # Ustvari "polje" objekta za zacetno in koncno polje
                        zacetno = Polje(vrstica, stolpec)
                        koncno = Polje(mozni_premik_vrstica, mozni_premik_stolpec)

                        # Ustvari nov "poteza" objekt in ga dodaj
                        poteza = Poteza(zacetno, koncno)
                        figura.dodajPotezo(poteza)


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
                        figura.dodajPotezo(poteza)

        def ravnaCrtaPoteze(incrs):

            for incr in incrs:
                vrstica_incr,  stolpec_incr = incr
                mozna_poteza_vrstica = vrstica + vrstica_incr
                mozna_poteza_stolpec = stolpec + stolpec_incr

                # Dokler je mozen premik naprej
                while True:
                    if Polje.vDosegu(mozna_poteza_vrstica, mozna_poteza_stolpec):
                        
                        # Ustvari polja za mogoco potezo
                        zacetno = Polje(vrstica, stolpec)
                        koncno = Polje(mozna_poteza_vrstica, mozna_poteza_stolpec)
                        poteza = Poteza(zacetno, koncno)
                        
                        # Ce je polje prazno
                        if self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].jePrazno():
                            figura.dodajPotezo(poteza)


                        # Ce ima polje nasprotnika
                        if self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].imaNasprotnik(figura.barva):
                            figura.dodajPotezo(poteza)
                            break

                        # Ce ima polje prijatelja
                        if self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].imaPrijatelj(figura.barva):
                            break
                    
                    # Ni v dosegu
                    else:
                        break

                    # Inkrementiranje inkrementov :D    
                    mozna_poteza_vrstica = mozna_poteza_vrstica + vrstica_incr
                    mozna_poteza_stolpec = mozna_poteza_stolpec + stolpec_incr

        def KraljPoteze():
            sosedno = [
                (vrstica -1, stolpec +0), # gor
                (vrstica -1, stolpec +1), # desno gor
                (vrstica +0, stolpec +1), # desno
                (vrstica +1, stolpec +1), # desno dol
                (vrstica +1, stolpec +0), # dol
                (vrstica +1, stolpec -1), # levo dol
                (vrstica +0, stolpec -1), # levo
                (vrstica -1, stolpec -1) # levo gor

            ]
            
            # Normalne poteze
            for mogoca_poteza in sosedno:
                mozna_poteza_vrstica, mozna_poteza_stolpec = mogoca_poteza

                if Polje.vDosegu(mozna_poteza_vrstica, mozna_poteza_stolpec):
                    if self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].praznoAliNasprotnik(figura.barva):

                       # Ustvari in dodaj polja za mogoco potezo
                        zacetno = Polje(vrstica, stolpec)
                        koncno = Polje(mozna_poteza_vrstica, mozna_poteza_stolpec)
                        poteza = Poteza(zacetno, koncno)

                        figura.dodajPotezo(poteza)
            
            # Rosada

        if isinstance(figura, Kmet):
            kmetPoteze()

        elif isinstance(figura, Skakac):
            skakacPoteze()

        elif isinstance(figura, Lovec):
            ravnaCrtaPoteze([
                (-1, 1), # desno gor
                (-1, -1), # levo gor
                (1, 1), # desno dol
                (1, -1) # levo dol
            ])

        elif isinstance(figura, Trdnjava):
            ravnaCrtaPoteze([
                (-1, 0), # gor
                (0, 1), # desno
                (1, 0), # dol
                (0, -1) # levo
            ])

        elif isinstance(figura, Kraljica):
            ravnaCrtaPoteze([
                (-1, 1), # desno gor
                (-1, -1), # levo gor
                (1, 1), # desno dol
                (1, -1), # levo dol
                (-1, 0), # gor
                (0, 1), # desno
                (1, 0), # dol
                (0, -1) # levo
            ])

        elif isinstance(figura, Kralj):
            KraljPoteze()


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