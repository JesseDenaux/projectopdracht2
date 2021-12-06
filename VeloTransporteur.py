from VeloStation import VeloStation
class VeloTransporteur:
    def __init__(self, naam):
        self.naam = naam
        self.aantalFietsen = 0
        self.fietsen = []

    def haalFietsenOp(self, aantalFietsen, veloStation):
        self.fietsen.append(veloStation.haalFietsOp(aantalFietsen))
        self.aantalFietsen += aantalFietsen

    def LeverFietsen(self, aantalFietsen, veloStation):
        veloStation.plaatsFiets(self.fietsen, aantalFietsen)
        self.aantalFietsen -= aantalFietsen

    def __str__(self):
        return f"Velo-transporteur {self.naam} heeft {self.aantalFietsen} op zijn wagen."

