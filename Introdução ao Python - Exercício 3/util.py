# util.py
def gerar_registro(dados):
    dados_lista = dados.split(';')
    
    registro = {
        "nome": dados_lista[0],
        "cidade": dados_lista[1],
        "idade": int(dados_lista[2]),
        "renda": float(dados_lista[3])
    }
    
    return registro
