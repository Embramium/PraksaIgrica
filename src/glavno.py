import pygame, sys

from konst import *
from igra import Igra

# Inicializacija in glavna zanka - Eman

class Glavno:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SIRINA, VISINA))
        pygame.display.set_caption("Šah")
        self.igra = Igra()
    

    def glavnazanka(self):
        
        while True:
            self.igra.pokazi_ozadje(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

glavno = Glavno()
glavno.glavnazanka()