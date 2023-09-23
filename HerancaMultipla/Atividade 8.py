class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: {self.valor:.2f}")

class VIP(Ingresso):
    def __init__(self, valor, valor_Add):
        super().__init__(valor)
        self.valor_Add = valor_Add

    def valorIngressoVip(self):
        return self.valor + self.valor_Add

class Normal(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    
    def imprimeIngresso(self):
        print(f"Ingresso Normal")

class CamaroteInferior(VIP):
    def __init__(self, valor, valor_Add, localizacao):
        super().__init__(valor, valor_Add)
        self.localizacao = localizacao

    def getLocalizacao(self):
        return self.localizacao
    
    def imprimeLocalizacao(self):
        print(f"Localização do ingresso: {self.getLocalizacao()}")

class CamaroteSuperior(VIP):
    def __init__(self, valor, valor_Add, localizacao, valor_adicionalCamarote):
        super().__init__(valor, valor_Add)
        self.localizacao = localizacao
        self.valor_adicionalCamarote = valor_adicionalCamarote

    def getLocalizacao(self):
        return self.localizacao
    
    def imprimeLocalizacao(self):
        print(f"Localização do ingresso: {self.getLocalizacao()}")

    def valorIngressoCamarote(self):
        return self.valor + self.valor_Add + self.valor_adicionalCamarote
    
ingresso = Ingresso(40.00)
ingresso.imprimeValor()

ingressoNormal = Normal(40.00)
ingressoNormal.imprimeIngresso()

ingressoVIP = VIP(60.00, 7.00)
print(f"Valor do ingresso vip com valor adicional: {ingressoVIP.valorIngressoVip()}")

camaroteInf = CamaroteInferior(60.00, 7.00, "Setor Sul")
camaroteInf.imprimeLocalizacao()

camaroteSup = CamaroteSuperior(60.00, 7.00, "Setor Norte", 10.00)
camaroteSup.imprimeLocalizacao()
print(f"Valor total do ingresso do camarote superior: {camaroteSup.valorIngressoCamarote()}")