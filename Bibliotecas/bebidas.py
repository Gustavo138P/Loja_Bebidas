import random

def adicionarBebidas(lista):
    atual = dict()
    atual['nome'] = input('Digite o nome da Bebida: ')
    atual['quantidade'] = int(input('Digite a quantidade: '))
    codigo = random.randint(0, 100)
    atual['codigo'] = codigo
    lista.append(atual.copy())
    atual.clear()

def alterarBebidas(lista):
    print('***********************')
    print('*****ALTERAR BEBIDA*****')
    print('**********************\n')
    print('1 = Buscar por nome')
    print('2 = Buscar por codigo')
    try:
        opcao = int(input('Digite a opcao desejada: '))
    except ValueError:
        print('Digite um inteiro valido!!!')
    else:
        if opcao == 1:
            nome = input('Digite o nome da bebida que deseja altera: ')
            for bebida in lista:
                if nome == bebida['nome']:
                    print('1 = Alterar nome')
                    print('2 = Alterar quantidade')
                    try:
                        opcao2 = int(input('Digite a opcao desejada: '))
                    except ValueError:
                        print('Digite um inteiro valido!!!')
                    else:
                        match opcao2:
                            case 1:
                                bebida['nome'] = input('Digite o novo nome: ')
                            case 2:
                                try:
                                    bebida['quantidade'] = int(input('Digite a nova quantidade: '))
                                except ValueError:
                                    print('Digite um inteiro valido!!!')
        elif opcao == 2:
            try:
                codigo = int(input('Digite o codigo da bebida que deseja altera: '))
            except ValueError:
                print('Digite um inteiro valido!!!')
            else:
                for bebida in lista:
                    if codigo == bebida['codigo']:
                        print('1 = Alterar nome')
                        print('2 = Alterar quantidade')
                        try:
                            opcao2 = int(input('Digite a opcao desejada: '))
                        except ValueError:
                            print('Digite um inteiro valido!!!')
                        else:
                            match opcao2:
                                case 1:
                                    bebida['nome'] = input('Digite o novo nome: ')
                                case 2:
                                    try:
                                        bebida['quantidade'] = int(input('Digite a nova quantidade: '))
                                    except ValueError:
                                        print('Digite um inteiro valido!!!')


def excluirBebidas():
    print('Digite o nome da Bebida:')

def listarBebidas(lista):
    for bebida in lista:
        print(f"Bebida {bebida['codigo']}\nNome: {bebida['nome']}\nQuantidade: {bebida['quantidade']}\nCodigo: {bebida['codigo']}")
        print('\n----------------------------------------------')
