#Modelar CSV em python
import csv

#Criando arquivo CSV de exemplo
dados = [
    ["Nome", "Categoria", "Preço", "Em Estoque"],
    ["Carrinho", "Veículos", 20.50, "Sim"],
    ["Boneca", "Bonecas", 35.00, "Não"],
    ["Quebra-Cabeça", "Jogos", 15.00, "Sim"]
]

#Salvando o arquivo como brinquedos.csv
arquivo_original = "brinquedos.csv"
with open(arquivo_original, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(dados)

#Ler o Arquivo e mostrar os brinquedos disponiveis em estoque
brinquedos_disponiveis = []
with open(arquivo_original, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for linha in reader:
        if linha["Em Estoque"] == "Sim":
            brinquedos_disponiveis.append(linha)

print("Brinquedos Disponiveis em estoque: ")
for brinquedo in brinquedos_disponiveis:
    print(f"- {brinquedo['Nome']} ({brinquedo['Categoria']}) - R$ {brinquedo['Preço']}")

# Filtrar brinquedos abaixo de 30R$
brinquedos_baratos = [dados[0]] #cabeçalho
for brinquedo in brinquedos_disponiveis:
    if float(brinquedo["Preço"]) < 30.00:
        brinquedos_baratos.append([brinquedo["Nome"], brinquedo["Categoria"], brinquedo["Preço"], brinquedo["Em Estoque"]])

# Criar um arquivo CSV com os brinquedos filtrados
arquivo_filtrado = "brinquedos_baratos.csv"
with open(arquivo_filtrado, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(brinquedos_baratos)

print("\nNovo arquivo 'brinquedos_baratos.csv' criado com sucesso.")
