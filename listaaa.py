def gravar_lista(lista):
    gravar_arq = input("Digite o nome do arquivo: ")
    with open(gravar_arq, "w") as arquivo: 
        for item in lista:
            for item in lista:
            arquivo.write(item + "\n")
        print("Gravado", gravar_arq)
        def ordenar_lista():


def minha_lista():
    lista = []     
    while True:
        print("Escolha uma opção:")
        print("1. Inserir um novo item na lista")
        print("2. Eliminar um item específico da lista")
        print("3. Mostrar a lista atual")
        print("4. Eliminar ")  
        
        escolha = input("Digite o número da opção que você deseja: ")

        if escolha == "1":
            item = input("Digite o novo item da lista: ")
            lista.append(item)
            print(f"{item} foi adicionado à lista.")
        elif escolha == "2":
            item = input("Digite o item a ser eliminado.")
            if item in lista:
                lista.remove(item)
                print(f"{item} foi eliminado da lista")
            else:
                print(f"{item} não está na lista.")
        elif escolha == "3":
            print("Lista atual:")
            for item in lista:
                print(item)
        elif escolha == "4":
            print("finalizado.")
            break
        else:
            print("Opção incorreta. Tente novamente.")
            
if __name__ == "__main__":
    minha_lista()
