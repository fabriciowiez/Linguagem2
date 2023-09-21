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

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, credimaximo, valorEmDivida):
        super().__init__(nome, endereco)
        self.credimaximo = credimaximo
        self.valorEmDivida = valorEmDivida

    def obterSaldo(self):
        return self.credimaximo - self.valorEmDivida
    
fornecedor = Fornecedor("Fabrício Medeiros Ciechowiez", "Rua 7 de Setembro, 123", 10000, 6500)

print(f"Nome do fornecedor: {fornecedor.getNome()}")
print(f"Endereço do fornecedor: {fornecedor.getEndereco()}")
print(f"Crédito máximo: {fornecedor.credimaximo}")
print(f"Valor em dívida: {fornecedor.valorEmDivida}")
print(f"Saldo: {fornecedor.obterSaldo()}")
