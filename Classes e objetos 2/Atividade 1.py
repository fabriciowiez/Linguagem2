class Circulo:
    def __init__(self, raio, x_centro, y_centro):
        self.raio = raio
        self.x_centro = x_centro
        self.y_centro = y_centro

    def __calcularArea(self):
        return 3.14 * self.raio ** 2
    
    def __calcularCircunferencia(self):
        return 2 * 3.14 * self.raio
    
    def definirRaio(self, raio):
        self.raio = raio
    
    def aumentarRaio(self, perc_aumento):
        aumento = self.raio * (perc_aumento / 100)
        self.raio += aumento
    
    def definirCentro(self, x_centro, y_centro):
        self.x_centro = x_centro
        self.y_centro = y_centro

    def imprimirRaio(self):
        print(f"Raio do círculo: {self.raio}")

    def imprimirCentro(self):
        print(f"Centro: {self.x_centro} - {self.y_centro}")
    
    def imprimirArea(self):
        area = self.__calcularArea()
        print(f"Área do círculo: {area}")

raio = float(input("Digite o raio do circulo: "))
x = float(input("Digite o x do centro: "))
y = float(input("Digite o y do centro: "))
c = Circulo(raio, x, y)

while 1:
    print("1 - Definir raio do circulo")
    print("2 - Aumentar tamanho do raio")
    print("3 - Definir centro do circulo")
    print("4 - Mostrar raio do circulo")
    print("5 - Mostrar centro do circulo")
    print("6 - Mostrar area do circulo")
    print("0 - Sair")

    opc = int(input("Digite uma opção: "))

    if opc == 1 : c.definirRaio(float(input("Digite um novo valor para o raio: ")))
    elif opc == 2 : c.aumentarRaio(float(input("Digite um novo valor em % para aumentar o raio: ")))
    elif opc == 3:
        x = float(input("Digite o valor para o x do centro: "))
        y = float(input("Digite o valor para o y do centro: "))
        c.definirCentro(x, y)
    elif opc == 4 : c.imprimirRaio()
    elif opc == 5 : c.imprimirCentro()
    elif opc == 6 : c.imprimirArea()
    elif opc == 0 : break