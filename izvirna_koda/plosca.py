
import os
import copy
from konst import *
from polje import Polje
from figura import *
from poteza import Poteza
from zvok import Zvok


class Plosca:

    # Definicija plosce - Eman
    def __init__(self):
        
        self.polja = [[0, 0, 0, 0, 0, 0, 0, 0] for stolpec in range(STOLPCI)]

        self.zadnja_poteza = None
        self._ustvari()
        self._dodajFigure('bela')
        self._dodajFigure('crna')

    def premik(self, figura, poteza, racunanje_potez = False):

        zacetno = poteza.zacetno
        koncno = poteza.koncno
        
        en_passant_prazno = self.polja[koncno.vrstica][koncno.stolpec].jePrazno() 

        # Posodobitev konzolne plosce
        self.polja[zacetno.vrstica][zacetno.stolpec].figura = None
        self.polja[koncno.vrstica][koncno.stolpec].figura = figura  
        
        # Ce je kmet preveri sledece
        if isinstance(figura, Kmet):
            
             # En passant
            razlika = koncno.stolpec - zacetno.stolpec
            if razlika != 0 and en_passant_prazno:
            
                # Posodobitev konzolne plosce
                self.polja[zacetno.vrstica][zacetno.stolpec + razlika].figura = None
                self.polja[koncno.vrstica][koncno.stolpec].figura = figura
                
                if not racunanje_potez:
                    zvok = Zvok(os.path.join(
                        "sredstva/zvok/pojej.wav"
                    ))
                    zvok.predvajaj()
            
            else:   
                   
                # Promocija kmeta
                self.preveriPromocija(figura, koncno)
            
        # Rosada
        if isinstance(figura, Kralj):
            if self.rosada(zacetno, koncno) and not racunanje_potez:
                razlika = koncno.stolpec - zacetno.stolpec
                trdnjava = figura.leva_trdnjava if (razlika < 0) else figura.desna_trdnjava
                
                self.premik(trdnjava, trdnjava.poteze[-1])
                            
        
        figura.premaknjen = True

        # Pobrise seznam pravilnih potez in nastavi zadnjo potezo
        figura.pobrisiPoteze()
        self.zadnja_poteza = poteza
    

    def pravilniPremik(self, figura, poteza):

        return poteza in figura.poteze

    def preveriPromocija(self, figura, koncno):
        
        if koncno.vrstica == 0 or koncno.vrstica == 7:
            self.polja[koncno.vrstica][koncno.stolpec].figura = Kraljica(figura.barva)
    
    def rosada(self, zacetno, koncno):
        
        return abs(zacetno.stolpec - koncno.stolpec) == 2
    
    def nastaviTrueEnPassant(self, figura):
        
        if not isinstance(figura, Kmet):
            return
        
        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                if isinstance(self.polja[vrstica][stolpec].figura, Kmet):
                    self.polja[vrstica][stolpec].figura.en_passant = False
                    
        figura.en_passant = True
                                
    
    def vSahu(self, figura, poteza):
        
        kopija_figura = copy.deepcopy(figura)
        kopija_plosca = copy.deepcopy(self)
        
        # Naredi premik v kopiji trenutne plosce in preveri ali bi bil sah
        kopija_plosca.premik(kopija_figura, poteza, racunanje_potez = True)
        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                if kopija_plosca.polja[vrstica][stolpec].imaNasprotnik(figura.barva):
                    
                    # Preveri ce bi premik nasprotnikove figure povzrocil sah na njegovi strani, vrne T/F
                    f = kopija_plosca.polja[vrstica][stolpec].figura
                    kopija_plosca.zracunajPoteze(f, vrstica, stolpec, bool = False)
                    for p in f.poteze:
                        if isinstance(p.koncno.figura, Kralj):
                            return True
        return False
    
    def zracunajPoteze(self, figura, vrstica, stolpec, bool = True):
        
        
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

                        # Ustvari nov "poteza" objekt
                        poteza = Poteza(zacetno, koncno)
                        
                        # Preveri za sah in dodaj potezo
                        if bool:
                            if not self.vSahu(figura, poteza):
                                figura.dodajPotezo(poteza)
                        else:
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
                        koncna_figura = self.polja[mozni_premik_vrstica][mozni_premik_stolpec].figura
                        koncno = Polje(mozni_premik_vrstica, mozni_premik_stolpec, koncna_figura)

                        # Ustvari nov "poteza" objekt in ga dodaj
                        poteza = Poteza(zacetno, koncno)
                        
                        # Preveri za sah in dodaj potezo
                        if bool:
                            if not self.vSahu(figura, poteza):
                                figura.dodajPotezo(poteza)
                        else:
                            figura.dodajPotezo(poteza)
            
            # En passant premiki
            v = 3 if figura.barva == "bela" else 4
            kv = 2 if figura.barva == "bela" else 5
            
            # Levi en passant
            if Polje.vDosegu(stolpec - 1) and vrstica == v:
                if self.polja[vrstica][stolpec - 1].imaNasprotnik(figura.barva):
                    f = self.polja[vrstica][stolpec - 1].figura
                    if isinstance(f, Kmet):
                        if f.en_passant:
                            
                            # Ustvari "polje" objekta za zacetno in koncno polje
                            zacetno = Polje(vrstica, stolpec)
                            koncno = Polje(kv, stolpec - 1, f)

                            # Ustvari nov "poteza" objekt in ga dodaj
                            poteza = Poteza(zacetno, koncno)
                            
                            # Preveri za sah in dodaj potezo
                            if bool:
                                if not self.vSahu(figura, poteza):
                                    figura.dodajPotezo(poteza)
                            else:
                                figura.dodajPotezo(poteza)
            
            # Desni en passant
            if Polje.vDosegu(stolpec + 1) and vrstica == v:
                if self.polja[vrstica][stolpec + 1].imaNasprotnik(figura.barva):
                    f = self.polja[vrstica][stolpec + 1].figura
                    if isinstance(f, Kmet):
                        if f.en_passant:
                            
                            # Ustvari "polje" objekta za zacetno in koncno polje
                            zacetno = Polje(vrstica, stolpec)
                            koncno = Polje(kv, stolpec + 1, f)

                            # Ustvari nov "poteza" objekt in ga dodaj
                            poteza = Poteza(zacetno, koncno)
                            
                            # Preveri za sah in dodaj potezo
                            if bool:
                                if not self.vSahu(figura, poteza):
                                    figura.dodajPotezo(poteza)
                            else:
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
                        koncna_figura = self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].figura
                        koncno = Polje(mozna_poteza_vrstica, mozna_poteza_stolpec, koncna_figura)

                        # Ustvari nove objekte "poteze" in dodaj
                        poteza = Poteza(zacetno, koncno)
                        
                        # Preveri za sah in dodaj potezo
                        if bool:
                            if not self.vSahu(figura, poteza):
                                figura.dodajPotezo(poteza)
                            else: break
                        else:
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
                        koncna_figura = self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].figura
                        koncno = Polje(mozna_poteza_vrstica, mozna_poteza_stolpec, koncna_figura)
                        poteza = Poteza(zacetno, koncno)
                        
                        # Ce je polje prazno
                        if self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].jePrazno():
                            
                            # Preveri za sah in dodaj potezo
                            if bool:
                                if not self.vSahu(figura, poteza):
                                    figura.dodajPotezo(poteza)
                            else:
                                figura.dodajPotezo(poteza)


                        # Ce ima polje nasprotnika
                        elif self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].imaNasprotnik(figura.barva):
                            
                            # Preveri za sah in dodaj potezo
                            if bool:
                                if not self.vSahu(figura, poteza):
                                    figura.dodajPotezo(poteza)
                            else:
                                figura.dodajPotezo(poteza)
                                
                            break

                        # Ce ima polje prijatelja
                        elif self.polja[mozna_poteza_vrstica][mozna_poteza_stolpec].imaPrijatelj(figura.barva):
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

                        # Preveri za sah in dodaj potezo
                        if bool:
                            if not self.vSahu(figura, poteza):
                                figura.dodajPotezo(poteza)
                        else:
                            figura.dodajPotezo(poteza)
            
            # Rosada
            if not figura.premaknjen:
                
                # Dolga 
                leva_trdnjava = self.polja[vrstica][0].figura
                if isinstance(leva_trdnjava, Trdnjava):
                    if not leva_trdnjava.premaknjen:
                        
                        for stlp in range(1, 4):
                            if self.polja[vrstica][stlp].imaFiguro(): # rosada ni mogoca
                                break
                            
                            if stlp == 3:
                                
                                # Poda levo trdnjavo kot kraljev atribut
                                figura.leva_trdnjava = leva_trdnjava
                                
                                # Premik trdnjave
                                zacetno = Polje(vrstica, 0)
                                koncno = Polje(vrstica, 3)
                                potezaT = Poteza(zacetno, koncno)
                                
                                # Premik kralja
                                zacetno = Polje(vrstica, stolpec)
                                koncno = Polje(vrstica, 2)
                                potezaK = Poteza(zacetno, koncno)
                                
                                # Preveri za sah in dodaj potezo
                                if bool:
                                    if not self.vSahu(figura, potezaK) and not self.vSahu(leva_trdnjava, potezaT):
                                        leva_trdnjava.dodajPotezo(potezaT)
                                        figura.dodajPotezo(potezaK)
                                else:
                                    leva_trdnjava.dodajPotezo(potezaT)
                                    figura.dodajPotezo(potezaK)
                                
                # Kratka
                desna_trdnjava = self.polja[vrstica][7].figura
                if isinstance(desna_trdnjava, Trdnjava):
                    if not desna_trdnjava.premaknjen:
                        
                        for stlp in range(5, 7):
                            if self.polja[vrstica][stlp].imaFiguro(): # rosada ni mogoca
                                break
                            
                            if stlp == 6:
                                
                                # Poda desno trdnjavo kot kraljev atribut
                                figura.desna_trdnjava = desna_trdnjava
                                
                                # Premik trdnjave
                                zacetno = Polje(vrstica, 7)
                                koncno = Polje(vrstica, 5)
                                potezaT = Poteza(zacetno, koncno)
                                
                                # Premik kralja
                                zacetno = Polje(vrstica, stolpec)
                                koncno = Polje(vrstica, 6)
                                potezaK = Poteza(zacetno, koncno)
                                
                                # Preveri za sah in dodaj potezo
                                if bool:
                                    if not self.vSahu(figura, potezaK) and not self.vSahu(desna_trdnjava, potezaT):
                                        desna_trdnjava.dodajPotezo(potezaT)
                                        figura.dodajPotezo(potezaK)
                                else:
                                    desna_trdnjava.dodajPotezo(potezaT)
                                    figura.dodajPotezo(potezaK)
                                

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