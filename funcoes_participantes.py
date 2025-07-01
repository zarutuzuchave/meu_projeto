import funcoes_eventos as GerenciadorEventos
from funcoes_eventos import salvar_dados


def mostrar_participantes_em_evento(eventos, dados_participantes, nome_evento):
    evento_encontrado = False
    for evento in eventos:
        if evento['nome'] == nome_evento:
            evento_encontrado = True
            print(f"\n--- Participantes em {nome_evento} ---")
            if 'participantes' in evento and evento['participantes']:
                codigos_participantes_evento = set(evento['participantes'])
                participantes_do_evento = list(filter(
                    lambda p: p['codigo'] in codigos_participantes_evento,
                    dados_participantes
                ))
                if participantes_do_evento:
                    for participante in participantes_do_evento:
                        print(f"Código: {participante['codigo']}, Nome: {participante['nome_completo']}, E-mail: {participante['email']}")
                else:
                    print("Nenhum participante registrado para este evento.")
            else:
                print("Nenhum participante registrado para este evento.")
            break
    if not evento_encontrado:
        print(f"Evento '{nome_evento}' não encontrado.")
def adicionar_participante(novo_participante, participantes, codigo, nome_completo, email , lista_temas=None):
    
    novo_participante = {
        "codigo": codigo,
        "nome_completo": nome_completo,
        "email": email,
        "preferencias_tematicas": lista_temas if lista_temas is not None else [],
    }
    participantes.append(novo_participante)
    salvar_dados(participantes)
    print(f"Participante '{nome_completo}' adicionado com sucesso.")
    return True

def buscar_participante(participantes, codigo_participante):
    encontrado = next(filter(lambda p: p['codigo'] == codigo_participante, participantes), None)
    if encontrado:
        print(f"\n--- Participante Encontrado ---")
        print(f"Código: {encontrado['codigo']}")
        print(f"Nome: {encontrado['nome_completo']}")
        print(f"E-mail: {encontrado['email']}")
        print(f"Preferências: {encontrado['preferencias_tematicas']}")
    else:
        print(f"Participante com o código '{codigo_participante}' não encontrado.")
    return encontrado

def atualizar_email_participante(eventos, participantes, codigo_participante, novo_email):
    for participante in participantes:
        if participante['codigo'] == codigo_participante:
            participante['email'] = novo_email
            print(f"E-mail do participante '{codigo_participante}' atualizado para '{novo_email}'.")
            GerenciadorEventos.salvar_dados(eventos, participantes) 
            return True
    print(f"Participante com o código '{codigo_participante}' não encontrado.")
    return False

def remover_participantes_duplicados(eventos, participantes):
    codigos_vistos = set()
    participantes_unicos = []
    contador_removidos = 0

    for participante in participantes:
        if participante['codigo'] not in codigos_vistos:
            participantes_unicos.append(participante)
            codigos_vistos.add(participante['codigo'])
        else:
            contador_removidos += 1
            print(f"Participante duplicado encontrado e removido: Código {participante['codigo']}")

    if contador_removidos > 0:
        print(f"Removido(s) {contador_removidos} registro(s) duplicado(s) de participante.")
        GerenciadorEventos.salvar_dados(eventos, participantes_unicos) 
    else:
        print("Nenhum participante duplicado encontrado.")
    return participantes_unicos

