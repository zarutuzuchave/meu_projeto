
from collections import Counter, defaultdict
from functools import reduce

def obter_participantes_mais_ativos(eventos, dados_participantes, top_n=5):
    todos_codigos_participantes = []
    for evento in eventos:
        if 'participantes' in evento:
            todos_codigos_participantes.extend(evento['participantes'])

    contagem_participantes = Counter(todos_codigos_participantes)
    mapa_nomes_participantes = {p['codigo']: p['nome_completo'] for p in dados_participantes}

    participantes_ativos = [
        (mapa_nomes_participantes.get(codigo, f"Desconhecido ({codigo})"), contagem)
        for codigo, contagem in contagem_participantes.items()
    ]
    participantes_ativos.sort(key=lambda x: x[1], reverse=True)

    print("\n--- Participantes Mais Ativos ---")
    for nome, contagem in participantes_ativos[:top_n]:
        print(f"- {nome}: {contagem} eventos")

    return participantes_ativos[:top_n]

def obter_temas_mais_frequentes(eventos, top_n=5):
    todos_temas = [evento['tema'] for evento in eventos if 'tema' in evento]
    contagem_temas = Counter(todos_temas)
    temas_frequentes = sorted(contagem_temas.items(), key=lambda item: item[1], reverse=True)

    print("\n--- Temas Mais Frequentes ---")
    for tema, contagem in temas_frequentes[:top_n]:
        print(f"- {tema}: {contagem} eventos")

    return temas_frequentes[:top_n]

def contar_eventos_por_tema(eventos):
    contagem_temas = reduce(
        lambda acumulador, evento: {**acumulador, evento['tema']: acumulador.get(evento['tema'], 0) + 1},
        eventos,
        {}
    )
    return contagem_temas

def calcular_media_participacao_por_tema(eventos):
    somas_participacao_tema = defaultdict(int)
    contagem_eventos_tema = defaultdict(int)

    for evento in eventos:
        tema = evento.get('tema')
        participantes = evento.get('participantes', [])
        if tema:
            somas_participacao_tema[tema] += len(participantes)
            contagem_eventos_tema[tema] += 1

    media_taxas_participacao = {
        tema: somas_participacao_tema[tema] / contagem_eventos_tema[tema]
        for tema in contagem_eventos_tema
    }
    return media_taxas_participacao

def relatorio_eventos_baixa_participacao(eventos, min_participantes=2):
    eventos_com_pouca_participacao = []
    for evento in eventos:
        if 'participantes' in evento and len(evento['participantes']) < min_participantes:
            eventos_com_pouca_participacao.append(evento['nome'])
    return eventos_com_pouca_participacao
