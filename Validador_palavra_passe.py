# Validador de palavra passe
class ValidadorPalavraPasse:
    def __init__(self, valor):
        self.valor = valor

    def verificar_letras(self):
        return self.valor.isalpha()
    
    def verificar_digitos(self):
        return self.valor.isdigit()
    
    def verificar_letras_e_digitos(self):
        tem_letra = any(c.isalpha() for c in self.valor)
        tem_digito = any(c.isdigit() for c in self.valor)
        return tem_letra and tem_digito
    
    def verificar_comprimento(self):
        return len(self.valor) >= 8
    
    # Criando metodo Validar
    def validar(self):
        print('Apenas Letras: ', self.verificar_letras())
        print('Apenas Digitos: ', self.verificar_digitos())
        print('Letras e Digitos: ', self.verificar_letras_e_digitos())
        print('Comprimento >= 8: ', self.verificar_comprimento())

# Experimentar
senha = ValidadorPalavraPasse('Senha123')
senha.validar()