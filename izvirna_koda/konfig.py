from ast import NodeVisitor
import pygame
import os
import sqlite3

from zvok import Zvok
from izgled import Izgled

class Konfig:

    def __init__(self):

        self._ustvariBazo()
        
        # Izgled
        self.izgledi = []
        self._dodajIzgled()
        
        # Pridobi indeks iz baze
        povezava = sqlite3.connect("izgled_baza.db")
        kazalec = povezava.cursor()
        
        kazalec.execute("SELECT * FROM Izgled")
        podatki = kazalec.fetchall()
        if podatki:
            for podatek in podatki:
                self.indeks = podatek[0]
        else:
            self.indeks = 0 # Ce ni bilo baze ni shanjenega indeksa, 0 je default
        
        povezava.commit()
        povezava.close()
        
        self.izgled = self.izgledi[self.indeks]

        # Zvok
        self.poteza_zvok = Zvok(
            os.path.join("sredstva/zvok/premakni.wav")
        )
        self.pojej_zvok = Zvok(
            os.path.join("sredstva/zvok/pojej.wav")
        )
        
        #Font 
        self.font = pygame.font.SysFont("monospace", 18, bold = True)

    def spremeniIzgled(self):

        # Povecaj indeks in spremeni izgled
        self.indeks += 1
        self.indeks %= len(self.izgledi)
        self.izgled = self.izgledi[self.indeks]
        
        # Posodobi bazo
        povezava = sqlite3.connect("izgled_baza.db")
        kazalec = povezava.cursor()
        
        kazalec.execute("DELETE FROM Izgled where indeks")
        kazalec.execute(f"INSERT INTO Izgled VALUES({self.indeks})")
        
        povezava.commit()
        povezava.close()

    def _dodajIzgled(self):

        zelena = Izgled((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), "#C86464", "#C84646")
        rjava = Izgled((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), "#C86464", "#C84646")
        modra = Izgled((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), "#C86464", "#C84646")
        siva = Izgled((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), "#C86464", "#C84646")
        cyberpunk = Izgled((255, 0, 110), (20, 20, 40), (255, 100, 200), (60, 0, 100), "#00FFF7", "#FF00F7")
        matrix = Izgled((100, 100, 100), (200, 255, 100), (30, 30, 30), (0, 200, 50), "#39FF14", "#00CC66")
        sladoled = Izgled((255, 240, 245), (255, 192, 203), (255, 223, 186), (255, 182, 193), "#FF69B4", "#FF1493")
        ognjena = Izgled((255, 85, 0), (100, 0, 0), (255, 150, 50), (150, 50, 0), "#FF4500", "#8B0000")
        ledena = Izgled((210, 240, 255), (100, 170, 200), (180, 220, 240), (80, 130, 160), "#A0E9FF", "#408FA3")
        galaksija = Izgled((25, 0, 51), (75, 0, 130), (138, 43, 226), (0, 0, 80), "#DA70D6", "#8A2BE2")
        puščavska = Izgled((250, 240, 219), (189, 154, 122), (255, 223, 170), (204, 153, 102), "#C68642", "#8B5A2B")
        gozdna = Izgled((210, 230, 200), (85, 107, 47), (144, 238, 144), (34, 139, 34), "#228B22", "#006400")
        vulkanska = Izgled((255, 235, 205), (139, 0, 0), (255, 100, 50), (100, 0, 0), "#FF6347", "#8B0000")
        pivska = Izgled((255, 248, 220), (210, 180, 140), (255, 215, 0), (184, 134, 11), "#DAA520", "#8B4513")
        nocna = Izgled((30, 30, 60), (10, 10, 30), (70, 70, 100), (20, 20, 40), "#4169E1", "#191970")
        nevihtna = Izgled((220, 220, 220), (105, 105, 105), (176, 196, 222), (70, 70, 90), "#708090", "#2F4F4F")
        roznata = Izgled((255, 228, 225), (255, 105, 180), (255, 182, 193), (255, 20, 147), "#DB7093", "#C71585")

        self.izgledi = [zelena, rjava, modra, siva, cyberpunk, matrix, sladoled, ognjena, ledena, galaksija, puščavska, gozdna, vulkanska, pivska, nocna, nevihtna, roznata]
        
    def _ustvariBazo(self):
        
        # Ustvari in preveri povezavo
        povezava = sqlite3.connect("izgled_baza.db")
        print(povezava.total_changes)
        
        # Ustvari bazo ce ze ne obstaja
        kazalec = povezava.cursor()
        kazalec.execute("CREATE TABLE IF NOT EXISTS Izgled(indeks INT)")

        # Odaj in zapri povezavo
        povezava.commit()
        povezava.close()
        