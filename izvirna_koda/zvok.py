import pygame

class Zvok:

    def __init__(self, pot):

        self.pot = pot
        self.zvok = pygame.mixer.Sound(pot)

    def predvajaj(self):

        pygame.mixer.Sound.play(self.zvok)