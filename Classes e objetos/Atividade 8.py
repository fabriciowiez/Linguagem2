class Musica:
    def __init__(self, nome, genero, duracao, artista):
        self.nome = nome
        self.genero = genero
        self.duracao = duracao
        self.artista = artista

    def mostraMusica(self):
        print(f"{self.artista} - {self.nome}")
    def mostraTempo(self):
        print(f"Tempo de duração: {self.duracao}")
    def mostraGenero(self):
        print(f"Genero da musica: {self.genero}")