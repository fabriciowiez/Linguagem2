class Barco:
    def __init__(self):
        self.velocidade = 0
    
    def liga(self):
        print("Barco ligado")

barco = Barco()

barco.liga()

print(f"Velocidade do barco: {barco.velocidade}")