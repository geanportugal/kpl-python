# -*- coding: utf-8 -*-
from ..enums import TipoLocalEntregaEnum, TipoPessoaEnum
# (*) = Campos obrigatórios segundo a documentação


class Order(object):
	NumeroDoPedido = None            								# String 50 Código do pedido (*)
	EMail = None                     								# String 100 E-mail (Se for digitado o código do cliente não será necessário digitar o e-mail e nem CPF) (*)
	CPFouCNPJ = None                 								# String 14 CPF ou CNPJ (Se for digitado o código do cliente, não será necessário digitar o CPF/CNPJ e nem o e-mail) (*)
	CodigoCliente = None             								# String 50 Código do cliente (*)
	RepresentanteVendas = None       								# String 50 Representante de vendas
	CondicaoPagamento = None         								# String 50 Nome da condição de pagamento (*)
	ValorPedido = 0                  								# Float - Valor do pedido (*)
	ValorFrete = 0                   								# Float - Valor do frete
	ValorEncargos = 0                								# Float - Valor de encargos
	ValorDesconto = 0                								# Float - Valor do desconto concedido no pedido
	ValorEmbalagemPresente = 0       								# Float - Valor de embalagens para presente
	ValorReceberEntrega = None       								# String 50 Valor a receber
	ValorTrocoEntrega = None         								# String 50 Valor de troco
	DataVenda = None                 								# Datetime - Data venda (*)
	Transportadora = None            								# String 50 Nome da transportadora
	ServicoEntrega = None            								# String 50 Nome do serviço de entrega
	Canal = None                     								# String 50 Canal
	SubCanal = None                  								# String 50 SubCanal
	EmitirNotaSimbolica = False      								# Bool - Emitir nota fiscal simbólica? Serve para pedidos para presente onde a nota fiscal deve ser enviada ao presentado (*)
	ValorCupomDesconto = 0           								# Float - Valor do cupom de desconto
	NumeroCupomDesconto = None       								# String 40 Número do cupom de desconto
	Lote = None                      								# String 50 Lote do pedido de venda (*)
	DestNome = None                  								# String 50 Destinatário – Nome
	DestSexo = None                  								# Char 1 Destinatário – Sexo (F, M ou E)
	DestEmail = None                 								# String 100 Destinatário - E-Mail
	DestTelefone = None              								# String 15 Destinatário – Telefone
	DestLogradouro = None            								# String 80 Destinatário – Logradouro
	DestNumeroLogradouro = None      								# String 50 Destinatário - Número
	DestComplementoEndereco = None   								# String 50 Destinatário – Complemento
	DestBairro = None                								# String 60 Destinatário - Bairro
	DestMunicipio = None             								# String 60 Destinatário - Município
	DestEstado = None                								# String 50 Destinatário - Estado
	DestCep = None                   								# String 20 Destinatário - CEP
	DestTipoLocalEntrega = TipoLocalEntregaEnum.tleeDesconhecido    # String - Valores disponiveis: enumTipoLocalEntrega
	DestEstrangeiro = None           								# Char 1 Destinatário - Flag estrangeiro
	DestPais = None                  								# String 100 Destinatário - País
	DestCPF = None                   								# String 14 Destinatário - CPF ou CNPJ
	DestTipoPessoa = TipoPessoaEnum.tpeFisica            			# String - Valore disponíveis: enumTipoPessoa
	DestDocumento = None             								# Char 14 Destinatário - Número de documento
	DestInscricaoEstadual = None     								# Char 14 Destinatário - Inscrição estadual
	DestInscricaoMunicipal = None    								# Char 15 Destinatário - Inscrição municipal
	DestReferencia = None            								# String 60 Destinatário - Referência
	Anotacao1 = None                 								# Text - Anotação
	Anotacao2 = None                 								# Text - Anotação
	Anotacao3 = None                 								# Text - Anotação
	PedidoJaPago = False             								# Bool - Pedido já foi pago?
	DataDoPagamento = None           								# Datetime - Data do pagamento
	OptouNFPaulista = None           								# String - Valores possíveis: enumOptouNFPaulista (*)
	CodigoCartaoPresente = None      								# String 50 Código do cartão presente
	MensagemCartaoPresente = None    								# Text - Mensagem para o cartão
	AssinaturaCartaoPresente = None  								# String 100 Assinatura do cartão
	ValorTotalCartaoPresente = 0     								# Float - Valor total do cartão
	CartaoPresenteBrinde = False     								# Bool - O cartão de presente é um brinde? (*)
	TempoEntregaTransportadora = 0   								# Int - Tempo de entrega da transportadora
	DataPrazoEntregaInicial = None   								# Datetime - Data inicial do prazo de entrega
	DataPrazoEntregaFinal = None     								# Datetime - Data final do prazo de entrega
	TipoEntrega = None               								# String 50 Tipo de entrega
	CodigoLocalRetirada = None       								# String 50 Local retirada
	SenhaRetirada = None             								# String 50 Senha retirada
	IPComprador = None               								# String 50 IP do usuário quando este efetuou a compra
	ComercializacaoOutrasSaidas = 0  								# Int - Comercialização outras saídas
	PrazoEntregaPosPagamento = 0     								# Float - Prazo de entrega pós-pagamento
	ValorFretePagar = 0 											# Float - Valor do frete a ser pago pela empresa
	CampoUsoLivre = None  											# String 50 Campo uso livre
	CodigoListaPresente = None 										# String 50 Código lista de presente
	TelefoneSMS = None 												# String 20 Numero de telefone para SMS
	ValorAdicionalImpostos = 0									    # Float IMPORTANTE: este campo NÃO está na documentação, foi encontrada no DEBUG, na raça


