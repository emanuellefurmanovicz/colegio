def adicionar_item(lista):
    novo_item = input("Digite uma fruta: ")
    lista.append(novo_item)
    print("Fruta adicionada com sucesso!")
    mostrar_lista(lista)

def excluir_item(lista):
    item_excluir = input("Digite a fruta você que deseja excluir: ")
    if item_excluir in lista:
        lista.remove(item_excluir)
        print("Fruta excluída com sucesso!")
    else:
        print("O item não está na lista.")
    mostrar_lista(lista)

def gravar_lista(lista):
    nome_arq = input("Digite o nome do arquivo")
    with open(nome_arq, "w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")
    print("Aquivo gravado com sucesso", nome_arq)

def ordenar_lista(lista):
    lista.sort(reverse = True)
    print("Lista ordenada com sucesso")

def carregar_lista(lista):
    nome_arq = input("Digite o nome do arquivo que deseja carregar")
    nome_arquivo += ".txt"
    try:
        with open(nome_arq, "r") as arquivo:
            lista.clear()
            for linha in arquivo:
                lista.append(linha.strip())
        print("Lista carregada com sucesso", nome_arq)

    except FileNotFoundError:
        print("Arquivo não encontrado")

    except Exception as e:
        print("Ocorreu um erro", e)

def listar_arquivo(lista):
    diretorios = os.getcwd()
    arquivos = os.listdir(diretorios)

    for lista_arquivo in arquivos:
        print(lista_arquivo)

def main():
    lista = []
    continuar = True

    while continuar:
        print("Escolha uma opção:")
        print("1. Adicionar uma fruta à lista")
        print("2. Excluir uma fruta da lista")
        print("3. Mostrar lista atual")
        print("4. Gravar lista")
        print("5. Carregar lista")
        print("6. Ordenar lista")
        print("7. Listar arquivo")
        print("8. Sair do programa")

        opcao = input("Opção: ")

        if opcao == '1':
            adicionar_item(lista)
        elif opcao == '2':
            excluir_item(lista)
        elif opcao == '3':
            mostrar_lista(lista)
        elif opcao == '4':
            gravar_lista(lista)
        elif opcao == '5':
            carregar_lista(lista)
        elif opcao == '6':
            ordenar_lista(lista)
        elif opcao == '7':
            listar_arquivo(lista)
        elif opcao == '8':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    main()
  
