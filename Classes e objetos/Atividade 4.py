class Lampada:

    def estaLigada(self, luz):
        if(luz == 0) : return 0
        else : return 1

luz = int(input("Informe 1 para luz ligada e 0 para desligada: "))
l = Lampada()
ligada = l.estaLigada(luz)

if (ligada): print("A lampada esta ligada")
else : print("A lampada esta desligada") 