import Carro
class Caminhonete(Carro.Carro):
    def __init__(self, nome, marca,quantidade_lugares,ano,kgCarga):
        super().__init__(nome, marca,quantidade_lugares,ano)
        self.kgCarga = kgCarga

    def __str__(self):
       return f"Caminhonete {self.nome}, da marca {self.marca}, leva {self.quantidade_lugares} pessoas, foi fabricado no ano {self.ano} e leva {self.kgCarga}kg de carga"

    def barulho(self):
        print("Hummm" + "Toc"*4)