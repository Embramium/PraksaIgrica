import pygame
import os

from zvok import Zvok
from izgled import Izgled

class Konfig:

    def __init__(self):

        # Izgled
        self.izgledi = []
        self._dodajIzgled()
        self.indeks = 0
        self.izgled = self.izgledi[self.indeks]

        # Zvok
        self.poteza_zvok = Zvok(
            os.path.join("sredstva/zvok/premakni.wav")
        )
        self.pojej_zvok = Zvok(
            os.path.join("sredstva/zvok/pojej.wav")
        )

    def spremeniIzgled(self):

        self.indeks += 1
        self.indeks %= len(self.izgledi)
        self.izgled = self.izgledi[self.indeks]

    def _dodajIzgled(self):

        zelena = Izgled((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), "#C86464", "C84646")
        rjava = Izgled((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), "#C86464", "C84646")
        modra = Izgled((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), "#C86464", "C84646")
        siva = Izgled((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), "#C86464", "C84646")

        self.izgledi = [zelena, rjava, modra, siva]