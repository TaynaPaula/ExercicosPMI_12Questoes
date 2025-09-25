#Desenvolva um sistema de controle de estoque usando listas e tuplas com operações
#CRUD [Create (Criar), Read (Ler), Update (Atualizar) e Delete (Apagar)]
lista = ["maça", "banana", "abobora"]

while True:
    acao = input("Deseja: Adicionar produto, remover, alterar ou 'sair' para terminar: ").lower()

    if acao == 'sair':
        break

    elif acao == 'adicionar':
        elemento = input("Digite o produto para adicionar: ")
        if elemento in lista:
            print(f"Elemento '{elemento}' já existe na lista.")
        else:
            lista.append(elemento)
            print(f"Elemento '{elemento}' adicionado.")

    elif acao == 'remover':
        elemento = input("Digite o produto para remover: ")
        if elemento in lista:
            lista.remove(elemento)
            print(f"Elemento '{elemento}' removido.")
        else:
            print(f"Elemento '{elemento}' não está na lista.")

    elif acao == 'alterar':
        antigo = input("Digite o produto que deseja alterar: ")
        if antigo in lista:
            novo = input("Digite o novo nome do produto: ")
            index = lista.index(antigo)
            lista[index] = novo
            print(f"Elemento '{antigo}' alterado para '{novo}'.")
        else:
            print(f"Elemento '{antigo}' não está na lista.")

    else:
        print("Opção inválida. Por favor, tente novamente.")

    print(f"Lista atual: {lista}")