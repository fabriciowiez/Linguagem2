class CadastroEmpregado:
    nome = None
    idade = None
    funcao = None
    dataNascimento = None
    telefone = None
    peso = None
    altura = None
    salario = None

    def getNome(self): return self.nome
    def getIdade(self): return self.idade
    def getFuncao(self): return self.funcao
    def getDataNascimento(self): return self.dataNascimento
    def getTelefone(self): return self.telefone
    def getPeso(self): return self.peso
    def getAltura(self): return self.altura
    def getSalario(self): return self.salario

    def setNome(self, nome): self.nome = nome
    def setIdade(self, idade): self.idade = idade
    def setFuncao(self, funcao): self.funcao = funcao
    def setDataNascimento(self, dataNascimento): self.dataNascimento = dataNascimento
    def setTelefone(self, telefone): self.telefone = telefone
    def setPeso(self, peso): self.peso = peso
    def setAltura(self, altura): self.altura = altura
    def setSalario(self, salario): self.salario = salario

    def cadastrarEmpregado(self):
        self.setNome(str(input("Digite o nome: ")))
        self.setIdade(int(input("Digite a idade: ")))
        self.setFuncao(str(input("Digite a função: ")))
        self.setDataNascimento(str(input("Digite a data de nascimento: ")))
        self.setTelefone(str("Digite o telefone: "))
        self.setPeso(float(input("Digite o peso: ")))
        self.setAltura(float(input("Digite a altura: ")))
        self.setSalario(float(input("Digite o salário: ")))
    
    def mostrarEmpregado(self):
        print(f"Nome: {self.getNome()}")
        print(f"Idade: {self.getIdade()}")
        print(f"Função: {self.getFuncao()}")
        print(f"Data de Nascimento: {self.getDataNascimento()}")
        print(f"Telefone: {self.getTelefone()}")
        print(f"Peso: {self.getPeso()}")
        print(f"Altura: {self.getAltura()}")
        print(f"Salário: {self.getSalario()}")

empregado = CadastroEmpregado()

while 1:
    print("1 - Cadastrar um novo empregado")
    print("2 - Ver empregado cadastrado")
    print("0 - Sair")

    opc = int(input("Digite sua opção: "))

    if opc == 1 : empregado.cadastrarEmpregado()
    elif opc == 2 : empregado.mostrarEmpregado()
    else : break