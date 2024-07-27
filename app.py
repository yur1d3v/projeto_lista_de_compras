import os

# Lista de compras armazenará dicionários com ID e nome do produto
lista_de_compras = []
proximo_id = 1  # Inicializa o próximo ID disponível

def limpar_tela():
    """
    Limpa a tela do terminal.
    Funciona apenas em sistemas operacionais que suportam o comando 'cls'.
    """
    os.system('cls')

def menu_principal():
    """
    Exibe o menu principal e lida com a navegação entre as opções.
    As opções incluem adicionar, remover, pesquisar e listar produtos.
    Também permite ao usuário sair do programa.
    """
    global proximo_id
    while True:
        print('\nLista de Compras Simples')
        print()
        print('1 - Adicionar produto')
        print('2 - Remover produto')
        print('3 - Pesquisar produtos')
        print('4 - Listar Produtos')
        print('s - Sair do programa')
        opcao = input('Escolha uma opção ou "s" para sair do programa: ')

        if opcao == 's' or opcao == 'S':
            print('\nObrigado por utilizar a Lista de Compras Simples!')
            break

        if opcao not in ['1', '2', '3', '4']:
            print('\nOpção inválida! Tente novamente!')
            continue

        if opcao == '1':
            produto = input('Digite o produto que deseja adicionar à lista: ')
            adicionar_produto(produto)
        elif opcao == '2':
            try:
                id_produto = int(input('Digite o ID do produto que deseja remover da lista: '))
                remover_produto(id_produto)
            except ValueError:
                print('ID inválido! Tente novamente.')
        elif opcao == '3':
            nome_produto = input('Digite o nome ou parte do nome do produto que deseja pesquisar: ')
            pesquisar_produto(nome_produto)
        elif opcao == '4':
            limpar_tela()
            listar_produtos()

def adicionar_produto(produto):
    """
    Adiciona um produto à lista de compras.

    Parâmetros:
    - produto (str): O nome do produto a ser adicionado.
    """
    global proximo_id
    limpar_tela()
    lista_de_compras.append({'id': proximo_id, 'nome': produto})
    print(f'O produto {produto} foi adicionado com sucesso com o ID {proximo_id}!')
    proximo_id += 1

def remover_produto(id_produto):
    """
    Remove um produto da lista de compras pelo seu ID.

    Parâmetros:
    - id_produto (int): O ID do produto a ser removido.
    """
    global lista_de_compras
    limpar_tela()
    for produto in lista_de_compras:
        if produto['id'] == id_produto:
            lista_de_compras.remove(produto)
            print(f'O produto {produto["nome"]} (ID {id_produto}) foi removido com sucesso!')
            return
    print(f'O produto com ID {id_produto} não está na lista!')

def pesquisar_produto(nome_produto):
    """
    Pesquisa produtos na lista de compras pelo nome ou parte do nome.

    Parâmetros:
    - nome_produto (str): O nome ou parte do nome do produto a ser pesquisado.
    """
    limpar_tela()
    resultados = [produto for produto in lista_de_compras if nome_produto.lower() in produto['nome'].lower()]
    if resultados:
        print(f'Produtos encontrados contendo "{nome_produto}":')
        for produto in resultados:
            print(f'ID: {produto["id"]}, Nome: {produto["nome"]}')
        print(f'Total de produtos encontrados: {len(resultados)}')
    else:
        print(f'Nenhum produto encontrado contendo "{nome_produto}".')

def listar_produtos():
    """
    Lista todos os produtos na lista de compras.
    """
    limpar_tela()
    if not lista_de_compras:
        print('Sua lista de compras está vazia!')
    else:
        print('Lista de produtos:')
        for produto in lista_de_compras:
            print(f'ID: {produto["id"]}, Nome: {produto["nome"]}')

if __name__ == '__main__':
    menu_principal()
