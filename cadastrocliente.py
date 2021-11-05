#casastrocliente simples 0.7

from datetime import datetime
import sqlite3
from sqlite3 import Error


def menu():
    limpa()
    print('Digite uma opção:\n'
          '----------------\n'
          '[1] Cadastrar Cliente\n'
          '[2] Buscar/Editar Cliente\n'
          '[3] Excluir CLiente')

def limpa(): #limpar a tela
    print('\n'*100)


def ConexaoBanco(): #conexao com banco de dados
    caminho = "/DIGITE O ENDEREÇO DA SUA DATABASE AQUI/basededadosoficina.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


def insert(conexao,args): #inserindo informações no banco de dados
    insql = """INSERT INTO clientesdb
                     (NOME,CONTATO,ENDERECO,PLACA,MODELO,COR,ANO,TIPODESERVICO,OBERVACAO,CUSTO,PAGO,
                      DATA, PRAZO)
              VALUES('""" + args.cliente + """','""" + args.contato + """',
              '""" + args.endereco + """','""" + args.placa + """','""" + args.modelo + """',
              '""" + args.cor + """','""" + args.ano + """','""" + args.tipodeservico + """',
              '""" + args.observacao + """','""" + args.custo + """','""" + args.pago + """',
              '""" + args.data + """','""" + args.prazo + """'
                     )"""
    try:
        c = conexao.cursor()
        c.execute(insql)
        conexao.commit()
    except Error as ex:
        print(ex)

vcon = ConexaoBanco()


class Cliente:
    def __init__(self, clien, conta, ender, placa, model, cor, ano, tipod, custo, pago, data, prazo, obser):
        self.cliente = clien
        self.contato = conta
        self.endereco = ender
        self.placa = placa
        self.modelo = model
        self.cor = cor
        self.ano = ano
        self.tipodeservico = tipod
        self.custo = custo
        self.pago = pago
        self.data = data
        self.prazo = prazo
        self.observacao = obser

    def InfoCliente(self):
        limpa()
        print('-'*35)
        print(f'Nome do Cliente.: {self.cliente}\n'
              f'Contato.........: {self.contato}\n'
              f'Endereço........: {self.endereco}\n'
              f'Placa...........: {self.placa}\n'
              f'Marca/Modelo....: {self.modelo}\n'
              f'Cor.............: {self.cor}\n'
              f'Ano.............: {self.ano}\n'
              f'Tipo de serviço.: {self.tipodeservico}\n'
              f'Custo...........: {self.custo}\n'
              f'Pagamento.......: {self.pago}\n'
              f'Data............: {self.data}\n'
              f'Prazo de entrega: {self.prazo}\n'
              f'Observações.....: {self.observacao}\n')
        print('-'*35)


def cadastro(args):
    limpa()
    cliente = input('Nome do Cliente.......................: ')
    contato = input('Contato............................: ')
    endereco = input('Endereço..........................: ')
    placa = input('Placa do veiculo.....................: ')
    modelo = input('Marca e modelo......................: ')
    cor = input('Cor....................................: ')
    ano = input('Ano de fabricação......................: ')
    tipodeservico = input('Descreva o serviço contratado: ')
    custo = input('Valor do serviço.....................: ')
    pago = input('Pagamento.............................: ')
    data = datetime.today().strftime('%d-%m-%Y')
    prazo = input('Prazo de entrega.....................: ')
    observacao = input('Observações.....................: ')
    novocliente = args(cliente,contato,endereco,placa,modelo,cor,ano,tipodeservico,custo,pago,
                          data,prazo,observacao)
    return novocliente


def revisao(arg):
    limpa()
    print('-' * 35)
    arg.InfoCliente()
    print('-' * 35)


######## inicio do programa
programa = True
menu()
while programa:
    opcao_menu = input('Digite uma opção do menu: ')
    if opcao_menu.isnumeric():
        if int(opcao_menu) == 1:
            while programa:
                cliente = cadastro(Cliente)
                revisao(cliente)
                while programa:
                    save = input('Salvar cliente? [s/n] ')
                    if save in 'SsNn':
                        if save in 'Ss':
                            save = insert(vcon, cliente)
                            programa = False
                            continue
                    else:
                        revisao(cliente)
                        print('Digite apenas S ou N para responder!')
                        continue
    else:
        menu()
        print('Digite apenas números para escolher uma opção do menu!')
        continue

vcon.close()
