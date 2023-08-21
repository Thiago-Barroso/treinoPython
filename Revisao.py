# texto = "Estou estudando"
# indice = texto.find("stou")
# print(indice,type(indice))
# print(texto.lower())
# print(texto.upper())
# print(texto.replace("Estou","Comecei"))
# print(texto)

# semana = ("Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado")
# print(semana,type(semana))
# print(semana[::-1])
# semana.pop()
# semana.append("Dia")

concurso = {
    "nome":"Serpro",
    "Contratacao":"CLT",
    "Data":"27/08/2023"
}
concurso["Remuneracao"] = 9025.00
#print(concurso["nome"],type(concurso["nome"]))
print(concurso.keys())
print(concurso.items())
print(concurso.values())
