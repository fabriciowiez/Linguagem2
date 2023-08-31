class Relogio:
    hora = 0
    minuto = 0
    segundo = 0

    def setHora(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def getHora(self):
        return self.hora, self.minuto, self.segundo

    def avancarHora(self):
        self.segundo += 1
        if(self.segundo >= 60):
            self.segundo = 0
            self.minuto += 1
            if(self.minuto >= 60):
                self.minuto = 0
                self.hora += 1

r = Relogio()

while 1:
    print("1 - Setar Hora")
    print("2 - Mostrar Hora")
    print("3 - Avançar Horário")
    print("0 - Sair")

    opc = int(input("Digite sua opção: "))

    if(opc == 1):
        hora = int(input("Informe a hora: "))
        minuto = int(input("Informe o minuto: "))
        segundo = int(input("Informe o segundo: "))

        r.setHora(hora, minuto, segundo)

    elif opc == 2 : print(f"Horário atual: {r.hora}:{r.minuto}:{r.segundo}")

    elif opc == 3 : r.avancarHora()

    else : break