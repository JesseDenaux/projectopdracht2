class Fiets:
    fietsId = []
    def __init__(self, fietsNummer):
        if (self.checkFietsNummer(fietsNummer)):
            self.fietsNummer = fietsNummer

    def checkFietsNummer(self, fietsNummer):
        if fietsNummer in self.fietsId:
            return False
        else:
            self.fietsId.append(fietsNummer)
            return True

    def __str__(self):
        return f"Dit is fiets {self.fietsNummer}."


