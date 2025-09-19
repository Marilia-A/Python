def criar_no(valor):
    return {"valor": valor, "proximo": None}

def inserir_fim(lista, valor):
    novo = criar_no(valor)
    if not lista:
        return novo
    atual = lista
    while atual["proximo"]:
        atual = atual["proximo"]
    atual["proximo"] = novo
    return lista

def buscar(lista, valor):
    atual = lista
    while atual:
        if atual["valor"]["url"] == valor:
            return atual
        atual = atual["proximo"]
    return None

def remover(lista, valor):
    if not lista:
        return None
    if lista["valor"]["url"] == valor:
        return lista["proximo"]
    anterior = lista
    atual = lista["proximo"]
    while atual:
        if atual["valor"]["url"] == valor:
            anterior["proximo"] = atual["proximo"]
            return lista
        anterior = atual
        atual = atual["proximo"]
    return lista

def imprimir(lista):
    atual = lista
    if not atual:
        print("Histórico vazio.")
        return
    print("Histórico de navegação:")
    while atual:
        valor = atual["valor"]
        print(f"{valor['horario']} - {valor['url']}")
        atual = atual["proximo"]

historico = None
while True:
    print("\n=== Menu de Histórico de Navegação ===")
    print("1 - Acessar novo site")
    print("2 - Ver histórico completo")
    print("3 - Remover um site do histórico")
    print("4 - Limpar todo o histórico")
    print("5 - Buscar um site pelo endereço")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        url = input("Digite a URL do site: ").strip()
        horario = input("Digite o horário da visita (ex: 14:30): ").strip()
        site = {"url": url, "horario": horario}
        historico = inserir_fim(historico, site)

    elif opcao == "2":
        imprimir(historico)

    elif opcao == "3":
        url = input("Digite a URL do site a ser removido: ").strip()
        historico = remover(historico, url)
        print("Se o site existia, foi removido.")

    elif opcao == "4":
        historico = None
        print("Histórico limpo.")

    elif opcao == "5":
        url = input("Digite a URL para busca: ").strip()
        resultado = buscar(historico, url)
        if resultado:
            print(f"Site encontrado: {resultado['valor']['horario']} - {resultado['valor']['url']}")
        else:
            print("Site não encontrado.")

    elif opcao == "6":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
