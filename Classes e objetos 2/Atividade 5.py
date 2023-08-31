class Carro:
    tanque = None
    distancia = None

    def abastecerCarro(self, gasolina):
        if(self.tanque == 50):
            print("Tanque cheio")
        elif(self.tanque + gasolina) < 50: 
            self.tanque = gasolina
        else: self.tanque = 50

    def moverCarro(self, distancia):
        self.distancia = distancia
    
    def getTanque(self):
        return self.tanque
    
    def getDistancia(self):
        return self.distancia
    
c1 = Carro()
c2 = Carro()

c1.tanque = int(input("Abastecimento do carro 1: "))
c1.abastecerCarro(c1.tanque)
c1.distancia = int(input("Distancia do carro 1: "))
c1.moverCarro(c1.distancia)

c2.tanque = int(input("Abastecimento do carro 2: "))
c2.abastecerCarro(c2.tanque)
c2.distancia = int(input("Distancia do carro 2: "))
c2.moverCarro(c2.distancia)


print(f"Carro 1: Distancia percorrida: {c1.getDistancia()} - Gasolina restante: {c1.getTanque() - (c1.getDistancia() / 15)}")
    
print(f"Carro 2: Distancia percorrida: {c2.getDistancia()} - Gasolina restante: {c2.getTanque() - (c2.getDistancia() / 15)}")
