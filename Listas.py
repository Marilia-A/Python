compras = []
while True:
    print('\nEscolha uma opção:')
    print('1 - Adicionar um novo item à lista')
    print('2 - Remover um item da lista')
    print('3 - Verificar se um item está ou não na lista')
    print('4 - Mostrar o primeiro item da lista')
    print('5 - Mostrar o último item da lista')
    print('6 - Mostrar os três primeiros e os três últimos itens da lista')
    print('7 - Colocar todos os itens em letras maiúsculas')
    print('8 - Colocar todos os itens em letras minúsculas')
    print('9 - Mostrar a quantidade de itens na lista')
    print('10 - Sair')

    opcao = input('\nDigite o número da opção desejada: ')
    if opcao == '1':
        item = input('Digite o item que deseja adicionar: ')
        compras.append(item)
        print(f"Item '{item}' adicionado à lista.")

    elif opcao == '2':
        item = input('\nDigite o item que deseja remover: ')
        if item in compras:
            compras.remove(item)
            print(f"Item '{item}' removido da lista.")
        else:
            print(f"Item '{item}' não encontrado na lista.")

    elif opcao == '3':
        item = input('\nDigite o item que deseja verificar: ')
        if item in compras:
            print(f"Item '{item}' está na lista.")
        else:
            print(f"Item '{item}' não está na lista.")

    elif opcao == '4':
        if compras:
            print(f'O primeiro item da lista é: {compras[0]}')
        else:
            print('A lista está vazia.')

    elif opcao == '5':
        if compras:
            print(f'O último item da lista é: {compras[-1]}')
        else:
            print('A lista está vazia.')

    elif opcao == '6':
        print('Três primeiros itens:', compras[:3])
        print('Três últimos itens:', compras[-3:])

    elif opcao == '7':
        compras = [item.upper() for item in compras]
        print('Todos os itens estão letras maiúsculas.')

    elif opcao == '8':
        compras = [item.lower() for item in compras]
        print('Todos os itens estão letras minúsculas.')

    elif opcao == '9':
        print(f'A quantidade de itens na lista é: {len(compras)}')

    elif opcao == '10':
        print('Programa encerrado..')
        break

    else:
        print('Opção inexistente. Escolha uma das opções de 1 a 10.')