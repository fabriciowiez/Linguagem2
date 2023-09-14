class Pedido:
    def __init__(self, valorTotal):
        self.itens = []
        self.valorTotal = valorTotal
    
    def addItem(self, item):
        self.itens.append(item)

    def obterTotal(self):
        self.valorTotal = sum(item.calcularTotalItem() for item in self.itens)
        return self.valorTotal
    
    def __str__(self):
        return f"Total do pedido: {self.obterTotal()}"
    
class ItemPedido:
    def __init__(self, produto, qntd):
        self.produto = produto
        self.qntd = qntd

    def calcularTotalItem(self):
        return self.produto.valor * self.qntd
    
    def __str__(self):
        return f"{self.produto} - {self.qntd}"

class Produto:
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

    def __str__(self):
        return f"{self.codigo} - {self.valor} - {self.descricao}"

prod1 = Produto(1, 25, "Boné")
prod2 = Produto(2, 3, "Lápis")

i1 = ItemPedido(prod1, 1)
i2 = ItemPedido(prod2, 3)

ped = Pedido(0)  
ped.addItem(i1)
ped.addItem(i2)

print("Itens do pedido: ")
for item in ped.itens:
    print(item)

print(ped)
