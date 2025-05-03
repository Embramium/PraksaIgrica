
import pygame
from konst import *
from plosca import Plosca
from vleka import Vleka
from polje import Polje
from konfig import Konfig

class Igra:

    # Inicializacija - Eman
    def __init__(self):
        
        self.naslednji_igralec = "bela"
        self.prekrito_polje = None
        self.plosca = Plosca()
        self.vleka = Vleka()
        self.konfig = Konfig()

    # Blit metode - Eman
    def pokaziOzadje(self, surface):
        
        izgled = self.konfig.izgled
        
        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                
                barva = izgled.ozadje.svetlo if (vrstica + stolpec) % 2 == 0 else izgled.ozadje.temno 

                polje = (stolpec * POLJE_VELIKOST, vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)

                pygame.draw.rect(surface, barva, polje)
                
                # Koordinate vrstic
                if stolpec == 0:
                    barva = izgled.ozadje.temno if vrstica % 2 == 0 else izgled.ozadje.svetlo
                    
                    # Oznaka
                    oznaka = self.konfig.font.render(str(VRSTICE-vrstica), 1, barva)
                    oznaka_poz = (5, 5 + vrstica * POLJE_VELIKOST)
                    
                    # Blit metode
                    surface.blit(oznaka, oznaka_poz)
                    
                # Koordinate stolpcev
                if vrstica == 7:
                    barva = izgled.ozadje.temno if (vrstica + stolpec) % 2 == 0 else izgled.ozadje.svetlo
                    
                    # Oznaka
                    oznaka = self.konfig.font.render(Polje.pridobiAlfaoznako(stolpec), 1, barva)
                    oznaka_poz = (stolpec * POLJE_VELIKOST + POLJE_VELIKOST - 20, VISINA -20)
                    
                    # Blit metode
                    surface.blit(oznaka, oznaka_poz)

    def pokaziFigure(self, surface):

        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):

                # Preveri ce je na polju figura - Eman
                if self.plosca.polja[vrstica][stolpec].imaFiguro():
                    figura = self.plosca.polja[vrstica][stolpec].figura

                    # Dodeli sliko in izrise (razen vlecenih) - Eman
                    if figura is not self.vleka.figura:
                        figura.nastaviSliko(velikost = 80)
                        slika_var = pygame.image.load(figura.slika)
                        slika_center = stolpec * POLJE_VELIKOST + POLJE_VELIKOST // 2, vrstica * POLJE_VELIKOST + POLJE_VELIKOST // 2
                        figura.slika_rect =slika_var.get_rect(center = slika_center)
                        surface.blit(slika_var, figura.slika_rect)
                        
    def pokaziPoteze(self, surface):
        
        izgled = self.konfig.izgled
        
        if self.vleka.vleka:
            figura = self.vleka.figura

            # Pojdi skozi vse validne poteze in prikazi
            for poteza in figura.poteze:

                barva = izgled.poteze.svetlo if (poteza.koncno.vrstica + poteza.koncno.stolpec) % 2 == 0 else izgled.poteze.temno
                polje = (poteza.koncno.stolpec * POLJE_VELIKOST, poteza.koncno.vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)

                pygame.draw.rect(surface, barva, polje)
    
    def pokaziZadnjoPotezo(self, surface):
        
        izgled = self.konfig.izgled
        
        if self.plosca.zadnja_poteza:
            zacetno = self.plosca.zadnja_poteza.zacetno
            koncno = self.plosca.zadnja_poteza.koncno
            
            # Prikazi potezo
            for poz in [zacetno, koncno]:
                barva = izgled.sled.svetlo if (poz.vrstica + poz.stolpec) % 2 == 0 else izgled.sled.temno
                polje = (poz.stolpec * POLJE_VELIKOST, poz.vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)
                pygame.draw.rect(surface, barva, polje)
    
    def pokaziPrekrito(self, surface):
        
        if self.prekrito_polje:
            barva = (180, 180, 180)
            polje = (self.prekrito_polje.stolpec * POLJE_VELIKOST, self.prekrito_polje.vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)
            pygame.draw.rect(surface, barva, polje, width=3)
            
    # Druge metode (metode ki niso za izris)
    
    def naslednjaPoteza(self):
        
        self.naslednji_igralec = "bela" if self.naslednji_igralec == "crna" else "crna"
    
    def nastavi_prekrito(self, vrstica, stolpec):
        
        self.prekrito_polje = self.plosca.polja[vrstica][stolpec]
    
    def spremeniIzgled(self):
        
        self.konfig.spremeniIzgled()
        
    def predvajajZvok(self, pojeden = False):
        
        if pojeden:
            self.konfig.pojej_zvok.predvajaj()
        else:
            self.konfig.poteza_zvok.predvajaj()
            
    def resetiraj(self):
        
        self.__init__()