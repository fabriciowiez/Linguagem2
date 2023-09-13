class Emprestimo:
    def __init__(self, livro, pessoa):
        self.livro = livro
        self.pessoa = pessoa

    def realizarEmprestimo(self):
        if not self.livro.emprestado:
            if self.livro.emprestarLivro(): 
                return True
        return False
        
    def realizarDevolucao(self):
        if self.livro.emprestado:
            if self.livro.devolverLivro():
                return True
        return False

class Livro:
    def __init__(self, nomeLivro):
        self.nomeLivro = nomeLivro
        self.emprestado = False

    def __str__(self):
        if self.emprestado:
            status = "Disponível"
        else:
            status = "Emprestado"
        return f"{self.nomeLivro} - {status}"
    
    def emprestarLivro(self):
        if not self.emprestado:
            self.emprestado = True
            return True
        return False
        
    def devolverLivro(self):
        if self.emprestado:
            self.emprestado = False
            return True
        return False

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return f"{self.nome}"

l = Livro("O Hobbit")
p = Pessoa("Fabrício")
e = Emprestimo(l, p)

while True:
    print("1 - Realizar Empréstimo")
    print("2 - Realizar Devolução")
    print("0 - Sair")

    opc = int(input("Digite sua opção: "))

    if opc == 1:
        if e.realizarEmprestimo():
            print(f"{p.nome} - emprestou o livro {l.nomeLivro}")
        else:
            print(f"O livro {l.nomeLivro} já está emprestado para {p.nome}")

    elif opc == 2:
        if e.realizarDevolucao():
            print(f"{p.nome} devolveu o livro {l.nomeLivro}")
        else:
            print(f"O livro {l.nomeLivro} não estava emprestado")

    elif opc == 0:
        break
