capacidade = 5
fila = [None] * capacidade 
primeiro = -1
ultimo = -1
numero_elementos = 0

def is_empty():
    return numero_elementos == 0

def is_full():
    return numero_elementos == capacidade

def first():
    if is_empty():
        print("Fila vazia.")
        return None
    return fila[primeiro]

def last():
    if is_empty():
        print("Fila vazia.")
        return None
    return fila[ultimo]

def enqueue(elemento):
    global ultimo, primeiro, numero_elementos, fila

    print("Enfileirando elemento {}".format(elemento))

    if is_full():
        print("Fila cheia!")
    else:
        if is_empty():
            primeiro = 0
            ultimo = 0
        else:
            ultimo += 1

        fila[ultimo] = elemento
        numero_elementos += 1

def dequeue():
    global primeiro, ultimo, numero_elementos, fila

    if is_empty():
        print("Desenfileirando elemento – Fila vazia")
    else:
        print("Desenfileirando elemento {}".format(fila[primeiro]))
        fila[primeiro] = None
        numero_elementos -= 1

        if is_empty():
            primeiro = -1
            ultimo = -1
        else:
            primeiro += 1

def mostrar_fila():
    print("Fila:", fila)
    print("Índice do primeiro:", primeiro)
    print("Índice do último:", ultimo)
    print("Número de elementos:", numero_elementos)
    print("---")

def menu():
    print("\nMenu:")
    print("1 - Enfileirar elemento")
    print("2 - Desenfileirar")
    print("3 - Verificar quem é o Primeiro da Fila")
    print("4 - Verificar quem é o Último da Fila")
    print("5 - Verificar se a fila está cheia")
    print("6 - Verificar se a fila está vazia")
    print("7 - Mostrar fila")
    print("8 - Sair do programa")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        elemento = input("Digite um elemento para enfileirar: ")
        enqueue(elemento)
    elif opcao == '2':
        dequeue()
    elif opcao == '3':
        elemento_primeiro = first()
        if elemento_primeiro is not None:
            print(f"O primeiro elemento da fila é: {elemento_primeiro}")
    elif opcao == '4':
        elemento_ultimo = last()
        if elemento_ultimo is not None:
            print(f"O último elemento da fila é: {elemento_ultimo}")
    elif opcao == '5':
        if is_full():
            print("A fila está cheia.")
        else:
            print("A fila não está cheia.")
    elif opcao == '6':
        if is_empty():
            print("A fila está vazia.")
        else:
            print("A fila não está vazia.")
    elif opcao == '7':
        mostrar_fila()
    elif opcao == '8':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")