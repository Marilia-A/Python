evento_tecnico = set()
evento_cultural = set()

while True:
    print("=== Menu de Consulta de Participação ===")
    print("1 - Inserir participantes do Evento Técnico")
    print("2 - Inserir participantes do Evento Cultural")
    print("3 - Remover participante de um evento")
    print("4 - Mostrar funcionários que participaram dos DOIS eventos")
    print("5 - Mostrar funcionários que participaram de APENAS UM evento")
    print("6 - Consultar se um funcionário participou (e de quais eventos)")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        qtd = int(input("Quantos participantes deseja adicionar ao Evento Técnico? "))
        for _ in range(qtd):
            nome = input("Digite o nome: ").strip()
            evento_tecnico.add(nome)

    elif opcao == "2":
        qtd = int(input("Quantos participantes deseja adicionar ao Evento Cultural? "))
        for _ in range(qtd):
            nome = input("Digite o nome: ").strip()
            evento_cultural.add(nome)

    elif opcao == "3":
        evento = input("Remover de qual evento? (Técnico/Cultural): ").strip().lower()
        nome = input("Digite o nome: ").strip()
        if evento in ["técnico", "tecnico"]:
            evento_tecnico.discard(nome)
        elif evento == "cultural":
            evento_cultural.discard(nome)
        else:
            print("Evento inválido.")

    elif opcao == "4":
        ambos = evento_tecnico & evento_cultural
        print("Participaram dos DOIS eventos:", ", ".join(ambos) if ambos else "Nenhum.")

    elif opcao == "5":
        apenas_um = evento_tecnico ^ evento_cultural
        print("Participaram de APENAS UM evento:", ", ".join(apenas_um) if apenas_um else "Nenhum.")

    elif opcao == "6":
        nome = input("Digite o nome: ").strip()
        t = nome in evento_tecnico
        c = nome in evento_cultural
        if t and c:
            print(f"{nome} participou dos dois eventos.")
        elif t:
            print(f"{nome} participou apenas do Evento Técnico.")
        elif c:
            print(f"{nome} participou apenas do Evento Cultural.")
        else:
            print(f"{nome} não participou de nenhum evento.")

    elif opcao == "7":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Insira uma opção válida.")

    print() 
