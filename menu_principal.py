
import dados_eventos
import dados_participantes
from menu_eventos import executar_menu_gerenciar_eventos
from menu_participantes import executar_menu_gerenciar_participantes
from menu_relatorios import executar_menu_relatorios
import funcoes_eventos as GerenciadorEventos
from apagar_terminal import clear

def executar_menu_principal():
    eventos = dados_eventos.carregar_dados_eventos()
    participantes = dados_participantes.carregar_dados_participantes()

    opcoes_menu = {
        '1': ("Ver Eventos", lambda: GerenciadorEventos.mostrar_eventos(eventos)),
        '2': ("Gerenciar Eventos", lambda: executar_menu_gerenciar_eventos(eventos, participantes)),
        '3': ("Gerenciar Participantes", lambda: executar_menu_gerenciar_participantes(eventos, participantes)), 
        '4': ("Relatórios e Estatísticas", lambda: executar_menu_relatorios(eventos, participantes)),
        '5': ("Apagar Terminal", clear),
        '6': ("Sair", None),
    }

    while True:
        print("\n--- Sistema de Gerenciamento de Eventos ---")
        for chave, (descricao, _) in opcoes_menu.items():
            print(f"{chave}. {descricao}")

        escolha = input("Digite sua escolha: ")

        acao = opcoes_menu.get(escolha)
        if acao:
            descricao, funcao = acao
            if funcao:
                funcao()
            else:
                print("Saindo do sistema. Até logo!")
                break
        else:
            print("Escolha inválida. Por favor, tente novamente.")