# -*- coding: utf-8 -*-
import unittest
from . enums import *
import datetime
from . order import OrderSoap
from . entities.order import Order, OrderItem, OrderPayment, CancelOrder


class TestOrder(unittest.TestCase):

    def setUp(self):
        o = Order()
        o.NumeroDoPedido = 123
        o.EMail = "ciclano2@gmail.com"
        o.CPFouCNPJ = "531.722.797-66"
        o.CodigoCliente = "100000012"
        # o.RepresentanteVendas = None
        # o.CondicaoPagamento = None
        o.ValorPedido = 150.99
        o.ValorFrete = 15.00
        # o.ValorEncargos = 0
        # o.ValorDesconto = 0
        # o.ValorEmbalagemPresente = 0
        # o.ValorReceberEntrega = None
        # o.ValorTrocoEntrega = None
        o.DataVenda = datetime.datetime(2018, 3, 12, 23, 59, 34)
        o.Transportadora = "Correios"
        o.ServicoEntrega = "PAC"
        # o.Canal = None
        # o.SubCanal = None
        # o.EmitirNotaSimbolica = False
        # o.ValorCupomDesconto = 0
        # o.NumeroCupomDesconto = None
        # o.Lote = None
        o.DestNome = "Mateus"
        o.DestSexo = "M"
        o.DestEmail = "mateuspaduaweb@gmail.com"
        o.DestTelefone = "(16) 99101-1851"
        o.DestLogradouro = "Rua Parque do Araçá"
        o.DestNumeroLogradouro = "234"
        o.DestComplementoEndereco = "perto da praca"
        o.DestBairro = "Jardim Paulista"
        o.DestMunicipio = "Ribeirão Preto"
        o.DestEstado = "SP"
        o.DestCep = "14092-560"
        # o.DestTipoLocalEntrega = enums.TipoLocalEntregaEnum.tleeDesconhecido
        # o.DestEstrangeiro = None
        # o.DestPais = None
        # o.DestCPF = None
        # o.DestTipoPessoa = enums.TipoPessoaEnum.tpeFisica
        # o.DestDocumento = None
        # o.DestInscricaoEstadual = None
        # o.DestInscricaoMunicipal = None
        # o.DestReferencia = None
        # o.Anotacao1 = None
        # o.Anotacao2 = None
        # o.Anotacao3 = None
        # o.PedidoJaPago = False
        # o.DataDoPagamento = None
        o.OptouNFPaulista = OptouNFPaulistaEnum.tbneNao
        # o.CodigoCartaoPresente = None
        # o.MensagemCartaoPresente = None
        # o.AssinaturaCartaoPresente = None
        # o.ValorTotalCartaoPresente = 0
        # o.CartaoPresenteBrinde = False
        # o.TempoEntregaTransportadora = 0
        # o.DataPrazoEntregaInicial = None
        # o.DataPrazoEntregaFinal = None
        # o.TipoEntrega = None
        # o.CodigoLocalRetirada = None
        # o.SenhaRetirada = None
        o.IPComprador = "192.189.33.45"
        # o.ComercializacaoOutrasSaidas = 0
        # o.PrazoEntregaPosPagamento = 0
        self.order = o

        self.order_items = []
        for i in range(1, 3):
            oi = OrderItem()
            oi.CodigoProduto = "AABB12_{}".format(i)
            oi.QuantidadeProduto = 0 + i
            oi.PrecoUnitario = 10 * i
            # oi.EmbalagemPresente = False
            # oi.MensagemPresente = None
            # oi.PrecoUnitarioBruto = 0
            # oi.Brinde = False
            # oi.ValorReferencia = 0
            self.order_items.append(oi)

        self.os = OrderSoap(api_key="F8194B4C-F6B9-45AD-9914-8FDF53E8601C")
        # print self.os.client

    # def test_create_order_billite(self):
    #     op = OrderPayment()
    #     op.FormaPagamentoCodigo = "billet_teste"
    #     op.Valor = 150.99
    #     # op.CartaoNumero = "4578.*****.8978"
    #     # op.CartaoCodigoSeguranca = "123"
    #     # op.CartaoValidade = "12/22"
    #     # op.CartaoNomeImpresso = "Mateus Padua"
    #     # op.CartaoQtdeParcelas = 0
    #     # op.CartaoCodigoAutorizacao = None
    #     op.BoletoVencimento = datetime.date(2018, 8, 10)
    #     op.BoletoNumeroBancario = "123456789"
    #     # op.CartaoCPFouCNPJTitular = "531.722.797-66"
    #     # op.CartaoDataNascimentoTitular = None
    #     # op.DebitoEmContaNumeroBanco = None
    #     # op.DebitoEmContaCodigoAgencia = None
    #     # op.DebitoEmContaDVCodigoAgencia = None
    #     # op.DebitoEmContaContaCorrente = None
    #     # op.DebitoEmContaDVContaCorrente = None
    #     # op.PreAutorizadaNaPlataforma = False
    #     # op.CartaoTID = None
    #     # op.CartaoNSU = None
    #     # op.CartaoNumeroToken = None
    #     # op.CodigoTransacaoGateway = None
    #     r = self.os.add_order(self.order, self.order_items, op)
    #     print r
    #     # self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    def test_get_availables_status_orders(self):
        r = self.os.get_availables_status_orders()
        print(r)
        # print self.os.client.last_sent()

    # def test_set_order_cancel(self):
    #     oc = CancelOrder()
    #     oc.CodigoPedido = "227009"
    #     oc.CodigoMotivoCancelamento = 10
    #     oc.MensagemCancelamento = "mensagem teste cancelamento á yaaa ã"
    #     print self.os.cancel_order(oc)
