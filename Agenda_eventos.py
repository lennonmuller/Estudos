# Agenda de eventos
from datetime import datetime

class Evento:
    def __init__(self, titulo, data_hora_inicio, data_hora_fim):
        self.titulo = titulo
        self.data_hora_inicio = data_hora_inicio
        self.data_hora_fim = data_hora_fim

class Agenda:
    def __init__(self):
        self.eventos = []

    def Adicionar_evento(self, evento):
        self.eventos.append(evento)

    def listar_eventos(self):
        for evento in self.eventos:
            print(f'\tTitulo: {evento.titulo}: Inicio: {evento.data_hora_inicio}, Fim: {evento.data_hora_fim}')
    
    def proximo_evento(self):
        if not self.eventos:
            print('Não há eventos!')
            return
        proximo = min(self.eventos, key=lambda e: e.data_hora_inicio)
        print(f'Próximo evento: {proximo.titulo}, Inicio {proximo.data_hora_inicio}, Fim: {proximo.data_hora_fim}.')

    def eventos_do_dia(self, data):
        eventos_do_dia = [evento for evento in self.eventos if evento.data_hora_inicio.date() == data.date()]
        if not eventos_do_dia:
            print('Não há eventos para esta data.')
            return
        for evento in eventos_do_dia:
            print(f'Titulo: {evento.titulo}, Inicio: {evento.data_hora_inicio}, Fim: {evento.data_hora_fim}.')

# Objeto classe agenda
agenda = Agenda()

# 5 objetos da classe eventos e adicionar a agenda
eventos = [
    Evento('Reunião', datetime(2024, 10, 20, 14, 0), datetime(2024, 10,20,15,0)),
    Evento('Ver a gata', datetime(2024, 11, 1, 9, 0), datetime(2024, 11, 1, 11, 0)),
    Evento('Consulta medica', datetime(2024, 11, 21, 9, 0), datetime(2024, 11, 21, 12, 0)),
    Evento('Aniversario do cachorro', datetime(2024, 10, 22, 18, 0), datetime(2024, 10, 22, 23, 0)),
    Evento('Treino Bodybuilder', datetime(2024, 10, 23, 9, 0), datetime(2024, 10, 23, 12, 0))
]

for evento in eventos:
    agenda.Adicionar_evento(evento)

#Listar Eventos
print('Todos os Eventos: ')
agenda.listar_eventos()

#mostrar o proximo evento
print('\nPróximo evento: ')
agenda.proximo_evento()

#Listar todos os eventos para uma data
data_especifica = datetime(2024, 11, 1)
print(f'\nEventos para a data: {data_especifica.date()}: ')
agenda.eventos_do_dia(data_especifica)