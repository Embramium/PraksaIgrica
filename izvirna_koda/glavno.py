
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
    def glavnaZanka(self):
        
        igra = self.igra
        zaslon = self.screen
        plosca = self.igra.plosca
        vleka = self.igra.vleka

        while True:

            # Osnovno zaporedje za prikaz igre (Metode prikazovanja)
            igra.pokaziOzadje(zaslon)
            igra.pokaziPoteze(zaslon)
            igra.pokaziFigure(zaslon)

            if vleka.vleka:
                vleka.posodobiBlit(zaslon)

            # Dogodki - Žiga
            for event in pygame.event.get():

                # Naredi ob pritisku miske
                if event.type == pygame.MOUSEBUTTONDOWN:

                    vleka.posodobiMisko(event.pos)
                    kliknjena_vrstica = vleka.miskaY // POLJE_VELIKOST
                    kliknjen_stolpec = vleka.miskaX // POLJE_VELIKOST

                    # Ce ima polje figuro
                    if plosca.polja[kliknjena_vrstica][kliknjen_stolpec].imaFiguro():
                        figura = plosca.polja[kliknjena_vrstica][kliknjen_stolpec].figura
                        plosca.zracunajPoteze(figura, kliknjena_vrstica, kliknjen_stolpec)
                        vleka.shraniZacetnoPoz(event.pos)
                        vleka.vleciFiguro(figura)

                        # Metode prikazovanja
                        igra.pokaziOzadje(zaslon)
                        igra.pokaziPoteze(zaslon)
                        igra.pokaziFigure(zaslon)


                # Naredi ob premiku miske
                elif event.type == pygame.MOUSEMOTION:
                    if vleka.vleka:
                        vleka.posodobiMisko(event.pos)

                        # Metode prikazovanja
                        igra.pokaziOzadje(zaslon)
                        igra.pokaziPoteze(zaslon)
                        igra.pokaziFigure(zaslon)

                        vleka.posodobiBlit(zaslon)
                
                # Naredi ob spustu miske
                elif event.type == pygame.MOUSEBUTTONUP:
                    vleka.nehajVlectFiguro()

                # Naredi ob izhodu
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

glavno = Glavno()
glavno.glavnaZanka()