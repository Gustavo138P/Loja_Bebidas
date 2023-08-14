import random

def adicionarBebidas(lista):
    atual = dict()
    atual['nome'] = input('Digite o nome da Bebida: ')
    atual['quantidade'] = int(input('Digite a quantidade: '))
    codigo = random.randint(0, 100)
    atual['codigo'] = codigo
    atual['valor'] = float(input('Digite o valor da bebida: '))
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

def excluirBebidas(lista):
    print('************************')
    print('*****EXCLUIR BEBIDA*****')
    print('************************\n')
    print('1 = Buscar por nome')
    print('2 = Buscar por codigo')
    try:
        opcao = int(input('Digite a opcao desejada: '))
    except ValueError:
        print('Digite um inteiro valido!!!')
    else:
        if opcao == 1:
            nome = input('Digite o nome da bebida que deseja excluir: ')
            indice = 0
            for bebida in lista:
                if bebida['nome'] == nome:
                    print(f'Bebida a excluir: {bebida["nome"]}')
                    confirmacao = input('\033[1;33mConfirmar(s=sim/n=nao):\033[m ')
                    if (confirmacao == 's' or confirmacao == 'S' or confirmacao == 'Sim' or confirmacao == 'sim'):
                        lista.pop(indice)
                        print('Bebida excluida com sucesso!!!')
                indice+=1
        elif opcao == 2:
            try:
                codigo = int(input('Digite o codigo da bebida que deseja excluir: '))
            except ValueError:
                print('Digite um inteiro valido!!!')
            else:
                indice = 0
                for bebida in lista:
                    if bebida['codigo'] == codigo:
                        print(f'Bebida a excluir: {bebida["nome"]}')
                        confirmacao = input('\033[1;33mConfirmar(s=sim/n=nao):\033[m ')
                        if (confirmacao == 's' or confirmacao == 'S' or confirmacao == 'Sim' or confirmacao == 'sim'):
                            lista.pop(indice)
                            print('Bebida excluida com sucesso!!!')
                    indice += 1

def listarBebidas(lista):
    for bebida in lista:
        print(f"Bebida {bebida['codigo']}\nNome: {bebida['nome']}\nQuantidade: {bebida['quantidade']}\nValor: {bebida['valor']}\nCodigo: {bebida['codigo']}")
        print('\n----------------------------------------------')
