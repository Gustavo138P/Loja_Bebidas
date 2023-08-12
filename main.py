from Bibliotecas import *
primeraVez = True

while(True):
    print('**********************')
    print('*****MENU INICIAL*****')
    print('**********************\n')
    print('1 = Funcionario')
    print('2 = Cliente')
    print('3 = Fechar Programa')
    try:
        opcao = int(input('Digite sua opcao: '))
    except ValueError:
        print('Digite um inteiro valido!!!')
    else:
        match opcao:
            case 1:
                if primeraVez == True:
                    senha = input('\nCrie uma senha de acesso: ')
                    print(f'senha digitada: {senha}')
                    confirmar = input('\nConfirmar senha?(s=sim/n=não)')
                    if confirmar == 's' or confirmar == 'S':
                        primeraVez = False
                        menuFuncionario(senha)
                    else:
                        menuFuncionario(senha)
            case 2:
                menuCliente()
            case 3:
                exit(0)
            case _:
                print('Opcao Inexistente!!')