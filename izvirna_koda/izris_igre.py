
import pygame
from konst import *
from plosca import Plosca


# Izrise igro - Eman
class Igra:

    def __init__(self):
        self.plosca = Plosca()

    # - Izris ozadja
    def pokazi_ozadje(self, surface):
        
        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                if (vrstica + stolpec) % 2 == 0:
                    barva = (210, 210, 210)
                else:
                    barva = (90, 90, 90)

                plosca = (stolpec * POLJE_VELIKOST, vrstica * POLJE_VELIKOST, POLJE_VELIKOST, POLJE_VELIKOST)

                pygame.draw.rect(surface, barva, plosca)

    def pokazi_figure(self, surface):

        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):

                # Preveri ce je na polju figura - Eman
                if self.plosca.polja[vrstica][stolpec].ima_figuro():
                    figura = self.plosca.polja[vrstica][stolpec].figura

                    # Dodeli sliko in izrise - Eman
                    slika = pygame.image.load(figura.slika)
                    slika_center = stolpec * POLJE_VELIKOST + POLJE_VELIKOST // 2, vrstica * POLJE_VELIKOST + POLJE_VELIKOST // 2
                    figura.slika_rect =slika.get_rect(center = slika_center)
                    surface.blit(slika, figura.slika_rect)