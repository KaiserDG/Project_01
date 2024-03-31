produtos = {}
done = False
while not done:
    print('Olá, oque gostaria de fazer?\n')
    print('1. Adicionar um produto ao inventário')
    print('2. Remover um produto do inventário')
    print('3. Modificar o valor de um produto no inventário')
    print('4. Modificar a quantidade do produto no inventário')
    print('5. Listar produtos no inventário')
    print('6. Sair')
    choice = (input(''))
    print(f'Você selecionou a opção número: {choice}')
    
    if choice == '1':
        nome_produto = input('Informe o nome do produto: ')
        preco_produto = (input('Informe o valor do produto: '))
        quantidade_produto = input('Informe a quantidade do produto no estoque: ')
        produtos[nome_produto] = {'name': (nome_produto), 'preco': (preco_produto), 'quantidade': (quantidade_produto)}
        print('produto adicionado')
        pass
    
    elif choice =='2':
        print_produtos()
        produto_num = int(input('Infomre o número do produto para ser retirado: '))
        if produto_num<= len(produtos):
            nome_produto = list(produtos.keys())[produto_num-1]
            del produtos[nome_produto]
            print('Produto removido com sucesso')
        else:
            print('Número inválido')
            pass
    
    elif choice == '3':
        print_produtos()
        produto_num = int(input('Informe o número do produto a ter o preço alterado: '))
        if produto_num<= len(produtos):
            nome_produto = list(produtos.keys())[produto_num-1]    
            novo_preco_produto = (input('Informe o novo valor do produto: '))
            preco_produto = novo_preco_produto
            produtos[nome_produto] = {'name': (nome_produto), 'preco': (preco_produto), 'quantidade': (quantidade_produto)}
            print('Novo valor adicionado')
        else:
            print('Número inválido')
            pass
    
    elif choice == '4':
        print_produtos()
        produtos_num = int(input('Informe o número do produto a ter a quantidade alterada: '))
        if produto_num<= len(produtos):
            nome_produto = list(produtos.keys())[produto_num-1]
            nova_quantidade_produto = input('Informe a nova quantidade do produto: ')
            quantidade_produto = nova_quantidade_produto
            produtos[nome_produto] = {'name': (nome_produto), 'preco': (preco_produto), 'quantidade': (quantidade_produto)}
            print('Nova quantidade adicionada')
        else:
            print('Número inválido')
            pass
    
    elif choice == '5':
        print_produtos()
    
    elif choice == '6':
        done = True
        print('Até logo')
    else:
        print('Opção inválida')
        
            
    # Função para listar os produtos
    def print_produtos():
        print("Produtos listados:")
        for i, produto in enumerate(produtos.values()):
            print(f'{i+1}. Nome: {produto['name']} $: {produto['preco']} Quantidade: {produto['quantidade']}')
            
        
    
    
    
    
    
    
    
    
    
    

