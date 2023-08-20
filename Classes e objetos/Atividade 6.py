class Time:
    nome = None
    esporte = None
    grito_de_guerra = None
    cidade = None
    treinador = None
    pontuacao = None
    jogadores = []

    def verPontuacao(self, ptns):
        self.pontuacao = ptns
    def adicionarJogador(self, jogador):
        self.jogadores.append = jogador
    def listarJogadores(self): 
        for jogador in self.jogadores:
            print(f"{jogador}")