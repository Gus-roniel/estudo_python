import os

lista_compras = []
inserir = "i"
delete = "d"
listar = "l"
while True:
    opcao = input('Escolha uma opção:\n[i]nserir [d]eletar [l]istar ')

    if inserir in opcao:
        os.system('cls')
        item_adicionado = input("Qual item deseja adicionar? ")
        lista_compras.append(item_adicionado)
        print(lista_compras)

    if listar in opcao:
        os.system('cls')
        for indice, nome in enumerate(lista_compras):
            print(indice, nome)

    if delete in opcao:
        os.system('cls')
        item_deletado = input('Qual item deseja deletar? ')
        del lista_compras[int(item_deletado)]
        print(lista_compras)
