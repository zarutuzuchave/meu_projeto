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
    

eventos = [
    {
        'nome': 'Workshop de Fundamentos de Python',
        'data': '2025-07-10',
        'tema': 'Web',
        'participantes': ['P001', 'P002', 'P003', 'P005']
    },
    {
        'nome': 'Seminário de IA na Saúde',
        'data': '2025-07-15',
        'tema': 'Inteligência Artificial',
        'participantes': ['P001', 'P004', 'P006']
    },
    {
        'nome': 'Fundamentos de Cibersegurança',
        'data': '2025-07-20',
        'tema': 'Segurança',
        'participantes': ['P002', 'P005']
    },
    {
        'nome': 'Bootcamp de Desenvolvimento Web',
        'data': '2025-08-01',
        'tema': 'Web',
        'participantes': ['P001', 'P003', 'P004', 'P007']
    },
    {
        'nome': 'Meetup de Ciência de Dados',
        'data': '2025-08-05',
        'tema': 'Inteligência Artificial',
        'participantes': ['P002', 'P006', 'P008']
    },
    {
        'nome': 'Essenciais de Redes',
        'data': '2025-08-10',
        'tema': 'Segurança',
        'participantes': ['P009']
    }
]
