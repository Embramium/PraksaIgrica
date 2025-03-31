
import pygame
from konst import *

# Razred za vleko oz. premikanje figur - Eman
class Vleka():

    def __init__(self):
        self.miskaX = 0
        self.miskaY = 0

    def update_mouse(self, pozicija):
        self.miskaX, self.miskaY = pozicija