class SessaoJogo:
    def __init__(self, jogo, tempo, total):
        self.jogo = jogo
        self.tempo = tempo
        self.total = total
        self.status = self.definir_status()

    def definir_status(self):
        if self.total < 2:
            return "iniciado"
        elif self.total < 10:
            return "em andamento"
        elif self.total < 20:
            return "muito jogado"
        return "concluido"

    def exibir(self):
        print(f"{self.jogo.titulo} | sessão {self.tempo}h | total {self.total}h | {self.status}")