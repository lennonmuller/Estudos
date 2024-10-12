# indice
class IndiceForaDosLimitesHandler:
    def __init__(self, lista):
        self.lista = lista

    def aceder_elemento(self, indice):
        try:
            elemento = self.lista[indice]
            print(f'Elemento no indice {indice}')
        except IndexError:
            print(f'Erro: O índice {indice} está fora dos limites da lista. Forneça um índice entre 0 e {len(self.lista) - 1}.')

objeto = IndiceForaDosLimitesHandler([1,2,3,4,5])

#Indice Válido
objeto.aceder_elemento(2)

#Indice Invalido
objeto.aceder_elemento(22)