import pyxel
from textos_finais import Textos_Finais

class Derrota(Textos_Finais):
    def __init__(self):
        super().__init__("GAME OVER!", pyxel.COLOR_WHITE, pyxel.COLOR_YELLOW)