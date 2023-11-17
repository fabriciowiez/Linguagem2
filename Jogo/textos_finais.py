import pyxel

class Textos_Finais:
    def __init__(self, texto, cor1, cor2):
        self.texto = texto
        self.cor1 = cor1
        self.cor2 = cor2
        self.x = 80 - 5 * pyxel.FONT_WIDTH
    
    def exibir_texto(self):
        pyxel.text(self.x, 60, self.texto, self.cor1)
        pyxel.text(self.x, 60, self.texto, self.cor2)