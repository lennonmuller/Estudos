with open('pessoas.txt', 'w', encoding='utf8') as ficheiro:
    ficheiro.write('1;Carlos;Pérez;05/01/1989\n2;Manuel;Heredia;26/12/1973\n3;Rosa;Campos;12/06/1961\n4;David;García;25/07/2006')
ficheiro.close()

with open('pessoas.txt', 'r', encoding='utf8') as ficheiro:
    linhas = ficheiro.readlines()

# Armazenar em dicionario
pessoas = []

#Percorrer linhas do ficheiro
for linha in linhas:
    linha = linha.strip()
    partes = linha.split(';')
    pessoa = {
        'id': partes[0],
        'nome': partes[1],
        'apelido': partes[2],
        'nascimento': partes[3]
    }
    pessoas.append(pessoa)

for pessoa in pessoas:
    print(f"(id={pessoa['id']}) {pessoa['nome']} {pessoa['apelido']} = {pessoa['nascimento']}")
ficheiro.close()

#Encontrar pessoa com base no ID
def encontrar_pessoa(pessoas, id_procurado):
    for pessoa in pessoas:
        if pessoa['id'] == id_procurado:
            return pessoa
    return None

id_procurado = '3'
pessoa_encontrada = encontrar_pessoa(pessoas, id_procurado)

if pessoa_encontrada:
    print(f"Pessoa Encontrada: (id={pessoa_encontrada['id']}) {pessoa_encontrada['nome']} {pessoa_encontrada['apelido']} = {pessoa_encontrada['nascimento']}")
else:
    print(f"Pessoa com id={id_procurado} não encontrada.")