class OrderItem(object):
	CodigoProduto = None       # String 50 Código do produto (*)
	QuantidadeProduto = 0      # Float - Quantidade de produtos (*)
	PrecoUnitario = 0          # Float - Preço unitário (*)
	EmbalagemPresente = False  # Bool - Embalagem para presente?
	MensagemPresente = None    # Text - Mensagem presente
	PrecoUnitarioBruto = 0     # Float - Preço unitário bruto
	Brinde = False             # Bool - Brinde? (*)
	ValorReferencia = 0        # Float - Valor referencia


class OrderPayment(object):
	FormaPagamentoCodigo = None          # Int Código da forma de pagamento. O KPL não aceita duas formas de pagamento do tipo cupom de desconto.
	Valor = 0                            # Float - Valor
	CartaoNumero = None                  # String 255 Numero do cartão
	CartaoCodigoSeguranca = None         # String 255 Código do cartão de segurança
	CartaoValidade = None                # String 255 Validade do cartão
	CartaoNomeImpresso = None            # String 50 Nome impresso no cartão
	CartaoQtdeParcelas = 0               # Int - Quantidade de parcelas
	CartaoCodigoAutorizacao = None       # String 50 Código autorização cartão
	BoletoVencimento = None              # Datetime - Boleto vencimento
	BoletoNumeroBancario = None          # String 20 Numero bancário boleto
	CartaoCPFouCNPJTitular = None        # Char 14 CPF ou CNPJ do titular do cartão de crédito
	CartaoDataNascimentoTitular = None   # Datetime - Data de nascimento do titular do cartão
	DebitoEmContaNumeroBanco = None      # String 10 Número do banco para débito em conta corrente
	DebitoEmContaCodigoAgencia = None    # String 10 Código da agência para débito em conta corrente
	DebitoEmContaDVCodigoAgencia = None  # Char 2 Digito da agencia para debito em conta
	DebitoEmContaContaCorrente = None    # String 20 Debito em conta
	DebitoEmContaDVContaCorrente = None  # Char 2 Número do dígito da conta para débito em conta corrente
	PreAutorizadaNaPlataforma = False    # Bool - Identificar se o pedido teve ou não sua pré-autorização na Plataforma. (*)
	CartaoTID = None                     # String 50 Código da transação da empresa intermediária de cobrança.
	CartaoNSU = None                     # String 50 Número sequencial único da transação de cartão.
	CartaoNumeroToken = None             # String 50 Número Token do cartão de crédito.
	CodigoTransacaoGateway = None        # String 100 Identificador da transação no gateway.


class ConfirmOrderPayment(object):
	NumeroPedido = None             # String 50 Número do pedido
	DataPagamento = None            # String 21 Data do pagamento
	CartaoCodigoAutorizacao = None  # String 50 Código autorização cartão
	CartaoNSU = None                # String 50 Cartão NSU
	CartaoTID = None                # String 50 Cartão TID
	CartaoCodigoRetorno = None      # String 15 Código de retorno do cartão
	CartaoMensagemRetorno = None    # String 255 Código de retorno do cartão
	StatusPagamento = None          # String - Valores disponíveis: enumStatusPagamento


class CancelOrder(object):
	CodigoPedido = None              # String 50 Número do pedido (*)
	CodigoMotivoCancelamento = None  # Int - Código do motivo de cancelamento. Será incluído no campo “Motivo” (*)
	MensagemCancelamento = None      # String 50 Mensagem de cancelamento. Será incluído no campo “Observação do status”
