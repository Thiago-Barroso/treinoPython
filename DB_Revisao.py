import pyodbc
dados_conexao = """DRIVER={SQL Server};
                   server=DESKTOP-320NFTA;
                   database=crud;
                   username=Thiago_Barroso;
                   password=Bolapresa91"""
conexao = pyodbc.connect(dados_conexao)
#print("Passou")
#sql = "select @@version"
nome="Famicom Clone"
valor="300.00"
sql = f"insert into produto values('{nome}',{valor})"
cursor1 = conexao.cursor()
cursor1.execute(sql)
sql_consulta = "select * from produto"
resultado = cursor1.execute(sql_consulta).fetchall()
print(type(resultado))
print(resultado)
#resultado = cursor1.execute(sql).fetchall()
#print(type(resultado),resultado)
conexao.close()