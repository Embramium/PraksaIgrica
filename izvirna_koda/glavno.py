
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
        vleka = self.igra.vleka

        while True:

            igra.pokazi_ozadje(zaslon)
            igra.pokazi_figure(zaslon)

            # Dogodki - Eman
            for event in pygame.event.get():

                # Naredi ob pritisku miske
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vleka.update_mouse(event.pos)
                    kliknjena_vrstics = vleka.miskaY // POLJE_VELIKOST

                # Naredi ob premiku miske
                elif event.type == pygame.MOUSEMOTION:
                    pass
                
                # Naredi ob spustu miske
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

                # Naredi ob izhodu
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

glavno = Glavno()
glavno.glavnazanka()