
import pygame
from konst import *

# Razred za vleko oz. premikanje figur - Eman
class Vleka():

    def __init__(self):

        self.figura = None
        self.vleka = False
        self.miskaX = 0
        self.miskaY = 0
        self.zacetna_vrstica = 0
        self.zacetni_stolpec = 0

    # Blit metode
    def posodobiBlit(self, surface):

        self.figura.nastavi_sliko(velikost = 128)
        slika = self.figura.slika

        slika_var = pygame.image.load(slika)
        slika_center = (self.miskaX, self.miskaY)
        self.figura.slika_rect = slika_var.get_rect(center=slika_center)

        surface.blit(slika_var, self.figura.slika_rect)



    def posodobiMisko(self, pozicija):

        self.miskaX, self.miskaY = pozicija

    def shraniZacetnoPoz(self, pozicija):

        self.zacetna_vrstica = pozicija[1] // POLJE_VELIKOST
        self.zacetni_stolpec = pozicija[0] // POLJE_VELIKOST

    def vleciFiguro(self, figura):

        self.figura = figura
        self.vleka = True

    def nehajVlectFiguro(self,):

        self.figura = None
        self.vleka = False