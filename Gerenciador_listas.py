class GerenciadorLista:
    def __init__(self,lista=None):
        self.lista = lista if lista is not None else []

    def adicionar_elemento(self, elemento):
        try:
            if elemento in self.lista:
                raise ValueError()
            else:
                self.lista.append(elemento)
            print(self.lista)
        except ValueError:
            print(f'Erro: Impossível adicionar elementos duplicados => {elemento}')

#experimentar
lista_inicial = GerenciadorLista([1,2,3])
# Adicionando Elementos a lista
lista_inicial.adicionar_elemento(10)
lista_inicial.adicionar_elemento(-2)
lista_inicial.adicionar_elemento('Olá')

#Adicionar Elemento Duplicado para mensagem de erro:
lista_inicial.adicionar_elemento(2)