class Carro:
    def __init__(self):
        self.velocidade = 0
    
    def liga(self):
        print("Carro ligado")

class Barco:
    def __init__(self):
        self.velocidade = 0
    
    def liga(self):
        print("Barco ligado")

class CarroAnfibio(Carro, Barco):
    def liga(self):
        super().liga()

class CarroAnfibio2(Barco, Carro):
    def liga(self):
        super().liga()

carAnfibio = CarroAnfibio()

carAnfibio.liga()

carAnfibio2 = CarroAnfibio2()

carAnfibio2.liga()