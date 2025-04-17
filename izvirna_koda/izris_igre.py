
import pygame
from konst import *
from plosca import Plosca
from vleka import Vleka


class Igra:

    # Inicializacija - Eman
    def __init__(self):
        
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

            # Pojdi skozi vse validne poteze
            for poteza in figura.poteze:

                barva = "#C86464" if (poteza.koncno.vrstica + poteza.koncno.stolpec) % 2 == 0 else "#C84646"
                polje = (poteza.koncno.stolpec * POLJE_VELIKOST, poteza.koncno.vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)
                