# Leitor de fixeiro externo
with open(f'provas.txt', 'w', encoding='utf8') as ficheiro:
    ficheiro.write("Olá que tal estás\nIsto é uma prova\nHoje não chove\nAproxima-se o natal\nAté logo e boa\ncontinuação")

#abrir e ler o ficheiro
with open(f'provas.txt', 'r', encoding='utf8') as ficheiro:
    conteudo = ficheiro.read()
    nome_arquivo = ficheiro.name
    fechado = ficheiro.closed
    modo_abertura = ficheiro.mode

# verificando se o arquivo está fechado
fechado = ficheiro.closed

#imprimindo informações
print(f'Nome do ficheiro: {nome_arquivo}')
print(f'Ficheiro fechado: {fechado}')
print(f'Modo de abertura do ficheiro: {modo_abertura}')
print('Conteúdo: ')
print(conteudo)