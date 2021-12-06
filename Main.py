from Fiets import Fiets
from Gebruiker import Gebruiker
from VeloStation import VeloStation
from VeloTransporteur import VeloTransporteur

oVeloStation1 = VeloStation(20, "Noorderplaats")
oVeloStation2 = VeloStation(50, "Ellermanstraat")
oTransporteur = VeloTransporteur("Bert")
oTransporteur.haalFietsenOp(10, oVeloStation1)
print(oVeloStation1.vrijePlaatsen)
print(oVeloStation2.vrijePlaatsen)
print(oTransporteur.aantalFietsen)
print(Fiets.fietsId)



