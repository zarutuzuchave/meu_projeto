
from collections import defaultdict
import json

def salvar_dados(eventos, participantes, nome_arquivo='banco_de_dados.json'):
    """Salva os dados de eventos e participantes no arquivo JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump({"eventos": eventos, "participantes": participantes}, f, indent=2, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except IOError as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

def mostrar_eventos(eventos):
    if not eventos:
        print("Nenhum evento para exibir.")
        return
    print("\n--- Todos os Eventos ---")
    for evento in eventos:
        print(f"Nome: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Tema: {evento['tema']}")
        print("-" * 20)

def adicionar_evento(eventos, participantes, nome, data, tema, lista_participantes_evento=None):
    if any(evento['nome'] == nome for evento in eventos):
        print(f"Erro: Um evento com o nome '{nome}' já existe.")
        return False
    
    novo_evento = {
        "nome": nome,
        "data": data,
        "tema": tema,
        "participantes": lista_participantes_evento if lista_participantes_evento is not None else []
    }
    eventos.append(novo_evento)
    salvar_dados(eventos, participantes) # Salva após adicionar
    print(f"Evento '{nome}' adicionado com sucesso.")
    return True

def remover_evento(eventos, participantes, nome_evento):
    tamanho_original = len(eventos)
    eventos[:] = [evento for evento in eventos if evento['nome'] != nome_evento]
    if len(eventos) < tamanho_original:
        print(f"Evento '{nome_evento}' removido com sucesso.")
        salvar_dados(eventos, participantes) # Salva após remover
        return True
    else:
        print(f"Evento '{nome_evento}' não encontrado.")
        return False

def atualizar_tema_evento(eventos, participantes, nome_evento, novo_tema): 
    for evento in eventos:
        if evento['nome'] == nome_evento:
            evento['tema'] = novo_tema
            print(f"Tema para o evento '{nome_evento}' atualizado para '{novo_tema}'.")
            salvar_dados(eventos, participantes) 
            return True
    print(f"Evento '{nome_evento}' não encontrado.")
    return False

def agrupar_eventos_por_tema(eventos):
    agrupados = defaultdict(list)
    for evento in eventos:
        agrupados[evento['tema']].append(evento)
    return dict(agrupados)

def listar_eventos_por_participante(eventos, codigo_participante):
    eventos_inscritos = [
        evento['nome'] for evento in eventos
        if 'participantes' in evento and codigo_participante in evento['participantes']
    ]
    return eventos_inscritos

def identificar_eventos_baixa_participacao(eventos, min_participantes=2):
    eventos_com_pouca_participacao = [
        evento['nome'] for evento in eventos
        if 'participantes' in evento and len(evento['participantes']) < min_participantes
    ]
    return eventos_com_pouca_participacao