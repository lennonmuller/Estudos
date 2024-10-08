''' buscador de palavras '''

# Criando classe
class Estrutura:
    def __init__(self):
        self.frase = ""
        self.palarva = ""

    #solicitando
    def solicitar(self):
        self.frase = input('Escreva uma frase: ')
        self.palavra = input('Qual palavra você deseja buscar na frase? ')

    # metodo para dividir
    def dividir(self):
        return self.frase.split()

    # metodo para contar
    def contar(self, lista_palavras):
        return lista_palavras.count(self.palavra)

    # metodo para imprimir resultados
    def resultados(self):
        lista_palavras = self.dividir()
        print('Lista de palavras: ', lista_palavras)
        contagem = self.contar(lista_palavras)
        print(f"Numero de vezes que a palavra '{self.palavra}' aparece na lista: {contagem}")

# Experimentar
extrator = Estrutura()
extrator.solicitar()
extrator.resultados()