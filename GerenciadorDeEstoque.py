def criar_bst(codigo, quantidade):
    return {
        'codigo': codigo,
        'quantidade': quantidade,
        'esquerda': None,
        'direita': None
    }

def inserir_produto(raiz, codigo, quantidade):
    if raiz is None:
        return criar_bst(codigo, quantidade)
    elif codigo < raiz['codigo']:
        raiz['esquerda'] = inserir_produto(raiz['esquerda'], codigo, quantidade)
    elif codigo > raiz['codigo']:
        raiz['direita'] = inserir_produto(raiz['direita'], codigo, quantidade)
    else:
        raiz['quantidade'] += quantidade
    return raiz

def buscar_produto(raiz, codigo):
    if raiz is None:
        return None
    elif codigo == raiz['codigo']:
        return raiz['quantidade']
    elif codigo < raiz['codigo']:
        return buscar_produto(raiz['esquerda'], codigo)
    else:
        return buscar_produto(raiz['direita'], codigo)

def exibir_estoque_ordem(raiz):
    if raiz is not None:
        exibir_estoque_ordem(raiz['esquerda'])
        print(f"Código: {raiz['codigo']}, Quantidade: {raiz['quantidade']}")
        exibir_estoque_ordem(raiz['direita'])

def exibir_menu():
    print("\n--- Gerenciador de Estoque ---")
    print("1. Adicionar/Atualizar Produto")
    print("2. Buscar Produto")
    print("3. Exibir Estoque Completo")
    print("4. Sair")

def main():
    raiz_bst = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                codigo = int(input("Digite o código do produto: "))
                quantidade = int(input("Digite a quantidade: "))
                raiz_bst = inserir_produto(raiz_bst, codigo, quantidade)
                print("Produto adicionado/atualizado com sucesso!")
            except ValueError:
                print("Erro: Código e quantidade devem ser números inteiros.")
        
        elif opcao == '2':
            try:
                codigo = int(input("Digite o código do produto a buscar: "))
                resultado = buscar_produto(raiz_bst, codigo)
                if resultado is not None:
                    print(f"Produto encontrado! Quantidade em estoque: {resultado}")
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("Erro: Código deve ser um número inteiro.")
        
        elif opcao == '3':
            if raiz_bst is None:
                print("Estoque vazio.")
            else:
                print("\n--- Estoque Atual ---")
                exibir_estoque_ordem(raiz_bst)
        
        elif opcao == '4':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()