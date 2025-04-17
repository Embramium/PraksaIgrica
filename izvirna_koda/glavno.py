
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
        plosca = self.igra.plosca
        vleka = self.igra.vleka

        while True:

            igra.pokazi_ozadje(zaslon)
            igra.pokazi_figure(zaslon)

            # Dogodki - Žiga
            for event in pygame.event.get():

                # Naredi ob pritisku miske
                if event.type == pygame.MOUSEBUTTONDOWN:

                    vleka.update_mouse(event.pos)
                    kliknjena_vrstica = vleka.miskaY // POLJE_VELIKOST
                    kliknjen_stolpec = vleka.miskaX // POLJE_VELIKOST

                    # Ce ima polje ze figuro
                    if plosca.polja[kliknjena_vrstica][kliknjen_stolpec].ima_figuro():
                        figura = plosca.polja[kliknjena_vrstica][kliknjen_stolpec].figura
                        vleka.shrani_zacetno_poz(event.pos)
                        vleka.vleci_figuro(figura)

                # Naredi ob premiku miske
                elif event.type == pygame.MOUSEMOTION:
                    if vleka.vleka:
                        vleka.posodobi_blit(zaslon)
                
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