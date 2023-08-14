def comprar(lista):
    print('************************')
    print('*****COMPRAR BEBIDA*****')
    print('************************\n')
    print('1 = Buscar por nome')
    print('2 = Buscar por codigo')
    try:
        opcao = int(input('Digite a opcao desejada: '))
    except ValueError:
        print('Digite um inteiro valido!!!')
    else:
        if opcao == 1:
            nome = input('Digite o nome da bebida que deseja comprar: ')
            indice = 0
            for bebida in lista:
                if bebida['nome'] == nome:
                    print(f'Bebida a comprar: {bebida["nome"]}\nValor: {bebida["valor"]}')
                    try:
                        quantidade = int(input('Digite a quantidade desejada: '))
                    except ValueError:
                        print('Digite um inteiro valido!!!')
                    else:
                        confirmacao = input('\033[1;33mConfirmar(s=sim/n=nao):\033[m ')
                        if (confirmacao == 's' or confirmacao == 'S' or confirmacao == 'Sim' or confirmacao == 'sim'):
                            valorCompra = quantidade*bebida['valor']
                            print('Compra realizada com sucesso!!!')
                            bebida['quantidade'] = bebida['quantidade'] - quantidade
                            return valorCompra
                indice+=1
        elif opcao == 2:
            try:
                codigo = int(input('Digite o codigo da bebida que deseja comprar: '))
            except ValueError:
                print('Digite um inteiro valido!!!')
            else:
                indice = 0
                for bebida in lista:
                    if bebida['codigo'] == codigo:
                        print(f'Bebida a comprar: {bebida["nome"]}\nValor: {bebida["valor"]}')
                        try:
                            quantidade = int(input('\nDigite a quantidade desejada: '))
                        except ValueError:
                            print('Digite um inteiro valido!!!')
                        else:
                            confirmacao = input('Confirmar(s=sim/n=nao): ')
                            if (confirmacao == 's' or confirmacao == 'S' or confirmacao == 'Sim' or confirmacao == 'sim'):
                                valorCompra = quantidade * bebida['valor']
                                print('Compra realizada com sucesso!!!')
                                bebida['quantidade'] = bebida['quantidade'] - quantidade
                                return valorCompra
                    indice += 1