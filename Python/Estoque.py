#Sistema de estoque
print('Sistema de estoque')
loja = []

def cadastro(): #Função do Cadastro
    produtinho = input('Qual produto deseja cadastrar? ').capitalize()
    id = int(input('Qual é o número de identificação?(ID) '))
    preco_produto = float(input('Qual é o preço do produto? '))
    quant_produtos = int(input('Quantas vezes deseja cadastrar este produto? '))
    estoque = {
        'Nome do Produto' : produtinho,
        'ID' : id,
        'Preco do Produto' : preco_produto,
        'Quantidade' : quant_produtos
    }
    loja.append(estoque)
    print(f"O produto {produtinho} foi cadastrado com o id {id}, preço de R${preco_produto} e tendo {quant_produtos} unidades")

def consulta(): #Função de Ver os Produtos Cadastrados
    confirmar = input('Realmente deseja consultar os produtos cadastros?\n ').capitalize()
    if confirmar == 'Sim':
        if len(loja) == 0:
            print('Erro! Nenhum produto cadastrado até agora!\n')
        else:
            print(f"\n---Total de {len(loja)} produto(s) foram cadastrado(s)---")
            for produto_cadastrado in loja:
                print(f"Nome: {produto_cadastrado['Nome do Produto']}, ID: {produto_cadastrado['ID']} ,Preço: {produto_cadastrado['Preco do Produto']}, Quantidade: {produto_cadastrado['Quantidade']}")
            print('-------------------------------------------\n')

def busca(): # Função que busca os produtos pelo ID
    confirmar_busca = input('\nDeseja realmente buscar por ID? ').capitalize()
    if confirmar_busca == 'Sim':
        try:
            id_da_busca = int(input('Digite o ID do produto: '))
            achou = False
            for indice, produto_cadastradu in enumerate(loja):
                if id_da_busca == indice + 1:
                    achou = True
                    print(f'\nAchei o ID {indice + 1}!')
                    print(f"Nome: {produto_cadastradu['Nome do Produto']}, Preço: {produto_cadastradu['Preco do Produto']}, Quantidade: {produto_cadastradu['Quantidade']}\n")
                    break
            
            if not achou:
                print('ID não encontrado no sistema!\n')
        except ValueError:
            print("Erro: Por favor, digite um número inteiro para o ID.")

def vendas():
    confirma = input('Deseja realmente abrir o sistema de vendas? ').capitalize()
    if confirma == 'Sim':
        try:
            confirma_id = int(input('Qual é o id que buscas? '))
            achou = False
            for indice, produto_cadastradu in enumerate(loja):
                if confirma_id == produto_cadastradu['ID']:
                    achou = True
                    print(f'\nAchei o ID {indice + 1}!')
                    print(f"Nome: {produto_cadastradu['Nome do Produto']}, Preço: {produto_cadastradu['Preco do Produto']}, Quantidade: {produto_cadastradu['Quantidade']}\n")
                    confirma_venda = input('Deseja vender este item? ').capitalize()
                    if confirma_venda == 'Sim':
                        quant_item = int(input('Quantos itens deseja vender? '))
                        nome_cliente = input('Qual nome do cliente? ').capitalize()
                        if quant_item <= produto_cadastradu['Quantidade']:
                            restante = produto_cadastradu['Quantidade'] - quant_item
                            print(f'Vendido o item do ID {confirma_id}, para o cliente {nome_cliente}. Sobrando no estoque {restante} itens.')
                            produto_cadastradu['Quantidade'] = restante
                            if restante == 0:
                                print('\nNecessário reabastecer!\n')
                                break
                            else:
                                break
                        else:
                            print('Falta estoque! Não é possível venda!')
                            break             
                if not achou:
                    print("Erro! Não encontrado item")
        except ValueError:
            print('Digite um número válido, por favor!')

while True:
    escolha = int(input("(Escolha em números)\n" \
    "1- Cadastrar produto\n2- Ver produtos\n3- Buscar produtos\n4- Vendas\n5- Sair\n"
    ""))
    if escolha == 1:
        cadastro()
    if escolha == 2:
        consulta()
    if escolha == 3:
        busca()
    if escolha == 4:
        vendas()
    if escolha == 5:
        print('Ok!\n')
        break