tarefas = []


def menu():
    # Exibe o menu de opções para o usuário
    print("\n=== Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")


def adicionar():
    # Adiciona uma nova tarefa na lista
    tarefa = input("Digite a tarefa: ")
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print("Tarefa adicionada!")


def listar():
    # Lista todas as tarefas cadastradas
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, t in enumerate(tarefas):
        # Mostra status ✔ concluído ou ✖ pendente
        status = "✔" if t["concluida"] else "✖"
        print(f"{i} - {t['tarefa']} ({status})")


def concluir():
    # Marca uma tarefa como concluída
    listar()
    indice = int(input("Número da tarefa para concluir: "))

    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")


def remover():
    # Remove uma tarefa da lista
    listar()
    indice = int(input("Número da tarefa para remover: "))

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida!")
    else:
        print("Índice inválido.")


# Loop principal do programa
while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        concluir()
    elif opcao == "4":
        remover()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
