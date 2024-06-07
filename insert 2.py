import sqlite3

# Criando conexao com o banco de dados
conexao = sqlite3.connect('bancodedados.db')

# Criando cursor para itereção
cursor = conexao.cursor()

# Comando
comando = "INSERT INTO pessoa VALUES(?, ?, ?)"

# Dados
registros = [
    (2, 'Maria', 18),
    (3, 'Amanda', 22)
]

# Inserindos os dados do registros no banco
for registro in registros:
    cursor.execute(comando, registro)

# commit usando para confirmar a execução do comando e torna-lo permanete
conexao.commit()

# Finalizando o cursor
cursor.close()

# Finalizando a conexão
conexao.close()