class Pessoa:
    def __init__(self, nome, idade, pai = None, mae = None):
        self.nome = nome
        self.idade = idade
        self.pai = pai
        self.mae = mae

    def addFilho(self, filho):
        if isinstance(filho, Pessoa): #isinstance verifica se o objeto 'filho' é do tipo classe 'Pessoa'
            if filho.pai is None:
                filho.pai = self
            if filho.mae is None:
                filho.mae = self

avoPaterno1 = Pessoa("Edmundo", 83)
avoPaterno2 = Pessoa("Isabel", 80)

avoMaterno1 = Pessoa("Hélio", 73)
avoMaterno2 = Pessoa("Lenir", 73)

pai = Pessoa("Valdir", 62, pai=avoPaterno1, mae=avoPaterno1)
mae = Pessoa("Simone", 50, pai=avoMaterno1, mae=avoMaterno2)

filho = Pessoa("Fabrício", 19, pai=pai, mae=mae)

irmao = Pessoa("Jonas", 38, pai=pai, mae=mae)

while 1:
    print("1 - Adicionar filho")
    print("2 - Mostrar árvore genealógica")
    print("0 - Sair")

    opc = int(input("Insira sua opção: "))
    if opc == 1:
        pai.addFilho(irmao)
    elif opc == 2:
        print(f"{pai.nome} é filho de {avoPaterno1.nome} e {avoPaterno2.nome}")
        print(f"{mae.nome} é filha de {avoMaterno1.nome} e {avoMaterno2.nome}")
        print(f"{filho.nome} é filho de {pai.nome} e {mae.nome}")
        print(f"{irmao.nome} é filho de {pai.nome} e {mae.nome}")
    else: break