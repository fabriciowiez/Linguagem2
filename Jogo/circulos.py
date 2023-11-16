import pyxel
import random
from math import sqrt

#Inicializando os círculos
pyxel.game_over = False
pyxel.x1 = random.uniform(20, 140)
pyxel.y1 = random.uniform(20, 100)
pyxel.sleep1 = False
pyxel.x2 = random.uniform(20, 140)
pyxel.y2 = random.uniform(20, 100)
pyxel.sleep2 = False
pyxel.x3 = random.uniform(20, 140)
pyxel.y3 = random.uniform(20, 100)
pyxel.sleep3 = False
pyxel.x4 = random.uniform(20, 140)
pyxel.y4 = random.uniform(20, 100)
pyxel.sleep4 = False
pyxel.x5 = random.uniform(20, 140)
pyxel.y5 = random.uniform(20, 100)
pyxel.sleep5 = False

class Circulos:
    def __init__(self):
        self.RADIUS = 4
        self.COLOR_ACTIVE =  pyxel.COLOR_CYAN
        self.COLOR_SLEEP =  pyxel.COLOR_LIME
    
    #Função que verifica se o ponto (x, y) está dentro do cículo de raio cx, cy
    def in_circle(self, x, y, cx, cy):
        dist = sqrt( (x - cx) ** 2 + (y - cy) ** 2)
        return dist <= self.RADIUS