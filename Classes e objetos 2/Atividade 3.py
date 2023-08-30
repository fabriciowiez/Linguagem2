class Agenda:
    nome = None
    idade = None
    altura = None
    pessoas = [10]
    qtdPessoas = 0

    def armazenaPessoa(self, nome, idade, altura):
        if(self.qtdPessoas >= 9):
            print("Agenda Cheia!")
        else:
            self.pessoas[self.qtdPessoas] = { self.nome : nome, self.idade: idade, self.altura: altura }
            print(f"{self.nome} registrado com sucesso!")
            self.qtdPessoas += 1



