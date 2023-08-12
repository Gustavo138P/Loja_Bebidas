from Bibliotecas import bebidas
from Bibliotecas import clientes
def menuFuncionario(senha):
    print('**************************')
    print('*****MENU FUNCIONARIO*****')
    print('**************************\n')
    senhaD = input('Digite a senha de Acesso: ')

    if senhaD == senha:
        print('**************************')
        print('*****MENU FUNCIONARIO*****')
        print('**************************\n')
        print('1 = Modificar lista de clientes')
        print('2 = modificar lista de produtos')
        opcao2 = int(input('Digite sua opcao: '))

        match opcao2:
            case 1:
                print('1 = Alterar Dados Clientes')
                print('2 = Excluir Clientes')
                print('3 = Listar Clientes')
                print('4 = Voltar ao Menu Inicial')
                try:
                    opcao3 = int(input('Digite sua opcao: '))
                except ValueError:
                    print('Digite um inteiro valido!!!')
                else:
                    match opcao3:
                        case 1:
                            clientes.alterarCliente()
                        case 2:
                            clientes.excluirCliente()
                        case 3:
                            clientes.listarCliente()
                        case 4:
                            exit(0)
                        case _:
                                print('Opcao Inexistente!!')
            case 2:
                print('1 = Adicionar Bebidas')
                print('2 = Alterar Bebidas')
                print('3 = Excluir Bebidas')
                print('4 = Listar Bebidas')
                print('5 = Voltar ao Menu Inicial')
                try:
                    opcao = int(input('Digite sua opcao: '))
                except ValueError:
                    print('Digite um inteiro valido!!!')
                else:
                    match opcao:
                        case 1:
                            bebidas.adicionarBebidas()
                        case 2:
                            bebidas.alterarBebidas()
                        case 3:
                            bebidas.excluirBebidas()
                        case 4:
                            bebidas.listarBebidas()
                        case 5:
                            exit(0)
                        case _:
                                print('Opcao Inexistente!!')
    else:
        print('Senha Invalida!!!')

def menuCliente():
    print('**********************')
    print('*****MENU CLIENTE*****')
    print('**********************\n')
    listarBebidas()
    try:
        opcao = int(input('Digite o codigo da bebida desejada: '))
    except ValueError:
        print('Digite um inteiro valido!!!')
    else:
        print(opcao)
