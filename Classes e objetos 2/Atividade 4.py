class Televisao:
    def __init__(self):
        self.canal = 0;
        self.volume = 0;

    def aumentarVolume(self):
        self.volume += 1;

    def diminuirVolume(self):
        if self.volume == 0 : print("O volume já está no 0")
        else : self.volume -= 1;

    def imprimeVolume(self):
        print(f"Volume: {self.volume}")

    def aumentarCanal(self):
        self.canal += 1;

    def diminuirCanal(self):
        self.canal -= 1;

    def escolherCanal(self, canal):
        if self.canal == canal : print(f"A televisão já está no canal {self.canal}")
        else : self.canal = canal
    
    def imprimirCanal(self):
        print(f"Canal: {self.canal}")

t = Televisao()

while 1:
    print("1 - Aumentar o Volume")
    print("2 - Diminuir o Volume")
    print("3 - Mostrar o Volume")
    print("4 - Aumentar o Canal") 
    print("5 - Diminuir o Canal")
    print("6 - Escolher o Canal")
    print("7 - Mostrar o Canal")
    print("0 - Sair")

    opc = int(input("Digite sua opção: "))

    if opc == 1 : t.aumentarVolume()
    elif opc == 2 : t.diminuirVolume()
    elif opc == 3 : t.imprimeVolume()
    elif opc == 4 : t.aumentarCanal()
    elif opc == 5 : t.diminuirCanal()
    elif opc == 6 :
        canal = int(input("Digite o canal que deseja: "))
        t.escolherCanal(canal)
    elif opc == 7 : t.imprimirCanal()
    else : break;