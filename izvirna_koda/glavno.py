
import pygame, sys
from konst import *
from izris_igre import Igra


class Glavno:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SIRINA, VISINA))
        pygame.display.set_caption("Šah")
        self.igra = Igra()
    
    # Glavna izvrsilna zanka - Eman
    def glavnazanka(self):
        
        igra = self.igra
        zaslon = self.screen

        while True:
            igra.pokazi_ozadje(zaslon)
            igra.pokazi_figure(zaslon)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

glavno = Glavno()
glavno.glavnazanka()