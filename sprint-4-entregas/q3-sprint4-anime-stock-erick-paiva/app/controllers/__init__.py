

def verifica_chaves(data:dict):
    chaves_validas = ["anime","released_date" , "seasons"]
    chaves_erradas = []
    for chave in data.keys():
        if not chave in chaves_validas:
            chaves_erradas.append(chave)
    if chaves_erradas:
        return {"available_keys": chaves_validas, "wrong_keys_sended" : chaves_erradas }
    