import funcoes_participantes as GerenciadorParticipantes
from apagar_terminal import clear

def executar_menu_gerenciar_participantes(eventos, dados_participantes):

    def _listar_em_evento():
        nome_evento = input("Digite o nome do evento: ")
        GerenciadorParticipantes.mostrar_participantes_em_evento(eventos, dados_participantes, nome_evento)

    def _buscar_participante():
        codigo_participante = input("Digite o código do participante: ")
        GerenciadorParticipantes.buscar_participante(dados_participantes, codigo_participante)

    def _atualizar_email():
        codigo_participante = input("Digite o código do participante: ")
        novo_email = input("Digite o novo e-mail: ")
        GerenciadorParticipantes.atualizar_email_participante(eventos, dados_participantes, codigo_participante, novo_email)

    def _remover_duplicados():
        dados_participantes[:] = GerenciadorParticipantes.remover_participantes_duplicados(eventos, dados_participantes)

    opcoes_menu = {
        '1': ("Listar Participantes em um Evento", _listar_em_evento),
        '2': ("Buscar Participante por Código", _buscar_participante),
        '3': ("Atualizar E-mail do Participante", _atualizar_email),
        '4': ("Remover Participantes Duplicados", _remover_duplicados),
        '5': ("Apagar Terminal", clear),
        '6': ("Voltar ao Menu Principal", None)
    }

    while True:
        print("\n--- Gerenciar Participantes ---")
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