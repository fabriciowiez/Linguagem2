class Pneu:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.marca} - {self.tamanho}"
    
class Motor:
    def __init__(self, tipoCombustivel, cavalos):
        self.tipoCombustivel = tipoCombustivel
        self.cavalos = cavalos

    def __str__(self):
        return f"{self.tipoCombustivel} - {self.cavalos}"

class Carro:
    def __init__(self, marca, ano, cor, pneus, motor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.pneus = pneus
        self.motor = motor

    def __str__(self):
        return f"Carro: {self.marca} - {self.ano} - {self.cor}\n" \
               f"Pneus: {self.pneus}\n" \
               f"Motor: {self.motor}"
    
pneus = Pneu("Michelin", 15)

motor = Motor("Flex", 260)

carro = Carro("Hyundai", 2023, "Azul", pneus, motor)

print(carro)