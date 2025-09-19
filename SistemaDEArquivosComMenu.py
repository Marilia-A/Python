def criar_pasta(nome):
    return {"nome": nome, "tipo": "pasta", "filhos": []}

def criar_arquivo(nome, tamanho):
    return {"nome": nome, "tipo": "arquivo", "tamanho": tamanho}

def adicionar_item(pasta_destino, item):
    if pasta_destino["tipo"] != "pasta":
        raise ValueError("Só é possível adicionar itens dentro de pastas.")
    pasta_destino["filhos"].append(item)

def imprimir_estrutura(pasta, prefixo=""):
    nome, tipo = pasta["nome"], pasta["tipo"]
    if prefixo == "":
        print(f"└── {nome}/")
    else:
        print(f"{prefixo}└── {nome}/" if tipo == "pasta" else f"{prefixo}└── {nome} ({pasta['tamanho']} KB)")
    if tipo == "pasta":
        filhos = pasta["filhos"]
        for i, filho in enumerate(filhos):
            novo_prefixo = prefixo + ("    " if i == len(filhos) - 1 else "│   ")
            imprimir_estrutura(filho, novo_prefixo)

def calcular_tamanho(pasta):
    if pasta["tipo"] == "arquivo":
        return pasta["tamanho"]
    return sum(calcular_tamanho(f) for f in pasta["filhos"])

def imprimir_pre_ordem(pasta):
    print(f"{pasta['nome']}/" if pasta["tipo"] == "pasta" else f"{pasta['nome']} ({pasta['tamanho']} KB)")
    if pasta["tipo"] == "pasta":
        for filho in pasta["filhos"]:
            imprimir_pre_ordem(filho)

def imprimir_pos_ordem(pasta):
    if pasta["tipo"] == "pasta":
        for filho in pasta["filhos"]:
            imprimir_pos_ordem(filho)
    print(f"{pasta['nome']}/" if pasta["tipo"] == "pasta" else f"{pasta['nome']} ({pasta['tamanho']} KB)")

def buscar_arquivo(pasta, nome_arquivo):
    if pasta["tipo"] == "arquivo" and pasta["nome"] == nome_arquivo:
        return pasta
    elif pasta["tipo"] == "pasta":
        for filho in pasta["filhos"]:
            resultado = buscar_arquivo(filho, nome_arquivo)
            if resultado:
                return resultado
    return None

def buscar_pasta(pasta, nome_pasta):
    if pasta["tipo"] == "pasta" and pasta["nome"] == nome_pasta:
        return pasta
    elif pasta["tipo"] == "pasta":
        for filho in pasta["filhos"]:
            resultado = buscar_pasta(filho, nome_pasta)
            if resultado:
                return resultado
    return None

def main():
    raiz = criar_pasta("root")
    print("Sistema de arquivos iniciado com pasta raiz 'root'.")

    # Dicionários para armazenar pastas e arquivos criados, facilitar busca para adicionar
    pastas_criadas = {"root": raiz}
    arquivos_criados = {}

    while True:
        print("\nMenu:")
        print("1 - Criar pasta")
        print("2 - Criar arquivo")
        print("3 - Adicionar item")
        print("4 - Imprimir pré-ordem")
        print("5 - Imprimir pós-ordem")
        print("6 - Buscar arquivo")
        print("7 - Buscar pasta")
        print("8 - Imprimir árvore")
        print("9 - Calcular tamanho de pasta")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da nova pasta: ").strip()
            if nome in pastas_criadas or nome in arquivos_criados:
                print("Nome já existe.")
                continue
            pasta = criar_pasta(nome)
            pastas_criadas[nome] = pasta
            print(f"Pasta '{nome}' criada.")

        elif escolha == "2":
            nome = input("Nome do arquivo: ").strip()
            if nome in arquivos_criados or nome in pastas_criadas:
                print("Nome já existe.")
                continue
            try:
                tamanho = int(input("Tamanho (KB): "))
            except ValueError:
                print("Tamanho inválido.")
                continue
            arquivo = criar_arquivo(nome, tamanho)
            arquivos_criados[nome] = arquivo
            print(f"Arquivo '{nome}' criado com tamanho {tamanho} KB.")

        elif escolha == "3":
            destino = input("Nome da pasta destino: ").strip()
            if destino not in pastas_criadas:
                print(f"Pasta '{destino}' não encontrada.")
                continue
            pasta_destino = pastas_criadas[destino]

            item_nome = input("Nome do item a adicionar (arquivo ou pasta): ").strip()
            item = None
            if item_nome in pastas_criadas:
                item = pastas_criadas[item_nome]
            elif item_nome in arquivos_criados:
                item = arquivos_criados[item_nome]
            else:
                print("Item não encontrado.")
                continue

            try:
                adicionar_item(pasta_destino, item)
                print(f"Item '{item_nome}' adicionado em '{destino}'.")
            except ValueError as e:
                print(str(e))

        elif escolha == "4":
            print("Impressão pré-ordem:")
            imprimir_pre_ordem(raiz)

        elif escolha == "5":
            print("Impressão pós-ordem:")
            imprimir_pos_ordem(raiz)

        elif escolha == "6":
            nome = input("Nome do arquivo para buscar: ").strip()
            resultado = buscar_arquivo(raiz, nome)
            if resultado:
                print(f"Arquivo encontrado: {resultado}")
            else:
                print("Arquivo não encontrado.")

        elif escolha == "7":
            nome = input("Nome da pasta para buscar: ").strip()
            resultado = buscar_pasta(raiz, nome)
            if resultado:
                print(f"Pasta encontrada: {resultado}")
            else:
                print("Pasta não encontrada.")

        elif escolha == "8":
            print("Árvore de arquivos:")
            imprimir_estrutura(raiz)

        elif escolha == "9":
            nome = input("Nome da pasta para calcular tamanho: ").strip()
            pasta = buscar_pasta(raiz, nome)
            if pasta:
                tamanho = calcular_tamanho(pasta)
                print(f"Tamanho total da pasta '{nome}': {tamanho} KB")
            else:
                print("Pasta não encontrada.")

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
