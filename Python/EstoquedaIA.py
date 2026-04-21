print('Sistema de estoque')
loja = []

def cadastro(): #Função do Cadastro
    produto = input('Qual produto deseja cadastrar? ').capitalize()
    id = int(input('Qual é o número de identificação?(ID) '))
    preco_produto = float(input('Qual é o preço do produto? '))
    quant_produtos = int(input('Quantas vezes deseja cadastrar este produto? '))
    estoque = {
        'Nome do Produto' : produto,
        'ID' : id,
        'Preco do Produto' : preco_produto,
        'Quantidade' : quant_produtos
    }
    loja.append(estoque)
    print(f"O produto {produto} foi cadastrado com o id {id}, preço de R${preco_produto} e tendo {quant_produtos} unidades")

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
            for produto_cadastradu in loja:
                # MUDANÇA: Agora busca pelo ID que você cadastrou, não pela posição na lista
                if id_da_busca == produto_cadastradu['ID']:
                    achou = True
                    print(f'\nAchei o ID {id_da_busca}!')
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
            for produto_cadastradu in loja:
                if confirma_id == produto_cadastradu['ID']:
                    achou = True
                    print(f'\nAchei o ID {confirma_id}!')
                    print(f"Nome: {produto_cadastradu['Nome do Produto']}, Preço: {produto_cadastradu['Preco do Produto']}, Estoque Atual: {produto_cadastradu['Quantidade']}\n")
                    
                    confirma_venda = input('Deseja vender este item? ').capitalize()
                    if confirma_venda == 'Sim':
                        quant_item = int(input('Quantos itens deseja vender? '))
                        nome_cliente = input('Qual nome do cliente? ').capitalize()
                        
                        if quant_item <= produto_cadastradu['Quantidade']:
                            # MUDANÇA: Atualizando a quantidade DIRETO na chave do dicionário para salvar na lista
                            produto_cadastradu['Quantidade'] -= quant_item
                            
                            print(f'Vendido o item ID {confirma_id} para {nome_cliente}. Restam {produto_cadastradu["Quantidade"]} itens.')
                            
                            if produto_cadastradu['Quantidade'] == 0:
                                print('AVISO: Estoque zerado! Necessário reabastecer!')
                        else:
                            print('Erro: Falta estoque! Venda não realizada.')
                    break # Para o loop após processar o produto encontrado
            
            # MUDANÇA: O "if not achou" deve ficar FORA do loop 'for' para não repetir erro a cada volta
            if not achou:
                print("Erro! Produto com este ID não foi encontrado.")
                
        except ValueError:
            print('Erro: Digite apenas números inteiros no ID e quantidade!')

while True:
    escolha = input("\n(Escolha em números)\n1- Cadastrar\n2- Ver produtos\n3- Buscar\n4- Vendas\n5- Sair\n")
    if escolha == '1':
        cadastro()
    elif escolha == '2':
        consulta()
    elif escolha == '3':
        busca()
    elif escolha == '4':
        vendas()
    elif escolha == '5':
        print('Saindo do sistema...')
        break
