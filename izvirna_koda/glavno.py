
import pygame, sys
from konst import *
from izris_igre import Igra
from polje import Polje
from poteza import Poteza

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
            igra.pokaziZadnjoPotezo(zaslon)
            igra.pokaziPoteze(zaslon)
            igra.pokaziFigure(zaslon)
            
            igra.pokaziPrekrito(zaslon)

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
                        
                        # Preveri barvo in povleci
                        if figura.barva == igra.naslednji_igralec:
                            plosca.zracunajPoteze(figura, kliknjena_vrstica, kliknjen_stolpec)
                            vleka.shraniZacetnoPoz(event.pos)
                            vleka.vleciFiguro(figura)

                        # Metode prikazovanja
                        igra.pokaziOzadje(zaslon)
                        igra.pokaziZadnjoPotezo(zaslon)
                        igra.pokaziPoteze(zaslon)
                        igra.pokaziFigure(zaslon)


                # Naredi ob premiku miske
                elif event.type == pygame.MOUSEMOTION:
                    
                    vrstica_premikanja = event.pos[1] // POLJE_VELIKOST
                    stolpec_premikanja = event.pos[0] // POLJE_VELIKOST
                    igra.nastavi_prekrito(vrstica_premikanja, stolpec_premikanja)
                    
                    if vleka.vleka:
                        vleka.posodobiMisko(event.pos)

                        # Metode prikazovanja
                        igra.pokaziOzadje(zaslon)
                        igra.pokaziZadnjoPotezo(zaslon)
                        igra.pokaziPoteze(zaslon)
                        igra.pokaziFigure(zaslon)
                        igra.pokaziPrekrito(zaslon)

                        vleka.posodobiBlit(zaslon)
                
                # Naredi ob spustu miske
                elif event.type == pygame.MOUSEBUTTONUP:
                    if vleka.vleka:
                        vleka.posodobiMisko(event.pos)

                        vrstica_spustitve = vleka.miskaY // POLJE_VELIKOST
                        stolpec_spustitve = vleka.miskaX // POLJE_VELIKOST

                        # Ustvari mozno potezo
                        zacetno = Polje(vleka.zacetna_vrstica, vleka.zacetni_stolpec)
                        koncno = Polje(vrstica_spustitve, stolpec_spustitve)
                        premik = Poteza(zacetno, koncno)

                        # Preveri ali je poteza pravilna
                        if plosca.pravilniPremik(vleka.figura, premik):
                            plosca.premik(vleka.figura, premik)

                            # Metode prikazovanja
                            igra.pokaziOzadje(zaslon)
                            igra.pokaziZadnjoPotezo(zaslon)
                            igra.pokaziFigure(zaslon)
                            
                            # Naslednja poteza
                            igra.naslednjaPoteza()


                    vleka.nehajVlectFiguro()

                # Naredi ob izhodu
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

glavno = Glavno()
glavno.glavnaZanka()