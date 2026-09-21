from model import Tripulante, MembroFrota

tripulante1 = Tripulante(
    "João",
    "Piloto",
    "Administrador",
)

tripulante2 = Tripulante(
    "Lucas",
    "Aeromoço",
    "Normal",
)

tripulante1.salvar()
tripulante2.salvar()

print(tripulante1)
print(tripulante2)

Tripulante.percorre_lista()



