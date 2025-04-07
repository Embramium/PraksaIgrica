
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

    # Povecaj sliko med drzanjem
    def posodobi_blit(self, surface):

        self.figura.nastavi_sliko(velikost = 120)

    def update_mouse(self, pozicija):

        self.miskaX, self.miskaY = pozicija

    def shrani_zacetno_poz(self, pozicija):

        self.zacetna_vrstica = pozicija[1] // POLJE_VELIKOST
        self.zacetni_stolpec = pozicija[0] // POLJE_VELIKOST

    def vleci_figuro(self, figura):

        self.figura = figura
        self.vleka = True

    def ne_vleci_figuro(self, figura):

        self.figura = None
        self.vleka = False