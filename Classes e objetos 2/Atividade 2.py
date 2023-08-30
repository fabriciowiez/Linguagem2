class Pessoa:
    __nome = None
    __idade = None
    __altura = None

    def definirNome(self, nome):
        self.__nome = nome
    def definirIdade(self, idade):
        self.__idade = idade
    def definirAltura(self, altura):
        self.__altura = altura

    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getAltura(self):
        return self.__altura
    
p = Pessoa()

nome = str(input("Digite o nome: "))
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))

p.definirNome(nome)
p.definirIdade(idade)
p.definirAltura(altura)

print(f"Nome: {p.getNome()}")
print(f"Idade: {p.getIdade()}")
print(f"Altura: {p.getAltura()}")