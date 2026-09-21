class MembroFrota:
    proximo_id = 1

    def __init__(self, nome):
        self.id = MembroFrota.proximo_id
        self.nome = nome
        MembroFrota.proximo_id += 1

class Tripulante(MembroFrota):
    banco_tripulantes = []
    def __init__(self, nome, cargo, nivel_acesso):
        
        super().__init__(nome)
        self.cargo = cargo
        self.__nivel_acesso = nivel_acesso

    def get_nivel_acesso(self):
        return self.__nivel_acesso

    def salvar(self):
        Tripulante.banco_tripulantes.append(self)

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.cargo} - {self.get_nivel_acesso()}"

    def percorre_lista():
        for tripulante in Tripulante.banco_tripulantes:
            print(tripulante)
    @classmethod
    def remover(cls, id_tripulante):
        cls.banco_tripulantes = [t for t in cls.banco_tripulantes if t.id != id_tripulante]