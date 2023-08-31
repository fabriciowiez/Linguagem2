class Agenda:
    pessoas = {}
    qtdPessoas = 0

    def armazenaPessoa(self, nome, idade, altura):
        if(self.qtdPessoas >= 10):
            print("Agenda Cheia!")
        else:
            self.pessoas[self.qtdPessoas] = { 'Nome': nome, 'Idade': idade, 'Altura': altura }
            print(f"{nome} registrado com sucesso!")
            self.qtdPessoas += 1
    
    def buscaPessoa(self, nome):
        achou = 0
        for i in self.pessoas:
            if (self.pessoas[i]['Nome'] == nome):
                print(f"{nome} encontrado na posição {i}")
                achou = 1
        
        if(achou == 0):
            print(f"O nome {nome} não foi encontrado")

    def imprimirAgenda(self):
        for i in self.pessoas:
            nome  = self.pessoas[i]['Nome']
            idade = self.pessoas[i]['Idade']
            altura = self.pessoas[i]['Altura']

            print(f"{nome} - {idade} - {altura}\n")

    def imprimePessoa(self, posicao):
        print(f"Pessoa encontrada na posição" [posicao])
        print(f"{self.pessoas[posicao]['Nome']} - {self.pessoas[posicao]['Idade']} - {self.pessoas[posicao]['Altura']}")

a = Agenda()

while 1:
    print("1 - Armazenar pessoa")
    print("2 - Imprime posição da pessoa pelo ome")
    print("3 - Listar agenda")
    print("4 - Imprime pessoa por posição")
    print("0 - Sair")

    opc = int(input("Digite sua opção: "))

    if opc == 1:
        nome = str(input("Insira o nome: "))
        idade = int(input("Insira a idade: "))
        altura = float(input("Insira a altura: "))

        a.armazenaPessoa(nome, idade, altura)
    
    elif opc == 2:
        nome = str(input("Insira o nome para a busca: "))
        a.buscaPessoa(nome)

    elif opc == 3:
        a.imprimirAgenda()

    elif opc == 4:
        pos = int(input("Insira a posição: "))
        a.imprimePessoa(pos)
    
    else : break