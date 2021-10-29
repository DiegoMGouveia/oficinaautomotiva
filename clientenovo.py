# cadastrando o cliente e o veiculo para serviço
# classe cliente


def limpa():
    print('\n'*100)


class Cliente:
    id = 0
    cliente = ''
    contato = ''
    endereco = ''
    placa = ''
    modelo = ''
    cor = ''
    ano = 0
    tipodeservico = ''
    observacao = ''
    custo = ''
    pago = False
    data = ''
    prazo = ''
    def __init__(self, clien, conta, ender, placa, model, cor, ano, tipod, obser, custo, pago, data, prazo):
        self.cliente = clien
        self.contato = conta
        self.endereco = ender
        self.placa = placa
        self.modelo = model
        self.cor = cor
        self.ano = ano
        self.tipodeservico = tipod
        self.observacao = obser
        self.custo = custo
        self.pago = pago
        self.data = data
        self.prazo = prazo

    def InfoCliente(self):
        limpa()
        print('-'*35)
        print(f'Nome do Cliente: {self.cliente}'
              f'Contato: {self.contato}'
              f'Endereço: {self.endereco}'
              f'Placa: {self.placa}'
              f'Marca/Modelo: {self.modelo}'
              f'Cor: {self.cor}'
              f'Ano: {self.ano}'
              f'Tipo de serviço: {self.tipodeservico}'
              f'Custo: {self.custo}'
              f'Pagamento: {self.pago}'
              f'Data: {self.data}'
              f'Prazo de entrega: {self.prazo}'
              f'Observações: {self.observacao}')
        print('-'*35)

