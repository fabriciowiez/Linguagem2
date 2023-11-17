import pyxel
from textos_finais import Textos_Finais

class Vitoria(Textos_Finais):
    def __init__(self):
        super().__init__("VITORIA!:)", pyxel.COLOR_DARK_BLUE, pyxel.COLOR_CYAN)