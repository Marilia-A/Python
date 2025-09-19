import requests
import json

# Lista principal onde os endereços serão armazenados
enderecos_coletados = []

def coletar_ceps():
    print("Iniciando coleta de endereços. Digite os CEPs (ou 'sair' para encerrar):")
    while True:
        cep = input("Digite o CEP (apenas números): ").strip()
        if cep.lower() == "sair":
            break
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. Deve conter exatamente 8 dígitos.")
            continue
        endereco = consultar_cep(cep)
        if endereco:
            enderecos_coletados.append(endereco)
            print("Endereço adicionado com sucesso.")

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado.")
            return None
        return dados
    except Exception as erro:
        print(f"Erro na consulta do CEP: {erro}")
        return None

def menu():
    lista_exibida = enderecos_coletados  # lista exibida no momento

    while True:
        print("\nMENU")
        print("1 - Listar Todos os Endereços")
        print("2 - Filtrar por Cidade")
        print("3 - Listar por Ordem Alfabética de Rua")
        print("4 - Salvar Relatório")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            lista_exibida = enderecos_coletados
            listar_enderecos(lista_exibida)
        elif opcao == "2":
            lista_exibida = filtrar_por_cidade()
        elif opcao == "3":
            lista_exibida = ordenar_por_logradouro()
        elif opcao == "4":
            salvar_relatorio(lista_exibida)
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def listar_enderecos(lista):
    if not lista:
        print("Nenhum endereço para exibir.")
        return
    for i, e in enumerate(lista, start=1):
        print(f"\n[{i}] {e.get('logradouro', '')}, {e.get('bairro', '')}, "
              f"{e.get('localidade', '')} - {e.get('uf', '')} | CEP: {e.get('cep')}")

def filtrar_por_cidade():
    cidade = input("Digite o nome da cidade: ").strip().lower()
    filtrados = [e for e in enderecos_coletados if e.get("localidade", "").lower() == cidade]
    if not filtrados:
        print("Nenhum endereço encontrado para essa cidade.")
    else:
        listar_enderecos(filtrados)
    return filtrados

def ordenar_por_logradouro():
    ordenados = sorted(enderecos_coletados, key=lambda x: x.get("logradouro", "").lower())
    listar_enderecos(ordenados)
    return ordenados

def salvar_relatorio(lista):
    try:
        with open("relatorio_enderecos.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)
        print("Relatório salvo como 'relatorio_enderecos.json'.")
    except Exception as erro:
        print(f"Erro ao salvar o arquivo: {erro}")

# Execução principal
if __name__ == "__main__":
    print("Sistema de Consulta e Gerenciamento de Endereços por CEP")
    coletar_ceps()
    if enderecos_coletados:
        menu()
    else:
        print("Nenhum CEP coletado.")
