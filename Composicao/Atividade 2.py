class Produto:
    def __init__(self, nome, preco, qntd):
        self.nome = nome
        self.preco = preco
        self.qntd = qntd

class Pedido:
    def __init__(self):
        self.itens = {}
        self.tipoPagamento = ""
        self.valorTotal = 0

    def cadastrarItem(self, produto, qntd):
        self.itens[len(self.itens)] = {'Nome': produto.nome, 'Valor': produto.preco, 'Quantidade': qntd}
        self.valorTotal += produto.preco * qntd

    def setTipoPagamento(self, tipo):
        self.pagamento = tipo

prod = Produto('Carne', 20, 1)
ped = Pedido()

while 1:
    print("Menu: ")
    print("1 - Carne - R$ 20,00")
    print("0 - Concluir pedido")

    opc = int(input("Digite sua opção: "))
    
    if opc == 1:
        qntd = int(input("Digite a quantidade de itens: ")) 
        ped.cadastrarItem(prod, qntd)

    elif opc == 0: break

ped.setTipoPagamento(str(input("Dinheiro, cheque ou cartão? ")))

print("Itens: ")

for item in ped.itens:
    print(f"Produto: {ped.itens[item]['Nome']} - Quantidade: {ped.itens[item]['Quantidade']}")

print(f"O pagamento será em {ped.pagamento}")
print(f"Total do pedido: {ped.valorTotal}")


