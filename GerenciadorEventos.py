import json
banco_de_dados = []

def coletar_dados_usuario():
    print("=== Formulário de Inscrição para Evento Online ===")
    nome = input("Digite seu nome (mínimo 3 letras): ").strip()
    email = input("Digite seu email (deve conter '@' e terminar com '.com'): ").strip()
    idade_str = input("Digite sua idade (maior ou igual a 16): ").strip()
    interesse = input("Digite seu interesse (Programação, Design, Marketing): ").strip()

    try:
        idade = int(idade_str)
    except ValueError:
        idade = -1  

    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade,
        "interesse": interesse
    }

    return json.dumps(usuario)

def processar_inscricao(dados_json):
    try:
        dados = json.loads(dados_json)
    except json.JSONDecodeError:
        return {
            "status": "erro",
            "mensagem": "Erro: dados inválidos recebidos."
        }

    nome = dados.get("nome", "").strip()
    email = dados.get("email", "").strip()
    idade = dados.get("idade")
    interesse = dados.get("interesse", "").strip()

    if len(nome) < 3:
        return {"status": "erro", "mensagem": "Erro: nome deve ter pelo menos 3 caracteres."}
    
    if "@" not in email or not email.endswith(".com"):
        return {"status": "erro", "mensagem": "Erro: email inválido."}
    
    if not isinstance(idade, int) or idade < 16:
        return {"status": "erro", "mensagem": "Erro: idade mínima não atingida."}
    
    if interesse not in ["Programação", "Design", "Marketing"]:
        return {"status": "erro", "mensagem": "Erro: interesse inválido."}

    banco_de_dados.append({
        "nome": nome,
        "email": email,
        "idade": idade,
        "interesse": interesse
    })

    return {"status": "sucesso", "mensagem": "Inscrição realizada com sucesso!"}

def exibir_resposta(resposta):
    print("\n=== Resposta do Servidor ===")
    print(f"Status: {resposta['status']}")
    print(f"Mensagem: {resposta['mensagem']}")

def main():
    dados_usuario_json = coletar_dados_usuario()
    resposta = processar_inscricao(dados_usuario_json)
    exibir_resposta(resposta)

main()
