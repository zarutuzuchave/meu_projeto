
import funcoes_relatorios as FuncoesRelatorios

def executar_menu_relatorios(eventos, dados_participantes):

    def _participantes_ativos():
        FuncoesRelatorios.obter_participantes_mais_ativos(eventos, dados_participantes)

    def _temas_frequentes():
        FuncoesRelatorios.obter_temas_mais_frequentes(eventos)

    def _contar_eventos_por_tema():
        contagem_temas = FuncoesRelatorios.contar_eventos_por_tema(eventos)
        print("\nEventos por Tema:")
        for tema, contagem in contagem_temas.items():
            print(f"- {tema}: {contagem} eventos")

    def _media_participacao():
        taxas_medias = FuncoesRelatorios.calcular_media_participacao_por_tema(eventos)
        print("\nTaxa Média de Participação por Tema:")
        for tema, taxa in taxas_medias.items():
            print(f"- {tema}: {taxa:.2f} participantes por evento")

    def _relatorio_baixa_participacao():
        eventos_com_pouca_participacao = FuncoesRelatorios.relatorio_eventos_baixa_participacao(eventos)
        if eventos_com_pouca_participacao:
            print("\nRelatório de Eventos com Baixa Participação:")
            for nome_evento in eventos_com_pouca_participacao:
                print(f"- {nome_evento}")
        else:
            print("Nenhum evento com baixa participação para relatar.")

    opcoes_menu = {
        '1': ("Participantes Mais Ativos", _participantes_ativos),
        '2': ("Temas Mais Frequentes", _temas_frequentes),
        '3': ("Contar Eventos por Tema", _contar_eventos_por_tema),
        '4': ("Taxa Média de Participação por Tema", _media_participacao),
        '5': ("Eventos com Baixa Participação (Relatório)", _relatorio_baixa_participacao),
        '6': ("Voltar ao Menu Principal", None)
    }

    while True:
        print("\n--- Relatórios e Estatísticas ---")
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