class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
    
    def getDados(self):
        print(f"Dados do animal: {self.nome} - {self.raca}")

    def caminha(self):
        print(f"{self.nome} caminha")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def late(self):
        print(f"O cachorro late!")

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def mia(self):
        print(f"O gato mia!")

cachorro = Cachorro("Rodolfo", "Dobermann")
cachorro.getDados()
cachorro.late()

gato = Gato("Alex", "Siamês")
gato.getDados()
gato.mia()