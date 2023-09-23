class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)
        self.dinheiro = dinheiro
    
    def fazCompras(self):
        print(f"{self.nome} faz compras!")
    
class Pobre(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        
    def trabalhar(self):
        print(f"{self.nome} trabalha!")

class Miseravel(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def mendiga(self):
        print(f"{self.nome} mendiga!")

rica = Rica("Carlos", 32, 1000000000)
rica.fazCompras()

pobre = Pobre("Sérgio", 47)
pobre.trabalhar()

miseravel = Miseravel("Pablo", 40)
miseravel.mendiga()