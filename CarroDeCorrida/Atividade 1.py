class CarroCorrida:
    def __init__(self, numeroCarro,  piloto,  equipe,  velocidadeMaxima, velocidadeAtual, ligado):
        self.numeroCarro = numeroCarro
        self.piloto = piloto
        self.equipe = equipe
        self.velocidadeMaxima = velocidadeMaxima
        self.velocidadeAtual = velocidadeAtual
        self.ligado = ligado

    def setNumeroCarro(self, numero): self.numeroCarro = numero

    def setPiloto(self, piloto): self.piloto = piloto

    def setEquipe(self, equipe): self.equipe = equipe

    def setVelocidadeMaxima(self, vlc): self.velocidadeMaxima = vlc

    def setVelocidadeAtual(self, vlc): self.velocidadeAtual = vlc

    def setLigado(self, ligado): self.ligado = ligado

    def getNumeroCarro(self): return self.numeroCarro
    
    def getPiloto(self): return self.piloto
        
    def getEquipe(self): return self.equipe
    
    def getVelocidadeMaxima(self): return self.velocidadeMaxima
    
    def getVelocidadeAtual(self): return self.velocidadeAtual
    
    def getLigado(self): return self.ligado
    
    def acelerar(self, vlc): 
        if not self.ligado : print("O carro está desligado")
        elif ((self.velocidadeAtual + vlc) >= self.velocidadeMaxima):
            self.velocidadeAtual = self.velocidadeMaxima
            print("Você já está na velocidade máxima")
        else : self.velocidadeAtual + vlc

    def frear(self, reducao): 
        if not self.ligado : print("O carro está desligado")
        elif (self.velocidadeAtual <= 0) : print("O carro está parado")
        else: 
            reducao = 100 - reducao
            self.velocidadeAtual = self.velocidadeAtual * (reducao/100)

    def parar(self):
        self.velocidadeAtual = 0
        print("O carro está parado")

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        if (self.velocidadeAtual == 0): 
            self.ligado == False
            print("Carro desligado")
        else : print("O carro precisa estar parado para ser desligado")