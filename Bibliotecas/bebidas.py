import random

def adicionarBebidas(lista):
    atual = dict()
    atual['nome'] = input('Digite o nome da Bebida: ')
    atual['quantidade'] = int(input('Digite a quantidade: '))
    codigo = random.randint(0, 100)
    atual['codigo'] = codigo
    lista.append(atual.copy())
    atual.clear()

def alterarBebidas():
    print('Digite o nome da Bebida:')

def excluirBebidas():
    print('Digite o nome da Bebida:')

def listarBebidas(lista):
    for bebida in lista:
        print(f"Bebida {bebida['codigo']}\nNome: {bebida['nome']}\nQuantidade: {bebida['quantidade']}\nCodigo: {bebida['codigo']}")
        print('\n----------------------------------------------')
