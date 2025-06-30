import json
import datetime

def formatar_data(eventos):
    formatos_entrada = [
        "%Y-%m-%d",  
        "%m/%d/%Y",  
        "%d-%m-%Y",  
        "%d/%m/%Y",  
    ]
    for evento in eventos:
        data_str = evento.get('data') 
        if data_str:
            data_valida = False
            for fmt in formatos_entrada:
                try:
                    data_obj = datetime.datetime.strptime(data_str, fmt)
                    evento['data'] = data_obj.strftime("%d/%m/%Y")
                    data_valida = True
                    break 
                except ValueError:
                    continue

            if not data_valida:
                print(f"Data inválida encontrada para o evento '{evento['nome']}': '{data_str}'. A data não será formatada.")
                evento['data'] = "Data Inválida"
        else:
            print(f" O evento '{evento.get('nome', 'Nome Desconhecido')}' não possui a chave 'data'.")

    return eventos

def carregar_dados_eventos(nome_arquivo='banco_de_dados.json'):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load()
            eventos_carregados = formatar_data(dados.get('eventos', []))
            return eventos_carregados
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com eventos vazios.")
        return []
    except json.JSONDecodeError:
        print(f"Error 404'{nome_arquivo}'. Arquivo não válidado.")
        return []
eventos = []