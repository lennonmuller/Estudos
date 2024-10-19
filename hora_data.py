from datetime import datetime, date, time, timedelta

# Data e hora atuais
dt = datetime.now()
print('Data e horas atuais: ',dt)

#Formatos diferentes de datas:
print('Formato dd/mm/aaaa: {}/{}/{}'.format(dt.day,dt.month,dt.year))
print('Formato aaaa/mm/dd HH:MM: {}/{}/{} {}:{}'.format(dt.year,dt.month,dt.day,dt.hour,dt.minute))

# Receber datas de inicio e termino do projeto
inicio = input('Digite a data e hora de inicio no modelo aaaa/mm/dd HH:MM: ')
final = input('Digite a data e hora do final no modelo aaaa/mm/dd HH:MM: ')

# Converter strings para objetos datetime
data_inicio = datetime.strptime(inicio, "%Y-%m-%d %H:%M")
data_final = datetime.strptime(final, "%Y-%m-%d %H:%M")

#Calcular duração
duracao = data_final - data_inicio
dias = duracao.days
horas, remainder = divmod(duracao.seconds, 3600)
minutos, segundos = divmod(remainder, 60)

# Exibir a duração
print(f'Duração do projeto: {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')