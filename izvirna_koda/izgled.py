from barva import Barva


class Izgled:

    def __init__(self, svetlo_oz, temno_oz,
                       svetlo_sled, temno_sled,
                       svetlo_pot, temno_pot):

        self.ozadje = Barva(svetlo_oz, temno_oz)
        self.sled = Barva(svetlo_sled, temno_sled)
        self.poteze = Barva(svetlo_pot, temno_pot)