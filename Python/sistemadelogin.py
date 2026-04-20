erros = 0
login = ""
senha = ""

while True:
    criar_conta = input('Deseja criar uma conta? ')
    if criar_conta == "não" or criar_conta == "Não" or criar_conta == "nao" or criar_conta == "Nao":
        print("Ok, colega. Saindo do sistema...")
        exit()
    if criar_conta == "sim" or criar_conta == "Sim":
            cria_login = input('Qual login você deseja? ')
            cria_senha = input('E qual senha deseja? ')
            login = cria_login
            senha = cria_senha
            break
    
while True:
    print("\nHora do login \n")
    login_certo = input("Login: ")
    senha_certa = input("Senha: ")
    if login_certo == login:
        if senha_certa == senha:
            print("Bem vindo ao sistema,", login)
            escolha = input('1. Mensagem ou 2. Sair: ')
            if escolha ==  "1":
                print("Jesus loves you <3")
                break
            elif escolha == "2":
                print("Ok, saindo...")
                break
            else:
                 print('Erro')
    if login != login_certo or senha != senha_certa:
        print("Errado! Tente novamente!")
        erros += 1
        
        if erros == 3:
             print("Acesso negado! Bloqueado!")
             break
        