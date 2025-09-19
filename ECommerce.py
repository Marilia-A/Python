produtos = {}

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos:")
        for codigo, produto in produtos.items():
            print(f"Código: {codigo}, Nome: {produto['nome']}, Descrição: {produto['descricao']}, Valor: R$ {produto['valor']:.2f}")

def cadastrar_produto():
    codigo = int(input("Digite o código do produto: "))
    if codigo in produtos:
        print("Inválido: Código já está em uso.")
        return
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    valor = float(input("Digite o valor do produto: "))
    
    produtos[codigo] = {
        "nome": nome,
        "descricao": descricao,
        "valor": valor
    }
    print("Produto cadastrado com sucesso!")

def alterar_produto():
    codigo = int(input("Digite o código do produto que deseja alterar: "))
    if codigo not in produtos:
        print("Produto não encontrado.")
        return
    
    nome = input("Digite o novo nome do produto (ou pressione Enter para manter): ")
    descricao = input("Digite a nova descrição do produto (ou pressione Enter para manter): ")
    valor_input = input("Digite o novo valor do produto (ou pressione Enter para manter): ")
    
    if nome:
        produtos[codigo]['nome'] = nome
    if descricao:
        produtos[codigo]['descricao'] = descricao
    if valor_input:
        produtos[codigo]['valor'] = float(valor_input)
    
    print("Produto alterado com sucesso!")

def excluir_produto():
    codigo = int(input("Digite o código do produto que deseja excluir: "))
    if codigo in produtos:
        del produtos[codigo]
        print("Produto excluído com sucesso!")
    else:
        print("Erro: Produto não encontrado.")

def menu():
    while True:
        print("\nBem-vindo(a) ao Sistema de E-Commerce \nMenu de opções:")
        print("1 - Listar Produtos")
        print("2 - Cadastrar Produto")
        print("3 - Alterar Produto")
        print("4 - Excluir Produto")
        print("5 - Sair do Programa")
        
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            listar_produtos()
        elif opcao == '2':
            cadastrar_produto()
        elif opcao == '3':
            alterar_produto()
        elif opcao == '4':
            excluir_produto()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Selecione uma das opções disponíveis.")

menu()