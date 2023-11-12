import pyxel
import random
from math import sqrt

pyxel.init(160, 120)
#Inicializando os círculos
RADIUS = 4
COLOR_ACTIVE =  pyxel.COLOR_CYAN
COLOR_SLEEP =  pyxel.COLOR_LIME
STEP = 2

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

#Função que verifica se o ponto (x, y) está dentro do cículo de raio cx, cy
def in_circle(x, y, cx, cy):
    dist = sqrt( (x - cx) ** 2 + (y - cy) ** 2)
    return dist <= RADIUS

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if pyxel.frame_count > 30 * 3:
        if not (pyxel.sleep1 == pyxel.sleep2 == pyxel.sleep3 == True):
            pyxel.game_over = True

    if not pyxel.game_over:  
         verifica_clique_mouse()
         update_posicoes()

def verifica_clique_mouse():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x1, pyxel.y1):
            pyxel.sleep1 = True

        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x2, pyxel.y2):
            pyxel.sleep2 = True

        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x3, pyxel.y3):
            pyxel.sleep3 = True
        
        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x4, pyxel.y4):
            pyxel.sleep4 = True
        
        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x5, pyxel.y5):
            pyxel.sleep5 = True
        
def update_posicoes():
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

def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    desenha_circulos()
    desenha_textos()

def desenha_circulos():
    if pyxel.sleep1:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x1, pyxel.y1, RADIUS, color)

    if pyxel.sleep2:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x2, pyxel.y2, RADIUS, color)

    if pyxel.sleep3:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x3, pyxel.y3, RADIUS, color)

    if pyxel.sleep4:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x4, pyxel.y4, RADIUS, color)

    if pyxel.sleep5:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x5, pyxel.y5, RADIUS, color)

def desenha_textos():
    if pyxel.game_over:
        x = 80 - 5 * pyxel.FONT_WIDTH
        pyxel.text(x, 60, "GAME OVER!", pyxel.COLOR_WHITE)

    if pyxel.sleep1 == pyxel.sleep2 == pyxel.sleep3 == True:
        x = 80 - 5 * pyxel.FONT_WIDTH
        pyxel.text(x, 60, "VITORIA!:)", pyxel.COLOR_DARK_BLUE)

pyxel.mouse(True)
pyxel.run(update, draw)