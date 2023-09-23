class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

class Novo(Imovel):
    def __init__(self, endereco, preco, add_preco):
        super().__init__(endereco, preco)
        self.add_preco = add_preco

    def getValorAdd(self):
        return self.add_preco
    
    def imprimeAdicional(self):
        print(f"Valor adicional do imóvel novo: R$ {self.getValorAdd()}")

class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def getValorDesc(self):
        return self.desconto
    
    def imprimeDesconto(self):
        print(f"Desconto para este imóvel velho: R$ {self.getValorDesc()}")

imovelNovo = Novo("Rua São João Batista, 780", 100000.00, 25000.00)
imovelNovo.imprimeAdicional()

imovelVelho = Velho("Rua 7 de Setembro, 978", 150000.00, 35000.00)
imovelVelho.imprimeDesconto()