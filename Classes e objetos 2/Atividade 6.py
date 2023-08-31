class Elevador:
    def __init__(self, andares, capacidade):
        self.totalAndares = andares;
        self.capacidade = capacidade;
        self.andarAtual = 0;
        self.capacidadeAtual = 0;

    def entra(self):
        if(self.capacidade == self.capacidadeAtual):
            print("O elevador esta cheio")
        else:
            self.capacidadeAtual += 1
    
    def sai(self):
        if(self.capacidadeAtual == 0):
            print("O elevador esta vazio")
        else:
            self.capacidadeAtual -= 1

    def sobe(self):
        if(self.andarAtual != self.totalAndares):
            self.andarAtual += 1
        else:
            print("Já está no último andar")
    
    def desce(self):
        if(self.andarAtual > 0):
            self.andarAtual -= 1
        else:
            print("Já está no térreo")

    def getAndarAtual(self):
        return self.andarAtual
    def getAndares(self):
        return self.totalAndares
    def getCapacidade(self):
        return self.capacidade
    def getCapacidadeAtual(self):
        return self.capacidadeAtual
    
andares = int(input("Informe o total de andares do prédio: "))
capacidade = int(input("Informe a capacidade máxima do elevador: "))

e = Elevador(andares, capacidade)

while 1:
    print("1 - Mostrar andar atual do elevador")
    print("2 - Mostrar número de andares do prédio")
    print("3 - Mostrar capacidade total do elevador")
    print("4 - Mostrar total atual de pessoas no elevador")
    print("5 - Entrar no elevador")
    print("6 - Sair do elevador")
    print("7 - Subir andar")
    print("8 - Descer andar")
    print("0 - Sair")

    opc = int(input("Digite sua opção: "))

    if opc == 1 : print(f"Andar atual: {e.getAndarAtual()}")
    elif opc == 2 : print(f"Total de andares: {e.getAndares()}")  
    elif opc == 3 : print(f"Capacidade do elevador: {e.getCapacidade()}")
    elif opc == 4 : print(f"Total de pessoas no elevador: {e.getCapacidadeAtual()}")
    elif opc == 5 : e.entra()
    elif opc == 6 : e.sai()
    elif opc == 7 : e.sobe()
    elif opc == 8 : e.desce()
    else : break




