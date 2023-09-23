class Carro:
    def __init__(self):
        self.velocidade = 0
    
    def liga(self):
        print("Carro ligado")

carro = Carro()

carro.liga()

print(f"Velocidade do carro: {carro.velocidade}")