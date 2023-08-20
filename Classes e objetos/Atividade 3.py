class LampadaTresEstados:
    luz = None

    def brilhoLuz(self, luz):
        if luz == 0 : self.luz = 'Apagada'
        elif luz >= 1 and luz <= 99 : self.luz = 'Meia Luz'
        else : self.luz = 'Acesa'

luz = int(input("Digite um valor para a luz da lampada: "))
l = LampadaTresEstados()
l.brilhoLuz(luz)
print(f"Estado da lampada: {l.luz}")