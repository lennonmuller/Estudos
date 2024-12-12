import sqlite3  # Importa o módulo sqlite3 para interagir com bancos de dados SQLite
from pathlib import Path  # Importa Path do módulo pathlib para manipulação de caminhos de arquivos

ROOT_PATH = Path(__file__).parent  # Define ROOT_PATH como o diretório pai do arquivo atual

conexao = sqlite3.connect(ROOT_PATH/'meu_banco.sqlite')  # Conecta ao banco de dados 'meu_banco.sqlite' localizado em ROOT_PATH
cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL e recuperar resultados
cursor.row_factory = sqlite3.Row  # Configura o cursor para acessar colunas pelo nome em vez de índices

try:
    cursor.execute("DELETE FROM clientes WHERE id = 7;")  # Tenta deletar o registro na tabela 'clientes' onde o 'id' é 7
    conexao.commit()  # Confirma a transação

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Jurescreudia", "Jurere@gmail.com"))  # Insere um novo registro na tabela 'clientes'
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (8, "Jega", "jegona@gmail.com"))  # Insere outro novo registro na tabela 'clientes'
    conexao.commit()  # Confirma as transações

except Exception as exc:  # Se ocorrer uma exceção durante a execução dos comandos SQL
    print(f"Ops! um erro ocorreu! {exc}")  # Imprime uma mensagem de erro
    conexao.rollback()  # Desfaz todas as transações pendentes
