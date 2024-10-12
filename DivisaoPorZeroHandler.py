# DivisaoPorZeroHandler
class DivisaoPorZeroHandler:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def calcular(self):
        try:
            resultado = self.numerador/self.denominador
            print(f'Resultado da divisão: {resultado}')
        except ZeroDivisionError:
            print('Não é possivel dividir um numero por 0, escolha outro numero.')

#Executar
objeto1 = DivisaoPorZeroHandler(3,6)
objeto2 = DivisaoPorZeroHandler(6,0)

#resultado certo
objeto1.calcular()

#resultado except
objeto2.calcular()