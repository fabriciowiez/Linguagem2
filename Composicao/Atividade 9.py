class Produto:
    def __init__(self, preco, tamanho):
        self.preco = preco
        self.tamanho = tamanho
    
    def vendido(self):
        print(f"Produto vendido por R${self.preco} de tamanho {self.tamanho}")

class Vendedor:
    def __init__(self, comissao):
        self.comissao = comissao
    
    def vender(self, comprador, produto):
        if comprador.verba >= produto.preco:
            print("Venda realizada")
            venda = Venda(comprador, self, produto)
            venda.concretizaVenda()
        else:
            print("O comprador não possui verba suficiente para comprar o produto")

    def __str__(self):
        return f"Vendedor (Comissão: R${self.comissao})"

class Comprador:
    def __init__(self, verba):
        self.verba = verba
    
    def compra(self, vendedor, produto):
        vendedor.vender(self, produto)

    def __str__(self):
        return f"Comprador (Verba: R${self.verba})"

class Venda:
    def __init__(self, comprador, vendedor, produto):
        self.comprador = comprador
        self.vendedor = vendedor
        self.produto = produto

    def concretizaVenda(self):
        self.vendedor.comissao += self.produto.preco * 0.1
        self.comprador.verba -= self.produto.preco
        self.produto.vendido()
    
    def cancelaVenda(self):
        self.comprador.verba += self.produto.preco
        self.vendedor.comissao -= self.produto.preco * 0.1

    def __str__(self):
        return f"Venda de {self.produto.tamanho} por R${self.produto.preco} realizada entre {self.comprador} e {self.vendedor}"

p = Produto(200, "Pequeno")
v = Vendedor(0)
c = Comprador(250)

c.compra(v, p)
venda1 = Venda(c, v, p)

print(venda1)
