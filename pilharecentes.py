class PilhaRecentes:
    def __init__(self, limite=20):
        self.dados = []
        self.limite = limite

    def push(self, jogo):
        self.dados = [j for j in self.dados if j.id != jogo.id]
        self.dados.append(jogo)

        if len(self.dados) > self.limite:
            self.dados.pop(0)

    def topo(self):
        return self.dados[-1] if self.dados else None

    def mostrar(self):
        if not self.dados:
            print("Nenhum jogo recente")
            return

        print("\n--- RECENTES ---")
        for j in reversed(self.dados):
            j.exibir()

    def tamanho(self):
        return len(self.dados)
