capacidade = 5
pilha = []
topo = -1  

def is_empty():
    if topo == -1:
        return True
    else:
        return False

def is_full():
    if topo == (capacidade - 1):
        return True
    else:
        return False

def push(valor):
    global topo
    if not is_full():
        topo += 1
        pilha.append(valor)
        print(f"{valor} empilhado com sucesso.")
    else:
        print("A pilha está cheia!")

def pop():
    global topo
    if not is_empty():
        valor = pilha[topo]
        pilha.pop()
        topo -= 1
        print(f"{valor} desempilhado com sucesso.")
    else:
        print("A pilha está vazia!")

def top():
    if not is_empty():
        return pilha[topo]
    else:
        print("A pilha está vazia!")
        return None

def remove_all():
    global topo
    pilha.clear()
    topo = -1
    print("Todos os elementos foram removidos da pilha.")

def mostrar():
    if not is_empty():
        print("Elementos na pilha:", pilha)
    else:
        print("A pilha está vazia!")

def menu():
    print("\nMenu:")
    print("1 - Empilhar (Push)")
    print("2 - Desempilhar (Pop)")
    print("3 - Verificar quem está no topo da pilha (Top)")
    print("4 - Verificar se a pilha está cheia (isFull)")
    print("5 - Verificar se a pilha está vazia (isEmpty)")
    print("6 - Remover todos os elementos da pilha (RemoveAll)")
    print("7 - Mostrar pilha")
    print("8 - Sair")
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = int(input("Digite um inteiro para empilhar: "))
        push(valor)
    elif opcao == '2':
        pop()
    elif opcao == '3':
        elemento_topo = top()
        if elemento_topo is not None:
            print(f"O elemento no topo da pilha é: {elemento_topo}")
    elif opcao == '4':
        if is_full():
            print("A pilha está cheia.")
        else:
            print("A pilha não está cheia.")
    elif opcao == '5':
        if is_empty():
            print("A pilha está vazia.")
        else:
            print("A pilha não está vazia.")
    elif opcao == '6':
        remove_all()
    elif opcao == '7':
        mostrar()
    elif opcao == '8':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")