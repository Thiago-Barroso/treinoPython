class Carro():
    def __init__(self, nome, marca,quantidade_lugares,ano):
        self.nome = nome
        self.marca = marca
        self.quantidade_lugares = quantidade_lugares
        self.ano = ano
    
    def __str__(self):
       return f"Carro {self.nome} da marca {self.marca}, leva {self.quantidade_lugares} pessoas e foi fabricado no ano {self.ano}"

    def barulho(self):
        print("Vruuuuummmm")
    
    
