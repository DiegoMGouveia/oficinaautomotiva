#casastrocliente simples 0.2
import clientenovo
from clientenovo import limpa
from clientenovo import Cliente
from datetime import datetime

clientenovo.limpa()
nome = ''
contato =''
endereco = ''
placa = ''
modelo = ''
cor = ''
ano = ''
tipodeservico = ''
observacao = ''
custo = ''
pago = ''
data = ''
prazo = ''


def cadastro():
    global nome
    global contato
    global endereco
    global placa
    global modelo
    global cor
    global ano
    global tipodeservico
    global observacao
    global custo
    global pago
    global data
    global prazo
    limpa()
    nome = input('Nome do Cliente.......................: ')
    contato = input('Contato............................: ')
    endereco = input('Endereço..........................: ')
    placa = input('Placa do veiculo.....................: ')
    modelo = input('Marca e modelo......................: ')
    cor = input('Cor....................................: ')
    ano = input('Ano de fabricação......................: ')
    tipodeservico = input('Descreva o serviço contratado: ')
    observacao = input('Observações.....................: ')
    custo = input('Valor do serviço.....................: ')
    pago = input('Pagamento.............................: ')
    data = datetime.today().strftime('%d-%m-%Y')
    prazo = input('Prazo de entrega.....................: ')


cadastro_seguranca = False
while not cadastro_seguranca:
    cadastro()
    limpa()
    print('REVISÃO DO CADASTRO:'
          '-------------------')
    newclient = clientenovo.Cliente(nome, contato, endereco, placa, modelo, cor, ano, tipodeservico, observacao,
                                        custo, pago, data, prazo)
    newclient.InfoCliente()
    perg = False
    while not perg:
        perg = input('[ S ] Salvar'
                     '[ E ] Editar'
                     '')
        if perg in 'Ss':
            print('Cliente salvo com sucesso!')
            cadastro_seguranca = True
            perg = True
        elif perg in 'Ee':
            limpa()
            print('OK, vamos recomeçar')
            perg = True
        else:
            print('Digite uma opção válida!')
            perg = False
