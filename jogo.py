class Jogo:
    def __init__(self, id_jogo, titulo, console, genero, publisher,
                 developer, critic_score, total_sales,
                 na_sales, jp_sales, pal_sales, other_sales, release_date):

        self.id = id_jogo
        self.titulo = titulo.strip()
        self.console = console.strip()
        self.genero = genero.strip()
        self.publisher = publisher.strip()
        self.developer = developer.strip()
        self.critic_score = float(critic_score or 0)
        self.total_sales = float(total_sales or 0)
        self.release_date = release_date.strip()

    def exibir(self):
        print(f"{self.id} | {self.titulo} | {self.console} | {self.genero} | Nota: {self.critic_score} | Vendas: {self.total_sales}")

    def linha_backlog(self):
        return f"{self.id};{self.titulo};{self.console}"
