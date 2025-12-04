produtos = []


def menu():
    # Exibe o menu principal do sistema
    print("\n=== Sistema de Cadastro de Produtos ===")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Atualizar produto")
    print("4. Excluir produto")
    print("5. Sair")


def cadastrar():
    # Coleta o nome e o preço do produto informado pelo usuário
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))

    # Armazena as informações em um dicionário
    produto = {"nome": nome, "preco": preco}

    # Adiciona o produto à lista geral
    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


def listar():
    # Verifica se a lista está vazia
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    # Mostra todos os produtos com seus índices
    for i, p in enumerate(produtos):
        print(f"{i} - {p['nome']} - R$ {p['preco']:.2f}")


def atualizar():
    # Mostra os produtos disponíveis
    listar()

    # Solicita o índice do produto a ser atualizado
    indice = int(input("Digite o índice do produto para atualizar: "))

    # Valida o índice informado
    if 0 <= indice < len(produtos):
        nome = input("Novo nome: ")
        preco = float(input("Novo preço: "))

        # Atualiza as informações do produto
        produtos[indice]["nome"] = nome
        produtos[indice]["preco"] = preco

        print("Produto atualizado!")
    else:
        print("Índice inválido.")


def excluir():
    # Exibe os produtos disponíveis
    listar()

    # Solicita o índice do produto para exclusão
    indice = int(input("Digite o índice do produto para excluir: "))

    # Valida o índice informado
    if 0 <= indice < len(produtos):
        produtos.pop(indice)
        print("Produto excluído!")
    else:
        print("Índice inválido.")


# Loop principal do sistema
while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
