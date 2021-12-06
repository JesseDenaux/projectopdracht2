from Fiets import Fiets
class VeloStation:
    def __init__(self, aantalFietsen, plaats):
        self.plaats = plaats
        self.fietsen = []
        self.vrijePlaatsen = aantalFietsen
        self.vulVeloStation(aantalFietsen)
        print(self.__str__())

    def plaatsFiets(self, fiets, aantalFietsen = 1):
        if (self.vrijePlaatsen > 0):
            if (aantalFietsen == 1):
                self.fietsen.append(fiets)
                self.vrijePlaatsen -= 1
            else:
                for x in range(len(Fiets.fietsId) + 1, len(Fiets.fietsId) + aantalFietsen + 1):
                    self.fietsen.append(fiets[x])
                    self.vrijePlaatsen -= 1
        else:
            return f"Er zijn geen vrije plaatsen meer in dit velo-station. Ga naar een velo-station in de buurt."

    def vulVeloStation(self, aantalFietsen):
        for x in range(len(Fiets.fietsId) + 1, len(Fiets.fietsId) + aantalFietsen + 1):
            self.fietsen.append(Fiets(x))
            self.vrijePlaatsen -= 1

    def haalFietsOp(self, aantalFietsen):
        fietsen = []
        if not (aantalFietsen >= len(self.fietsen)):
            if (aantalFietsen == 1):
                fiets = self.fietsen[0]
                del self.fietsen[0]
                self.vrijePlaatsen += 1
                return fiets
            else:
                for fiets in range(aantalFietsen):
                    fietsen.append(self.fietsen[0])
                    del self.fietsen[0]
                    self.vrijePlaatsen += 1
                return fietsen
        else:
            print(f"Er zijn niet zoveel fietsen meer beschikbaar. Er zijn nog {self.vrijePlaatsen} beschikbaar.")

    def __str__(self):
        return f"Velo-station {self.plaats} heeft {len(self.fietsen)} fietsen ter beschikking en {self.vrijePlaatsen} " \
               f"vrije plaatsen."




