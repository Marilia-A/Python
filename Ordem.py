import random

with open("dados_desordenados.txt", "w") as f:
    for _ in range(1000000):
        f.write(f"{random.randint(1, 1000000)}\n")

import time
import bisect

# Algoritmos de ordenação
def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Funções auxiliares
def carregar_dados():
    with open("dados_desordenados.txt") as f:
        return [int(line.strip()) for line in f.readlines()]

def medir_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

def buscar_elemento(lista, valor):
    return valor in lista 

def busca_binaria(lista, valor):
    idx = bisect.bisect_left(lista, valor)
    return idx < len(lista) and lista[idx] == valor

def inserir_ordenado(lista, valor):
    bisect.insort(lista, valor)

def excluir_ordenado(lista, valor):
    idx = bisect.bisect_left(lista, valor)
    if idx < len(lista) and lista[idx] == valor:
        lista.pop(idx)
        return True
    return False

# Interface principal
def menu():
    desordenada = carregar_dados()
    ordenada = []
    ordenada_status = False

    while True:
        print("\n--- Laboratório de Performance de Algoritmos ---")
        print(f"Status: {len(desordenada)} itens carregados")
        print("\n[ Menu Principal ]")
        print("1. Ordenar a lista")
        print("2. Realizar operação na lista DESORDENADA")
        print("3. Realizar operação na lista ORDENADA")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Escolha o Algoritmo de Ordenação ---")
            print("1. Bubble Sort")
            print("2. Selection Sort")
            print("3. Insertion Sort")
            print("4. Merge Sort")
            print("5. Quick Sort")
            print("6. Timsort (Python sort())")
            print("7. Voltar")
            metodo = input("Escolha o algoritmo: ")
            print("Ordenando...")

            algoritmos = {
                "1": bubble_sort,
                "2": selection_sort,
                "3": insertion_sort,
                "4": merge_sort,
                "5": quick_sort,
                "6": sorted
            }

            if metodo in algoritmos:
                ordenada, tempo = medir_tempo(algoritmos[metodo], desordenada)
                ordenada_status = True
                print(f"Pronto! Tempo gasto: {tempo:.6f} segundos.")
            elif metodo == "7":
                continue
            else:
                print("Opção inválida.")

        elif opcao == "2":
            print("\nOperação na Lista DESORDENADA")
            print("a. Buscar um elemento")
            print("b. Inserir um elemento")
            print("c. Excluir um elemento")
            print("d. Voltar ao menu principal")
            sub = input("Escolha a operação: ").lower()

            if sub == "a":
                num = int(input("Digite o número para BUSCAR: "))
                print("Buscando...")
                _, tempo = medir_tempo(buscar_elemento, desordenada, num)
                encontrado = buscar_elemento(desordenada, num)
                print(f"Elemento {'encontrado' if encontrado else 'não encontrado'}! Tempo: {tempo:.6f} segundos.")

            elif sub == "b":
                num = int(input("Digite o número para INSERIR: "))
                _, tempo = medir_tempo(desordenada.append, num)
                print(f"Inserido! Tempo: {tempo:.6f} segundos.")

            elif sub == "c":
                num = int(input("Digite o número para EXCLUIR: "))
                print("Removendo...")
                if num in desordenada:
                    _, tempo = medir_tempo(desordenada.remove, num)
                    print(f"Removido! Tempo: {tempo:.6f} segundos.")
                else:
                    print("Elemento não encontrado.")

        elif opcao == "3":
            if not ordenada_status:
                print("Lista ainda não foi ordenada.")
                continue

            print("\nOperação na Lista ORDENADA")
            print("a. Buscar um elemento (binária)")
            print("b. Inserir um elemento (mantendo a ordem)")
            print("c. Excluir um elemento (mantendo a ordem)")
            print("d. Voltar ao menu principal")
            sub = input("Escolha a operação: ").lower()

            if sub == "a":
                num = int(input("Digite o número para BUSCAR: "))
                print("Buscando com busca binária...")
                _, tempo = medir_tempo(busca_binaria, ordenada, num)
                encontrado = busca_binaria(ordenada, num)
                print(f"Elemento {'encontrado' if encontrado else 'não encontrado'}! Tempo: {tempo:.6f} segundos.")

            elif sub == "b":
                num = int(input("Digite o número para INSERIR: "))
                _, tempo = medir_tempo(inserir_ordenado, ordenada, num)
                print(f"Inserido mantendo a ordem! Tempo: {tempo:.6f} segundos.")

            elif sub == "c":
                num = int(input("Digite o número para EXCLUIR: "))
                print("Removendo mantendo a ordem...")
                _, tempo = medir_tempo(excluir_ordenado, ordenada, num)
                print(f"Elemento {'removido' if excluir_ordenado(ordenada, num) else 'não encontrado'}! Tempo: {tempo:.6f} segundos.")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar
if __name__ == "__main__":
    menu()
