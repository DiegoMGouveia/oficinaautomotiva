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
        print(f'Nome do Cliente: {self.cliente}\n'
              f'Contato: {self.contato}\n'
              f'Endereço: {self.endereco}\n'
              f'Placa: {self.placa}\n'
              f'Marca/Modelo: {self.modelo}\n'
              f'Cor: {self.cor}\n'
              f'Ano: {self.ano}\n'
              f'Tipo de serviço: {self.tipodeservico}\n'
              f'Custo: {self.custo}\n'
              f'Pagamento: {self.pago}\n'
              f'Data: {self.data}\n'
              f'Prazo de entrega: {self.prazo}\n'
              f'Observações: {self.observacao}\n')
        print('-'*35)

