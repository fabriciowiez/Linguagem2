class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostraCoordenadas(self):
        print(f"Coordenadas: {self.x} - {self.y}")

    def distancia(self, outro_ponto):
        dx = self.x - outro_ponto.x
        dy = self.y - outro_ponto.y
        return (dx ** 2 + dy ** 2) ** 0.5
    
print("Informe as coordenadas do primeiro ponto: ")

x1 = int(input())
y1 = int(input())

print("Informe as coordenadas do segundo ponto: ")

x2 = int(input())
y2 = int(input())

ponto1 = Ponto2D(x1, y1)
ponto2 = Ponto2D(x2, y2)

ponto1.mostraCoordenadas()
ponto2.mostraCoordenadas()

distancia = ponto1.distancia(ponto2)
print(f"A distancia entre os pontos é: {distancia}")
