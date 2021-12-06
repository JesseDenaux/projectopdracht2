from VeloStation import VeloStation
class Gebruiker:
    def __init__(self, naam):
        self.naam = naam
        self.fiets = 0

    def neemFiets(self, veloStation):
        self.fiets = veloStation.haalFietsOp(1)

    def zetFietsTerug(self, veloStation):
        veloStation.plaatsFietsen(self.fiets)

    def __str__(self):
        if (self.fiets == 0):
            return f"{self.naam} heeft nog geen fiets."
        else:
            return f"{self.naam} heeft een fiets met nummer {self.fiets.fietsNummer}"

