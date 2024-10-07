# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua imagem,
#se ele vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que alistar imediatamente!')
elif idade < 18:
    print('Você ainda não tem 18 anos. Ainda falta {} anos')
elif idade > 18:
