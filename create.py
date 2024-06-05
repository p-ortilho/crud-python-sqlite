import sqlite3

# Criando conexão com o banco
conexao = sqlite3.connect('bancodedados.db')

# Mostrando o tipo da variavel conexão
print(type(conexao))

# Criando cursor para iteração com o banco de dados
cursor = conexao.cursor()

# Mostrando o tipo da variavel cursor
print(type(cursor))

# Criando tabela
comando = "CREATE TABLE pessoa(id INTEGER PRIMARY KEY, nome VARCHAR(255) NOT NULL, idade INT NOT NULL)"

# Executando o comando SQL
cursor.execute(comando)

# Finalizando o cursor
cursor.close()

# Finalizando a conexão
conexao.close()