import sqlite3

# Criando conexao com o banco de dados
conexao = sqlite3.connect('bancodedados.db')

# Criando cursor para itereção
cursor = conexao.cursor()

# Comando
comando = "SELECT * FROM pessoa"

# Executando o comando SQL
cursor.execute(comando)

# Recuperando os dados trasidos pelo comando
dados = cursor.fetchall()

# Iterando sobre os dados para imprimir na tela
for dado in dados:
    print(dado)

# Finalizando o cursor
cursor.close()

# Finalizando a conexão
conexao.close()