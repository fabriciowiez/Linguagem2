import pyxel

class Desenhos:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.RADIUS = 2

    def desenha_circulos(self):
        self.x, self.y = pyxel.x1 - self.RADIUS, pyxel.y1 - self.RADIUS
        if pyxel.sleep1:
            pyxel.blt(self.x, self.y, img = 2, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK) 
        else:
            pyxel.blt(self.x, self.y, img = 0, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK) 

        self.x, self.y = pyxel.x2 - self.RADIUS, pyxel.y2 - self.RADIUS
        if pyxel.sleep2:
            pyxel.blt(self.x, self.y, img = 2, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK)
        else:
            pyxel.blt(self.x, self.y, img = 0, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK) 

        self.x, self.y = pyxel.x3 - self.RADIUS, pyxel.y3 - self.RADIUS
        if pyxel.sleep3:
            pyxel.blt(self.x, self.y, img = 2, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK)
        else:
            pyxel.blt(self.x, self.y, img = 0, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK) 

        self.x, self.y = pyxel.x4 - self.RADIUS, pyxel.y4 - self.RADIUS
        if pyxel.sleep4:
            pyxel.blt(self.x, self.y, img = 2, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK)
        else:
            pyxel.blt(self.x, self.y, img = 0, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK) 

        self.x, self.y = pyxel.x5 - self.RADIUS, pyxel.y5 - self.RADIUS
        if pyxel.sleep5:
            pyxel.blt(self.x, self.y, img = 2, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK)
        else:
            pyxel.blt(self.x, self.y, img = 0, u = 0, v = 0, w = 8, h = 8, colkey = pyxel.COLOR_BLACK) 

    def desenha_textos(self):
        if pyxel.game_over:
            self.x = 80 - 5 * pyxel.FONT_WIDTH
            pyxel.text(self.x, 60, "GAME OVER!", pyxel.COLOR_WHITE)

        if pyxel.sleep1 == pyxel.sleep2 == pyxel.sleep3 == pyxel.sleep4 == pyxel.sleep5 == True:
            self.x = 80 - 5 * pyxel.FONT_WIDTH
            pyxel.text(self.x, 60, "VITORIA!:)", pyxel.COLOR_DARK_BLUE)