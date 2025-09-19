def criar_pasta(nome):
    return {
        "nome": nome,
        "tipo": "pasta",
        "filhos": []
    }

def criar_arquivo(nome, tamanho):
    return {
        "nome": nome,
        "tipo": "arquivo",
        "tamanho": tamanho
    }

def adicionar_item(pasta_destino, item):
    if pasta_destino["tipo"] != "pasta":
        raise ValueError("Só é possível adicionar itens dentro de pastas.")
    pasta_destino["filhos"].append(item)

def imprimir_estrutura(pasta, prefixo=""):
    nome = pasta["nome"]
    tipo = pasta["tipo"]

    if prefixo == "":
        print(f"└── {nome}/")
    else:
        print(f"{prefixo}└── {nome}/" if tipo == "pasta" else f"{prefixo}└── {nome} ({pasta['tamanho']} KB)")

    if tipo == "pasta":
        filhos = pasta.get("filhos", [])
        for i, filho in enumerate(filhos):
            is_ultimo = (i == len(filhos) - 1)
            novo_prefixo = prefixo + ("    " if is_ultimo else "│   ")
            imprimir_estrutura(filho, novo_prefixo)

def calcular_tamanho(pasta):
    if pasta["tipo"] == "arquivo":
        return pasta["tamanho"]
    total = 0
    for filho in pasta.get("filhos", []):
        total += calcular_tamanho(filho)
    return total

raiz = criar_pasta("root")
docs = criar_pasta("documentos")
img = criar_arquivo("foto.png", 150)
txt = criar_arquivo("texto.txt", 50)

adicionar_item(docs, txt)
adicionar_item(raiz, docs)
adicionar_item(raiz, img)

imprimir_estrutura(raiz)
print("\nTamanho total:", calcular_tamanho(raiz), "KB")
