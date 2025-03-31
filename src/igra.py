import pygame

from konst import *

# Inicializacija in program igre - Eman
class Igra:

    def __init__(self):
        pass

    # - Pokazi metode
    def pokazi_ozadje(self, surface):
        for vrstica in range(VRSTICE):
            for stolpec in range(STOLPCI):
                if (vrstica + stolpec) % 2 == 0:
                    color = (210, 210, 210)
                else:
                    color = (90, 90, 90)

                plosca = (stolpec * KVADRATEK_VELIKOST, vrstica * KVADRATEK_VELIKOST, KVADRATEK_VELIKOST, KVADRATEK_VELIKOST)

                pygame.draw.rect(surface, color, plosca)