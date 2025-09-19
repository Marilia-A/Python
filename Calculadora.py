while True:
    def calcular_expressao(expressao):
        expressao = expressao.replace(" ", "")  

        for operador in ['+', '-', '*', '/']:
            if operador in expressao:
                partes = expressao.split(operador)  
                if len(partes) == 2:
                    try:
                        num1, num2 = int(partes[0]), int(partes[1])
                        if operador == '+':
                            return f"{num1} {operador} {num2} = {num1 + num2}"
                        
                        elif operador == '-':
                            return f"{num1} {operador} {num2} = {num1 - num2}"
                        
                        elif operador == '*':
                            return f"{num1} {operador} {num2} = {num1 * num2}"
                        
                        elif operador == '/':
                            if num2 == 0:
                                return f"Erro: Divisão por Zero em {expressao}"
                            return f"{num1} {operador} {num2} = {num1 / num2}"
                        
                    except ValueError:
                        return f"Expressão Inválida: {expressao}"
        return f"Expressão Inválida: {expressao}"

    entrada = input("Digite uma ou mais expressões matemáticas (Separadas por Vírgula): ")
    
    for expressao in entrada.split(','):
        print(calcular_expressao(expressao))
    
    continuar = input("Deseja realizar outro cálculo? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o Programa.")
        break