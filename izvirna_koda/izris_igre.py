
import pygame
from konst import *
from plosca import Plosca
from vleka import Vleka
from polje import Polje

class Igra:

    # Inicializacija - Eman
    def __init__(self):
        
        self.naslednji_igralec = "bela"
        self.prekrito_polje = None
        self.plosca = Plosca()
        self.vleka = Vleka()

    # Blit metode - Eman
    def pokaziOzadje(self, surface):
        
        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                if (vrstica + stolpec) % 2 == 0:
                    barva = (210, 210, 210)
                else:
                    barva = (90, 90, 90)

                polje = (stolpec * POLJE_VELIKOST, vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)

                pygame.draw.rect(surface, barva, polje)

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
        if self.vleka.vleka:
            figura = self.vleka.figura

            # Pojdi skozi vse validne poteze in prikazi
            for poteza in figura.poteze:

                barva = "#C86464" if (poteza.koncno.vrstica + poteza.koncno.stolpec) % 2 == 0 else "#C84646"
                polje = (poteza.koncno.stolpec * POLJE_VELIKOST, poteza.koncno.vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)

                pygame.draw.rect(surface, barva, polje)
    
    def pokaziZadnjoPotezo(self, surface):
        if self.plosca.zadnja_poteza:
            zacetno = self.plosca.zadnja_poteza.zacetno
            koncno = self.plosca.zadnja_poteza.koncno
            
            # Prikazi potezo
            for poz in [zacetno, koncno]:
                barva = (244, 247, 116) if (poz.vrstica + poz.stolpec) % 2 == 0 else (172, 195, 51)
                polje = (poz.stolpec * POLJE_VELIKOST, poz.vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)
                pygame.draw.rect(surface, barva, polje)
    
    def pokaziPrekrito(self, surface):
        
        if self.prekrito_polje:
            barva = (50,50,50)
            polje = (self.prekrito_polje.stolpec * POLJE_VELIKOST, self.prekrito_polje.vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)
            pygame.draw.rect(surface, barva, polje, width=3)
            
    # Druge metode (metode ki niso za izris)
    
    def naslednjaPoteza(self):
        
        self.naslednji_igralec = "bela" if self.naslednji_igralec == "crna" else "crna"
    
    def nastavi_prekrito(self, vrstica, stolpec):
        
        self.prekrito_polje = self.plosca.polja[vrstica][stolpec]