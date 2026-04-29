class FilaBacklog:
    def __init__(self):
        self.dados = []

    def enqueue(self, jogo):
        if jogo not in self.dados:
            self.dados.append(jogo)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.dados.pop(0)

    def is_empty(self):
        return len(self.dados) == 0

    def mostrar(self):
        if self.is_empty():
            print("Backlog vazio")
            return

        print("\n--- BACKLOG ---")
        for i, j in enumerate(self.dados, 1):
            print(f"{i}. ", end="")
            j.exibir()

    def tamanho(self):
        return len(self.dados)
