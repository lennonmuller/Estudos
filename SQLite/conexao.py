import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH/'meu_banco.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(f"INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany(f"INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_cliente(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")

clientes = listar_cliente(cursor)
for cliente in clientes:
    print(dict(cliente))


cliente = recuperar_cliente(cursor, 1) # localizar clientes
print(dict(cliente))

print(f'Seja bem vindo ao sistema {cliente["nome"]}')



# dados = [
#     ("Junior Negão", "Jrnegao@gmail.com"),
#     ("Sinha moça", "mocinha@gmail.com")
#     ("Suila", "suila@gmail.com")
# ]

# inserir_muitos(conexao, cursor, dados)


#inserir_registro(conexao, cursor, 'Bob', 'boobsbob@boob.com')
#atualizar_registro(conexao, cursor, 'Lennon Müler', 'lennon-muller@hotmail.com', 1)
#excluir_registro(conexao, cursor, 3)