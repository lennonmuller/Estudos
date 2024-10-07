import Animal

class Gato(Animal.animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Cao(Animal.animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

class Coelho(Animal.animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

gato = Gato("Fofinho", "Branco")
cachorro = Cao("Snoop", "Preto")
coelho = Coelho("Hantaro", "Marrom")

gato.comer()
cachorro.comer()
coelho.comer()
