import csv
from jogo import Jogo
from backlog import FilaBacklog
from pilharecentes import PilhaRecentes
from sessao import SessaoJogo


class SteamPy:
    def __init__(self):
        self.catalogo = []
        self.jogos_dict = {}

        self.backlog = FilaBacklog()
        self.recentes = PilhaRecentes()

        self.historico = []
        self.tempo_por_jogo = {}

    
    def catalogo_carregado(self):
        return len(self.catalogo) > 0

    
    def carregar_jogos(self, arquivo):
        self.catalogo = []
        self.jogos_dict = {}

        with open(arquivo, encoding="latin-1") as f:
            leitor = csv.reader(f)
            next(leitor)

            for i, p in enumerate(leitor):
                try:
                    if len(p) < 13:
                        continue

                    jogo = Jogo(
                        i,
                        p[1],
                        p[2],
                        p[3],
                        p[4],
                        p[5],
                        p[6],
                        p[7],
                        p[8],
                        p[9],
                        p[10],
                        p[11],
                        p[12]
                    )

                    self.catalogo.append(jogo)
                    self.jogos_dict[jogo.id] = jogo

                except:
                    continue

        print(f"Jogos carregados: {len(self.catalogo)}")

    
    def buscar_jogo_por_nome(self, termo):
        if not self.catalogo_carregado():
            print("Catálogo não carregado")
            return

        termo = termo.lower()
        encontrados = [j for j in self.catalogo if termo in j.titulo.lower()]

        if not encontrados:
            print("Nenhum jogo encontrado")
            return

        print("\n--- RESULTADOS ---")
        for j in encontrados[:20]:
            j.exibir()

    
    def filtrar_por_genero(self, g):
        for j in self.catalogo:
            if j.genero.lower() == g.lower():
                j.exibir()

    def filtrar_por_console(self, c):
        for j in self.catalogo:
            if j.console.lower() == c.lower():
                j.exibir()

    def filtrar_por_nota(self, n):
        for j in self.catalogo:
            if j.critic_score >= n:
                j.exibir()

    def filtrar_por_vendas(self, v):
        for j in self.catalogo:
            if j.total_sales >= v:
                j.exibir()

    def filtrar_por_publisher(self, p):
        for j in self.catalogo:
            if j.publisher.lower() == p.lower():
                j.exibir()

    
    def ordenar_jogos(self, c):
        if c == "nota":
            lista = sorted(self.catalogo, key=lambda x: x.critic_score, reverse=True)
        elif c == "vendas":
            lista = sorted(self.catalogo, key=lambda x: x.total_sales, reverse=True)
        elif c == "data":
            lista = sorted(self.catalogo, key=lambda x: x.release_date)
        elif c == "console":
            lista = sorted(self.catalogo, key=lambda x: x.console)
        elif c == "genero":
            lista = sorted(self.catalogo, key=lambda x: x.genero)
        else:
            lista = sorted(self.catalogo, key=lambda x: x.titulo)

        for j in lista[:20]:
            j.exibir()

    
    def adicionar_ao_backlog(self, idj):
        jogo = self.jogos_dict.get(idj)

        if not jogo:
            print("Jogo não encontrado")
            return

        self.backlog.enqueue(jogo)
        print("Adicionado ao backlog:", jogo.titulo)

    def salvar_backlog(self):
        try:
            with open("backlog.txt", "w", encoding="utf-8") as f:
                for j in self.backlog.dados:
                    f.write(j.linha_backlog() + "\n")
        except:
            print("Erro ao salvar backlog")

    def jogar_proximo(self):
        if self.backlog.is_empty():
            print("Backlog vazio")
            return

        j = self.backlog.dequeue()
        print("Jogando:")
        j.exibir()
        self.recentes.push(j)

    
    def registrar_sessao(self, jogo, tempo):
        total = self.tempo_por_jogo.get(jogo.id, 0) + tempo
        self.tempo_por_jogo[jogo.id] = total

        s = SessaoJogo(jogo, tempo, total)
        self.historico.append(s)
        self.recentes.push(jogo)

        s.exibir()

    
    def mostrar_historico(self):
        if not self.historico:
            print("Sem histórico")
            return

        for h in self.historico:
            h.exibir()

    
    def recomendar_jogos(self):
        if not self.historico:
            print("Sem dados suficientes para recomendação")
            return

        genero_count = {}
        console_count = {}

        for h in self.historico:
            g = h.jogo.genero
            c = h.jogo.console

            genero_count[g] = genero_count.get(g, 0) + 1
            console_count[c] = console_count.get(c, 0) + 1

        genero_favorito = max(genero_count, key=genero_count.get)
        console_favorito = max(console_count, key=console_count.get)

        print("\n--- RECOMENDAÇÕES PERSONALIZADAS ---")
        print(f"Baseado em gênero: {genero_favorito}")
        print(f"Baseado em console: {console_favorito}\n")

        recomendados = []

        for j in self.catalogo:
            if (
                j.genero == genero_favorito
                and j.console == console_favorito
                and j.critic_score >= 7
            ):
                recomendados.append(j)

        if not recomendados:
            print("Nenhuma recomendação encontrada com base no seu perfil.")
            return

        recomendados = sorted(recomendados, key=lambda x: x.critic_score, reverse=True)

        for j in recomendados[:10]:
            j.exibir()

    
    def ranking(self):
        if not self.tempo_por_jogo:
            print("Sem dados")
            return

        for idj, t in sorted(self.tempo_por_jogo.items(), key=lambda x: x[1], reverse=True):
            self.jogos_dict[idj].exibir()
            print("Horas:", t)

    
    def dashboard(self):
        print("\n--- DASHBOARD ---")
        print("Jogos:", len(self.catalogo))
        print("Backlog:", self.backlog.tamanho())
        print("Recentes:", self.recentes.tamanho())
        print("Sessões:", len(self.historico))