import Classe_revisao
class Aluno(Classe_revisao.Pessoa):
    def __init__(self, nome, idade, sexo, curso):
        super().__init__(nome,idade,sexo)
        self.curso = curso
    
    def info(self):
        print(f"O meu curso é {self.curso}")