#casastrocliente simples 0.6
from datetime import datetime
import sqlite3
from sqlite3 import Error


def limpa(): #limpar a tela
    print('\n'*100)


def ConexaoBanco(): #conexao com banco de dados
    caminho = "/ESCREVA O PATH DA SUA DB AQUI/lojacarros/basededadosoficina.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


def insert(conexao,sql): #inserindo informações no banco de dados
    try:
        c = conexao.cursor()
        c.execute(sql)
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

    def Info(self):
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


def cadastro():
    limpa()
    cadastro_loop = False
    while not cadastro_loop:
        cliente = input('Nome do Cliente....................: ')
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
        novocliente = Cliente(cliente,contato,endereco,placa,modelo,cor,ano,tipodeservico,custo,pago,
                              data,prazo,observacao)
        cadastro_seguranca = False
        while not cadastro_seguranca: #verificando itens antes de salvar
            limpa()
            print('REVISÃO DO CADASTRO:'
                  '-------------------')
            print('-' * 35)
            novoc.Info()
            print('-' * 35)
            perg = False
            while not perg:
                perg = input('[ S ] Salvar [ E ] Editar ')
                if perg in 'Ss':
                    salvaseguranca = True
                    perg = 0
                    insql = """INSERT INTO clientesdb
                                    (NOME,CONTATO,ENDERECO,PLACA,MODELO,COR,ANO,TIPODESERVICO,OBERVACAO,CUSTO,PAGO,
                                     DATA, PRAZO)
                             VALUES('""" + novoc.cliente + """','""" + novoc.contato + """',
                             '""" + novoc.endereco + """','""" + novoc.placa + """','""" + novoc.modelo + """',
                             '""" + novoc.cor + """','""" + novoc.ano + """','""" + novoc.tipodeservico + """',
                             '""" + novoc.observacao + """','""" + novoc.custo + """','""" + novoc.pago + """',
                             '""" + novoc.data + """','""" + novoc.prazo + """'
                                    )"""
                    insert(vcon, insql) #inserindo na tabela
                    print('Cliente salvo com sucesso!')
                    cadastro_seguranca = True
                    perg = True
                    cadastro_loop = True
                    continue
                elif perg in 'Ee':
                    limpa()
                    print('OK, vamos recomeçar')
                    cadastro_seguranca = True
                    perg = True
                    continue
                else:
                    print('Digite uma opção válida!')
                    perg = False


cadastro()
vcon.close()
