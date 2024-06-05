import sqlite3

# Criando conexao com o banco de dados
conexao = sqlite3.connect('bancodedados.db')

# Criando cursor para itereção
cursor = conexao.cursor()

# Comando
comando = "INSERT INTO videos VALUES(1, 'Banco de Dados', 'Simples iteração com banco de dados sqlite3')"

# Executando o comando
cursor.execute(comando)

# commit usando para confirmar a execução do comando e torna-lo permanete
conexao.commit()

# Finalizando o cursor
cursor.close()

# Finalizando a conexão
conexao.close()