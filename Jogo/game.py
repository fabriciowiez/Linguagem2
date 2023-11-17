import pyxel
import random
from circulos import Circulos
from mouse import Mouse
from musica import Musica
from draw import Desenhos
from vitoria import Vitoria
from derrota import Derrota

STEP = 2

class Game:
    def __init__(self):
        try:
            pyxel.init(160, 120)
            pyxel.load("desenhos.pyxres")
            self.mouse = Mouse()
            self.circulos = Circulos()   
            self.musica = Musica()
            self.draw = Desenhos()
            self.vitoria = Vitoria()
            self.derrota = Derrota()

            pyxel.run(self.update, self.desenhar)
        except Exception as e:
            print(f"Ocorreu um erro durante a inicialização do jogo: {e}")

       
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.frame_count > 30 * 3:
            if not (pyxel.sleep1 == pyxel.sleep2 == pyxel.sleep3 == pyxel.sleep4 == pyxel.sleep5 == True):
                pyxel.game_over = True

        if not pyxel.game_over:  
            self.verifica_clique_mouse()
            self.update_posicoes()

    def verifica_clique_mouse(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.circulos.in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x1, pyxel.y1):
                pyxel.sleep1 = True

            if self.circulos.in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x2, pyxel.y2):
                pyxel.sleep2 = True

            if self.circulos.in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x3, pyxel.y3):
                pyxel.sleep3 = True
            
            if self.circulos.in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x4, pyxel.y4):
                pyxel.sleep4 = True
            
            if self.circulos.in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x5, pyxel.y5):
                pyxel.sleep5 = True
            
    def update_posicoes(self):
        try:
            if not pyxel.sleep1:
                    pyxel.x1 = pyxel.x1 + random.uniform(-STEP, STEP)
                    pyxel.y1 = pyxel.y1 + random.uniform(-STEP, STEP)
                
            if not pyxel.sleep2:
                    pyxel.x2 = pyxel.x2 + random.uniform(-STEP, STEP)
                    pyxel.y2 = pyxel.y2 + random.uniform(-STEP, STEP)

            if not pyxel.sleep3:
                    pyxel.x3 = pyxel.x3 + random.uniform(-STEP, STEP)
                    pyxel.y3 = pyxel.y3 + random.uniform(-STEP, STEP)
                
            if not pyxel.sleep4:
                    pyxel.x4 = pyxel.x4 + random.uniform(-STEP, STEP)
                    pyxel.y4 = pyxel.y4 + random.uniform(-STEP, STEP)

            if not pyxel.sleep5:
                    pyxel.x5 = pyxel.x5 + random.uniform(-STEP, STEP)
                    pyxel.y5 = pyxel.y5 + random.uniform(-STEP, STEP)

        except Exception as e:
            print(f"Ocorreu um erro na atualização das posições: {e}")

    def desenhar(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, tm = 0, u = 0, v = 0, w = 160, h = 120, colkey = pyxel.COLOR_BLACK)
        self.draw.desenha_circulos()
        self.draw.desenha_textos()    

if __name__ == "__main__":
    Game()