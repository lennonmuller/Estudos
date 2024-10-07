class ExtratorTexto:
    def __init__(self, texto, palavra):
        self.texto = texto
        self.palavra = palavra

    def pesquisar_e_extrair(self):
        posicao = self.texto.find(self.palavra)
        if posicao != -1:
            resultado = self.texto[posicao:]
            print('Extração: ', resultado)
        else:
            print('Palavra não encontrada.')

#Experimentar
texto = 'Hoje a giripoca vai piar vai'
palavra = 'giripoca'
extrator = ExtratorTexto(texto, palavra)
extrator.pesquisar_e_extrair()