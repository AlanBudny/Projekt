
class Enemystats:
    def __init__(self,name):
        name = None
    hp = 0
    atak = 0
class Mystats(Enemystats):
    def __init__(self, name):
        super().__init__(name)
        hp = 0
        self.atak1 = 0
        self.atak2 = 0
        self.atak3 = 0
        self.atak4 = 0
class Kule:
    pokebal = 0
    greatbal = 0
    ultrabal = 0
    masterbal = 0