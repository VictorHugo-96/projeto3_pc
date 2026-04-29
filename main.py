from sistema import SteamPy


def menu():
    sistema = SteamPy()

    while True:
        print("\n========= STEAMPY =========")
        print("1. Carregar catálogo")
        print("2. Buscar jogo por nome")
        print("3. Filtrar por gênero")
        print("4. Filtrar por console")
        print("5. Filtrar por nota mínima")
        print("6. Filtrar por vendas mínimas")
        print("7. Filtrar por publisher")
        print("8. Ordenar jogos")
        print("9. Adicionar jogo ao backlog")
        print("10. Ver backlog")
        print("11. Jogar próximo do backlog")
        print("12. Ver jogos recentes")
        print("13. Retomar último jogo")
        print("14. Registrar sessão de jogo")
        print("15. Ver histórico completo")
        print("16. Ver recomendações")
        print("17. Ver ranking pessoal")
        print("18. Ver dashboard")
        print("0. Sair")

        op = input("Escolha uma opção: ").strip()

        
        if op == "1":
            sistema.carregar_jogos("dataset.csv")

        
        elif op == "2":
            sistema.buscar_jogo_por_nome(input("Digite parte do nome: "))

        
        elif op == "3":
            sistema.filtrar_por_genero(input("Gênero: "))

        elif op == "4":
            sistema.filtrar_por_console(input("Console: "))

        elif op == "5":
            try:
                sistema.filtrar_por_nota(float(input("Nota mínima: ")))
            except:
                print("Valor inválido")

        elif op == "6":
            try:
                sistema.filtrar_por_vendas(float(input("Vendas mínimas: ")))
            except:
                print("Valor inválido")

        elif op == "7":
            sistema.filtrar_por_publisher(input("Publisher: "))

        
        elif op == "8":
            print("Critérios: titulo | nota | vendas | data | console | genero")
            sistema.ordenar_jogos(input("Escolha: "))

        
        elif op == "9":

            if not sistema.catalogo_carregado():
                print("⚠ Carregue o catálogo primeiro (opção 1)")
                continue

            termo = input("Digite parte do nome do jogo: ").strip().lower()

            encontrados = [j for j in sistema.catalogo if termo in j.titulo.lower()]

            if not encontrados:
                print("Nenhum jogo encontrado")
                continue

            print("\n--- RESULTADOS ---")
            lista = encontrados[:10]

            for i, j in enumerate(lista, 1):
                print(f"{i}. ", end="")
                j.exibir()

            escolha = input("\nEscolha o número do jogo: ").strip()

            if not escolha.isdigit():
                print("Entrada inválida (use número)")
                continue

            escolha = int(escolha)

            if escolha < 1 or escolha > len(lista):
                print("Escolha fora da lista")
                continue

            jogo = lista[escolha - 1]

            sistema.adicionar_ao_backlog(jogo.id)
            sistema.salvar_backlog()

            print("Adicionado ao backlog:", jogo.titulo)

        
        elif op == "10":
            sistema.backlog.mostrar()

        elif op == "11":
            sistema.jogar_proximo()

        
        elif op == "12":
            sistema.recentes.mostrar()

        elif op == "13":
            jogo = sistema.recentes.topo()
            if jogo:
                print("Retomando:")
                jogo.exibir()
            else:
                print("Nenhum jogo recente")

        
        elif op == "14":
            try:
                idj = int(input("ID do jogo: "))
                tempo = float(input("Horas jogadas: "))

                jogo = sistema.jogos_dict.get(idj)

                if jogo:
                    sistema.registrar_sessao(jogo, tempo)
                else:
                    print("Jogo não encontrado")

            except:
                print("Entrada inválida")

        
        elif op == "15":
            sistema.mostrar_historico()

        
        elif op == "16":
            sistema.recomendar_jogos()

        
        elif op == "17":
            sistema.ranking()

        
        elif op == "18":
            sistema.dashboard()

        
        elif op == "0":
            sistema.salvar_backlog()
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu()