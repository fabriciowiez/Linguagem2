class Contato:
    def __init__(self, nome, num):
        self.nome = nome
        self.num = num
    
    def __str__(self):
        return f"Contato: {self.nome} - Número: {self.num}"
    
class Agenda:
    agendaContatos = []

    def addContato(self, contato):
        self.agendaContatos.append(contato)
    
    def listarContatos(self):
        for cont in self.agendaContatos:
            print(cont)

agd = Agenda()

while 1:
    print("1 - Adicionar contato")
    print("2 - Mostrar agenda de contatos")
    print("0 - Sair")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        nome = str(input("Digite o nome do contato: "))
        numero = int(input("Digite o número do contato: "))
        cont = Contato(nome, numero)
        agd.addContato(cont)

    elif opcao == 2:
        agd.listarContatos()
    
    else : break