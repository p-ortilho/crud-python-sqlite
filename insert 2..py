import sqlite3

# Criando conexao com o banco de dados
conexao = sqlite3.connect('bancodedados.db')

# Criando cursor para itereção
cursor = conexao.cursor()

# Comando
comando = "INSERT INTO videos VALUES(?, ?, ?)"

# Dados
registros = [
    (2, 'Shell Reverse', 'Crianção de shell reverse'),
    (3, 'Modelagem de Software', 'Como fazer modelagem de Software')
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