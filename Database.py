import pyodbc
dados_conexao = """Driver={SQL Server};
                   SERVER=DESKTOP-320NFTA;
                   DATABASE=crud;
                   username=Thiago_Barroso;
                   password=Bolapresa91"""
conexao = pyodbc.connect(dados_conexao)
print("Conectou")       
cursor1 = conexao.cursor()

#sql = "select @@version;"

#sql = """create table produto(
#    id int identity(1,1) primary key,
#    nome varchar(50),
#    preco decimal(12,2),
#    )"""

# sql = """insert into produto(
#             nome,
#             preco
#         )
#         values ('Arcade',400.00),('Gamestick',190.00)
#         """

# sql = """update produto
#          set preco = 220.00
#          where nome='TV Box'
#          """

sql = """delete from produto
         where preco=400.00"""

resultado = cursor1.execute(sql)
resultado.commit()
conexao.close()
# lista = resultado.fetchone()
# print(lista,type(lista))            