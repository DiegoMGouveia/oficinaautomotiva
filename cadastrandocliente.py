#casastrocliente simples 0.3
from datetime import datetime
import sqlite3
from sqlite3 import Error


# variaveis utilizadas na função cadastro() e
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
importar = []



def limpa(): #limpar a tela
    print('\n'*100)


def ConexaoBanco(): #conexao com banco de dados
    caminho = "/media/diego/EA00FB8D00FB5F4F/python3 projetos/lojacarros/basededadosoficina.db"
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
    global importar
    global insql
    limpa()
    cadastro_loop = False
    while not cadastro_loop:
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
        while not cadastro_seguranca: #verificando itens antes de salvar
            limpa()
            print('REVISÃO DO CADASTRO:'
                  '-------------------')
            print('-' * 35)
            print(f'Nome do Cliente.: {nome}\n'
                  f'Contato.........: {contato}\n'
                  f'Endereço........: {endereco}\n'
                  f'Placa...........: {placa}\n'
                  f'Marca/Modelo....: {modelo}\n'
                  f'Cor.............: {cor}\n'
                  f'Ano.............: {ano}\n'
                  f'Tipo de serviço.: {tipodeservico}\n'
                  f'Observações.....: {observacao}\n'
                  f'Custo...........: {custo}\n'
                  f'Pagamento.......: {pago}\n'
                  f'Data............: {data}\n'
                  f'Prazo de entrega: {prazo}\n')
            print('-' * 35)
            perg = False
            while not perg:
                perg = input('[ S ] Salvar'
                             '[ E ] Editar'
                             ' ')
                if perg in 'Ss':
                    salvaseguranca = True
                    perg = 0
                    insql = """INSERT INTO clientesdb
                                    (NOME,CONTATO,ENDERECO,PLACA,MODELO,COR,ANO,TIPODESERVICO,OBERVACAO,CUSTO,PAGO,
                                     DATA, PRAZO)
                             VALUES('""" + nome + """','""" + contato + """','""" + endereco + """',
                             '""" + placa + """','""" + modelo + """','""" + cor + """','""" + ano + """',
                             '""" + tipodeservico + """','""" + observacao + """','""" + custo + """',
                             '""" + pago + """','""" + data + """','""" + prazo + """'
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
