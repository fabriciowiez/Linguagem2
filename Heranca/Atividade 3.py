class Pessoa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def getNome(self):
        return self.nome
    def getEndereco(self):
        return self.endereco
    def setNome(self, nome):
        self.nome = nome
    def setEndereco(self, endereco):
        self.endereco = endereco
    