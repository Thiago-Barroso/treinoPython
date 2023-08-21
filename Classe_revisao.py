class Pessoa():
    def __init__(self,nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def saudacao(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e sou do sexo {self.sexo}")
