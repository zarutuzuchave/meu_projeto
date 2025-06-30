from apagar_terminal import clear
import funcoes_eventos as GerenciadorEventos

def executar_menu_gerenciar_eventos(eventos, dados_participantes): 

    def _adicionar_evento():
        nome = input("Nome do evento: ")
        data = input("Data do evento (AAAA-MM-DD): ")
        tema = input("Tema do evento: ")
        GerenciadorEventos.adicionar_evento(eventos, dados_participantes, nome, data, tema)

    def _remover_evento():
        nome_evento = input("Nome do evento para remover: ")
        GerenciadorEventos.remover_evento(eventos, dados_participantes, nome_evento)

    def _atualizar_tema():
        nome_evento = input("Nome do evento para atualizar o tema: ")
        novo_tema = input("Novo tema: ")
        GerenciadorEventos.atualizar_tema_evento(eventos, dados_participantes, nome_evento, novo_tema)

    def _agrupar():
        agrupados = GerenciadorEventos.agrupar_eventos_por_tema(eventos)
        for tema, lista_eventos in agrupados.items():
            print(f"\nTema: {tema}")
            for evento in lista_eventos:
                print(f"  - {evento['nome']} em {evento['data']}")

    def _listar_por_participante():
        codigo_participante = input("Digite o código do participante: ")
        eventos_inscritos = GerenciadorEventos.listar_eventos_por_participante(eventos, codigo_participante)
        if eventos_inscritos:
            print(f"\nEventos em que {codigo_participante} está inscrito:")
            for nome_evento in eventos_inscritos:
                print(f"- {nome_evento}")
        else:
            print(f"O participante {codigo_participante} não está inscrito em nenhum evento ou não existe.")

    def _identificar_baixa_participacao():
        eventos_com_pouca_participacao = GerenciadorEventos.identificar_eventos_baixa_participacao(eventos)
        if eventos_com_pouca_participacao:
            print("\nEventos com baixa participação (menos de 2 participantes):")
            for nome_evento in eventos_com_pouca_participacao:
                print(f"- {nome_evento}")
        else:
            print("Nenhum evento com baixa participação encontrado.")

    opcoes_menu = {
        '1': ("Adicionar Novo Evento", _adicionar_evento),
        '2': ("Remover Evento", _remover_evento),
        '3': ("Atualizar Tema do Evento", _atualizar_tema),
        '4': ("Agrupar Eventos por Tema", _agrupar),
        '5': ("Listar Eventos por Participante", _listar_por_participante),
        '6': ("Identificar Eventos com Baixa Participação", _identificar_baixa_participacao),
        '7': ("Apagar Terminal", clear),
        '8': ("Voltar ao Menu Principal", None)
    }

    while True:
        print("\n--- Gerenciar Eventos ---")
        for chave, (descricao, _) in opcoes_menu.items():
            print(f"{chave}. {descricao}")

        escolha = input("Digite sua escolha: ")

        acao = opcoes_menu.get(escolha)
        if acao:
            descricao, funcao = acao
            if funcao:
                funcao()
            else:
                break
        else:
            print("Escolha inválida. Por favor, tente novamente.")