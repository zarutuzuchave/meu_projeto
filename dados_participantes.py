import json

def carregar_dados_participantes(nome_arquivo='banco_de_dados.json'):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return dados.get('participantes', [])
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com participantes vazios.")
        return []
    except json.JSONDecodeError:
        print(f"Error 404 '{nome_arquivo}'. Arquivo não válidado.")
        return []
participantes = []
