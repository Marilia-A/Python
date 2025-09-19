import requests

def buscar_pokemon(nome_ou_numero):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_ou_numero}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

def exibir_perfil(pokemon):
    nome = pokemon['name']
    numero = pokemon['id']
    tipos = [tipo['type']['name'] for tipo in pokemon['types']]
    habilidades = [habilidade['ability']['name'] for habilidade in pokemon['abilities']]
    peso = pokemon['weight'] / 10  
    altura = pokemon['height'] / 10  

    print(f"Nome: {nome.capitalize()}")
    print(f"Número da Pokédex: {numero}")
    print(f"Tipos: {', '.join(tipos)}")
    print(f"Lista de Habilidades: {', '.join(habilidades)}")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")

def comparar_pokemons(pokemon1, pokemon2):
    peso1 = pokemon1['weight'] / 10  #
    peso2 = pokemon2['weight'] / 10  

    print("\nComparação de Atributos:")
    print(f"{pokemon1['name'].capitalize()} vs {pokemon2['name'].capitalize()}")
    print(f"Peso: {peso1} kg vs {peso2} kg")
    print(f"Altura: {pokemon1['height'] / 10} m vs {pokemon2['height'] / 10} m")
    
    if peso1 > peso2:
        print(f"{pokemon1['name'].capitalize()} é mais pesado.")
    elif peso1 < peso2:
        print(f"{pokemon2['name'].capitalize()} é mais pesado.")
    else:
        print("Ambos têm o mesmo peso.")

def main():
    nome_ou_numero = input("Digite o nome ou número de um Pokémon: ").lower()
    pokemon = buscar_pokemon(nome_ou_numero)
    
    if pokemon:
        exibir_perfil(pokemon)
    else:
        print("Pokémon não encontrado.")

    nome_ou_numero1 = input("\nDigite o nome ou número do primeiro Pokémon: ").lower()
    pokemon1 = buscar_pokemon(nome_ou_numero1)
    
    if pokemon1:
        nome_ou_numero2 = input("Digite o nome ou número do segundo Pokémon: ").lower()
        pokemon2 = buscar_pokemon(nome_ou_numero2)
        
        if pokemon2:
            comparar_pokemons(pokemon1, pokemon2)
        else:
            print("Segundo Pokémon não encontrado.")
    else:
        print("Primeiro Pokémon não encontrado.")

if __name__ == "__main__":
    main()
