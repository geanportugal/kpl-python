
from datetime import datetime
import re
from . enums import *
from . utils import get_aware_text, smart_encode, parse_response_confirm_integration
from . base import ClientSoap


class OrderSoap(ClientSoap):

    def _order_factory(self, order, order_items, payments):
        o = self.client.factory.create('DadosPedidos')

        # ========================= Dados do pedido ===========================
        o.NumeroDoPedido = order.NumeroDoPedido
        o.RepresentanteVendas = get_aware_text(order.RepresentanteVendas)
        o.CondicaoPagamento = get_aware_text(order.CondicaoPagamento)
        o.ValorPedido = order.ValorPedido
        o.ValorFrete = order.ValorFrete
        o.ValorEncargos = order.ValorEncargos
        o.ValorDesconto = order.ValorDesconto
        o.ValorEmbalagemPresente = order.ValorEmbalagemPresente
        o.ValorReceberEntrega = get_aware_text(order.ValorReceberEntrega)
        o.ValorTrocoEntrega = get_aware_text(order.ValorTrocoEntrega)
        o.DataVenda = order.DataVenda.strftime('%d%m%Y %H:%M:%S.%f')
        o.Transportadora = get_aware_text(order.Transportadora)
        o.ServicoEntrega = get_aware_text(order.ServicoEntrega)
        o.Canal = get_aware_text(order.Canal)
        o.SubCanal = get_aware_text(order.SubCanal)
        o.EmitirNotaSimbolica = order.EmitirNotaSimbolica
        o.ValorCupomDesconto = order.ValorCupomDesconto
        o.NumeroCupomDesconto = get_aware_text(order.NumeroCupomDesconto)
        o.Lote = get_aware_text(order.Lote)
        o.DestNome = get_aware_text(order.DestNome)
        o.DestSexo = order.DestSexo
        o.DestEmail = get_aware_text(order.DestEmail)
        o.DestTelefone = get_aware_text(order.DestTelefone)
        o.DestLogradouro = get_aware_text(order.DestLogradouro)
        o.DestNumeroLogradouro = get_aware_text(order.DestNumeroLogradouro)
        o.DestComplementoEndereco = get_aware_text(order.DestComplementoEndereco)
        o.DestBairro = get_aware_text(order.DestBairro)
        o.DestMunicipio = get_aware_text(order.DestMunicipio)
        o.DestEstado = get_aware_text(order.DestEstado)
        o.DestCep = re.sub(r'[^\d]+', '', get_aware_text(order.DestCep)) if order.DestCep else None
        o.DestTipoLocalEntrega = get_aware_text(order.DestTipoLocalEntrega)
        o.DestEstrangeiro = order.DestEstrangeiro
        o.DestPais = get_aware_text(order.DestPais)
        o.DestCPF = get_aware_text(order.DestCPF)
        o.DestTipoPessoa = get_aware_text(order.DestTipoPessoa)
        o.DestDocumento = get_aware_text(order.DestDocumento)
        o.DestInscricaoEstadual = get_aware_text(order.DestInscricaoEstadual)
        o.DestInscricaoMunicipal = get_aware_text(order.DestInscricaoMunicipal)
        o.DestReferencia = get_aware_text(order.DestReferencia)
        o.Anotacao1 = get_aware_text(order.Anotacao1)
        o.Anotacao2 = get_aware_text(order.Anotacao2)
        o.Anotacao3 = get_aware_text(order.Anotacao3)
        o.PedidoJaPago = order.PedidoJaPago
        o.DataDoPagamento = order.DataDoPagamento.strftime('%d%m%Y %H:%M:%S.%f') if order.DataDoPagamento else None
        o.OptouNFPaulista = get_aware_text(order.OptouNFPaulista)
        o.CodigoCartaoPresente = get_aware_text(order.CodigoCartaoPresente)
        o.MensagemCartaoPresente = order.MensagemCartaoPresente
        o.AssinaturaCartaoPresente = get_aware_text(order.AssinaturaCartaoPresente)
        o.ValorTotalCartaoPresente = order.ValorTotalCartaoPresente
        o.CartaoPresenteBrinde = order.CartaoPresenteBrinde
        o.TempoEntregaTransportadora = order.TempoEntregaTransportadora
        o.DataPrazoEntregaInicial = order.DataPrazoEntregaInicial
        o.DataPrazoEntregaFinal = order.DataPrazoEntregaFinal
        o.TipoEntrega = get_aware_text(order.TipoEntrega)
        o.CodigoLocalRetirada = get_aware_text(order.CodigoLocalRetirada)
        o.SenhaRetirada = get_aware_text(order.SenhaRetirada)
        o.IPComprador = get_aware_text(order.IPComprador)
        o.ComercializacaoOutrasSaidas = order.ComercializacaoOutrasSaidas
        o.PrazoEntregaPosPagamento = order.PrazoEntregaPosPagamento
        o.ValorFretePagar = order.ValorFretePagar
        o.ValorAdicionalImpostos = order.ValorAdicionalImpostos

        # Dados do cliente ====================================================
        o.EMail = get_aware_text(order.EMail)
        o.CPFouCNPJ = re.sub(r'[^\d]+', '', get_aware_text(order.CPFouCNPJ)) if order.CPFouCNPJ else None
        o.CodigoCliente = get_aware_text(order.CodigoCliente)

        # Itens do pedido =====================================================
        o.Itens = self._order_items_factory(order_items)

        # Métodos de pagamento do pedido ======================================
        pms = []
        for payment in payments:
            pms.append(self._payment_factory(payment))

        ArrayOfDadosPedidosFormaPgto = self.client.factory.create('ArrayOfDadosPedidosFormaPgto')
        ArrayOfDadosPedidosFormaPgto.DadosPedidosFormaPgto = [pms]

        o.FormasDePagamento = ArrayOfDadosPedidosFormaPgto

        return o

    def _order_items_factory(self, order_items):
        ArrayOfDadosPedidosItem = self.client.factory.create('ArrayOfDadosPedidosItem')
        order_items_list = []

        for order_item in order_items:
            oi = self.client.factory.create('DadosPedidosItem')
            oi.CodigoProduto = order_item.CodigoProduto
            oi.QuantidadeProduto = order_item.QuantidadeProduto
            oi.PrecoUnitario = order_item.PrecoUnitario
            oi.EmbalagemPresente = order_item.EmbalagemPresente
            oi.MensagemPresente = get_aware_text(order_item.MensagemPresente)
            oi.PrecoUnitarioBruto = order_item.PrecoUnitarioBruto
            oi.Brinde = order_item.Brinde
            oi.ValorReferencia = order_item.ValorReferencia
            order_items_list.append(oi)

        ArrayOfDadosPedidosItem.DadosPedidosItem = order_items_list
        return ArrayOfDadosPedidosItem

    def _payment_factory(self, payment):
        pm = self.client.factory.create('DadosPedidosFormaPgto')

        pm.FormaPagamentoCodigo = payment.FormaPagamentoCodigo
        pm.Valor = payment.Valor
        pm.CartaoNumero = get_aware_text(payment.CartaoNumero)
        pm.CartaoCodigoSeguranca = get_aware_text(payment.CartaoCodigoSeguranca)
        pm.CartaoValidade = get_aware_text(payment.CartaoValidade)
        pm.CartaoNomeImpresso = get_aware_text(payment.CartaoNomeImpresso)
        pm.CartaoQtdeParcelas = payment.CartaoQtdeParcelas
        pm.CartaoCodigoAutorizacao = get_aware_text(payment.CartaoCodigoAutorizacao)
        pm.BoletoVencimento = payment.BoletoVencimento.strftime('%d%m%Y') if payment.BoletoVencimento else None
        pm.BoletoNumeroBancario = get_aware_text(payment.BoletoNumeroBancario)
        pm.CartaoCPFouCNPJTitular = re.sub(r'[^\d]+', '', get_aware_text(payment.CartaoCPFouCNPJTitular)) if payment.CartaoCPFouCNPJTitular else None
        pm.CartaoDataNascimentoTitular = payment.CartaoDataNascimentoTitular.strftime('%d%m%Y') if payment.CartaoDataNascimentoTitular else None
        pm.DebitoEmContaNumeroBanco = get_aware_text(payment.DebitoEmContaNumeroBanco)
        pm.DebitoEmContaCodigoAgencia = get_aware_text(payment.DebitoEmContaCodigoAgencia)
        pm.DebitoEmContaDVCodigoAgencia = get_aware_text(payment.DebitoEmContaDVCodigoAgencia)
        pm.DebitoEmContaContaCorrente = get_aware_text(payment.DebitoEmContaContaCorrente)
        pm.DebitoEmContaDVContaCorrente = get_aware_text(payment.DebitoEmContaDVContaCorrente)
        pm.PreAutorizadaNaPlataforma = payment.PreAutorizadaNaPlataforma
        pm.CartaoTID = get_aware_text(payment.CartaoTID)
        pm.CartaoNSU = get_aware_text(payment.CartaoNSU)
        pm.CartaoNumeroToken = get_aware_text(payment.CartaoNumeroToken)
        pm.CodigoTransacaoGateway = get_aware_text(payment.CodigoTransacaoGateway)
        return pm

    def add_order(self, order, order_items, payments):
        ArrayOfDadosPedidos = self.client.factory.create('ArrayOfDadosPedidos')
        ArrayOfDadosPedidos.DadosPedidos = [self._order_factory(order, order_items, payments)]

        response = self.client.service.InserirPedido(ChaveIdentificacao=self.api_key, ListaDePedidos=ArrayOfDadosPedidos)
        code, description, response_type, exception_message = self.parse_response(response)
        # print response
        # print code
        # print description
        # print response_type
        # print exception_message

        success = False
        if response_type in TipoDeResultadoEnumSuccessList:
            success = True

        # Ótimo para debug, nao apagar
        # print self.client.last_sent()
        # print "=========================="
        # print self.client.last_received()

        return {
            'result': {
                # 'original': response,
                'original': self.client_last_received(),
                'code': code,
                'message': description,
                'type': response_type,
                'exception_message': exception_message
            },
            'success': success,
            # 'request_body': ArrayOfDadosPedidos,
            'request_body': self.client_last_sent()
        }

    def _confirm_payment_order_factory(self, confirm_payment_order):
        po = self.client.factory.create('DadosPgtoPedido')

        po.NumeroPedido = confirm_payment_order.NumeroPedido
        po.DataPagamento = confirm_payment_order.DataPagamento.strftime('%d%m%Y') if confirm_payment_order.DataPagamento else None
        po.CartaoCodigoAutorizacao = confirm_payment_order.CartaoCodigoAutorizacao
        po.CartaoNSU = confirm_payment_order.CartaoNSU
        po.CartaoTID = confirm_payment_order.CartaoTID
        po.CartaoCodigoRetorno = confirm_payment_order.CartaoCodigoRetorno
        po.CartaoMensagemRetorno = confirm_payment_order.CartaoMensagemRetorno
        po.StatusPagamento = StatusPagamentoEnum.speConfirmado

        return po

    def confirm_payment_order(self, confirm_payment_order):
        ArrayOfDadosPgtoPedido = self.client.factory.create('ArrayOfDadosPgtoPedido')
        ArrayOfDadosPgtoPedido.DadosPgtoPedido = [self._confirm_payment_order_factory(confirm_payment_order)]

        response = self.client.service.ConfirmarPagamentosPedidos(
            ChaveIdentificacao=self.api_key,
            ListaDePagamentos=ArrayOfDadosPgtoPedido,
        )

        code, description, response_type, exception_message = self.parse_response(response)
        # print response
        # print code
        # print description
        # print response_type
        # print exception_message

        success = False
        if response_type in TipoDeResultadoEnumSuccessList:
            success = True

        return {
            'result': {
                # 'original': response,
                'original': self.client_last_received(),
                'code': code,
                'message': description,
                'type': response_type,
                'exception_message': exception_message
            },
            'success': success,
            # 'request_body': ArrayOfDadosPgtoPedido,
            'request_body': self.client_last_sent()
        }

    def _cancel_order_factory(self, cancel_order):
        co = self.client.factory.create('DadosCancelamentoPedido')
        co.CodigoPedido = cancel_order.CodigoPedido
        co.CodigoMotivoCancelamento = cancel_order.CodigoMotivoCancelamento
        co.MensagemCancelamento = get_aware_text(cancel_order.MensagemCancelamento)

        return co

    def _parse_response_cancel_order(self, response):

        code = response.Resultado.Codigo
        description = str(response.Resultado.Descricao)
        response_type = str(response.Resultado.Tipo)

        exception_message = u''
        if response_type not in TipoDeResultadoEnumSuccessList:
            exception_message = getattr(response.Resultado, 'ExceptionMessage', u'')
            exception_message = str(exception_message)
        return code, description, response_type, exception_message

    def cancel_order(self, cancel_order):
        DadosCancelamentoPedido = self._cancel_order_factory(cancel_order)
        response = self.client.service.CancelarPedido(
            ChaveIdentificacao=self.api_key,
            DadosCancelamentoPedido=DadosCancelamentoPedido,
        )

        code, description, response_type, exception_message = self._parse_response_cancel_order(response)
        # print code
        # print description
        # print response_type
        # print exception_message

        success = False
        if response_type in TipoDeResultadoEnumSuccessList:
            success = True

        return {
            'result': {
                'original': self.client_last_received(),
                'code': code,
                'message': description,
                'type': response_type,
                'exception_message': exception_message
            },
            'success': success,
            'request_body': self.client_last_sent()
        }

    def parse_response_retrieve(self, response, callback):
        code = response.ResultadoOperacao.Codigo
        description = response.ResultadoOperacao.Descricao
        response_type = response.ResultadoOperacao.Tipo
        exception_message = ''
        data = []
        success = True

        if response_type in TipoDeResultadoEnumSuccessList:
            data = callback(response)
        else:
            exception_message = response.ResultadoOperacao.ExceptionMessage
            success = False

        # print code
        # print description
        # print response_type
        # print exception_message
        # print data
        # import json
        # print json.dumps(data, sort_keys=True, indent=4)

        return code, description, response_type, success, exception_message, data

    def get_availables_status_orders(self):
        response = self.client.service.StatusPedidoDisponiveis(ChaveIdentificacao=self.api_key)

        def callback_status_order_list_parser(response):
            availables_status_orders = []
            if getattr(response, 'Rows', None):
                for order_status in response.Rows.DadosStatusPedido:
                    status = {
                        'protocol_status': smart_encode(order_status.ProtocoloStatusPedido),
                        'number': int(order_status.NumeroPedido),
                        'abacos_code': int(order_status.CodigoPedidoAbacos),
                        'status_code': int(order_status.CodigoStatus),
                        'status': smart_encode(order_status.StatusPedido),
                        'datetime': order_status.DataHora,
                        'invoice_serie': smart_encode(order_status.SerieNota),
                        'invoice_number': order_status.NumeroNota,
                        'object_number': smart_encode(order_status.NumeroObjeto),
                        'amount_size': int(order_status.QuantidadeVolumes),
                        'cancel_reason_code': smart_encode(order_status.CodigoMotivoCancelamento),
                        'cancel_reason': smart_encode(order_status.MotivoCancelamento),
                        'nfe_key': smart_encode(order_status.ChaveNfe),
                    }
                    status['invoice_date_emission'] = None
                    if order_status.DataEmissaoNota:
                        # pega a data até o 'ponto', transformando isto
                        # '07082018 17:09:11.334' nisso '07082018 17:09:11'
                        ide = order_status.DataEmissaoNota
                        ide = ide[0:ide.find(".")]
                        # e converte em data real Python
                        status['invoice_date_emission'] = \
                            datetime.strptime(ide, '%d%m%Y %H:%M:%S')

                    availables_status_orders.append(status)
            return availables_status_orders

        code, description, response_type, success, exception_message, data = \
            self.parse_response_retrieve(response, callback_status_order_list_parser)

        return {
            'result': {
                'original': response,
                'data': data,
                'code': code,
                'message': smart_encode(description),
                'type': smart_encode(response_type),
                'exception_message': smart_encode(exception_message),
                'success': success,
            }
        }

    def confirm_integration_order_status(self, protocol_status):
        response = self.client.service.ConfirmarRecebimentoStatusPedido(ProtocoloStatusPedido=protocol_status)
        return parse_response_confirm_integration(response, protocol_status)
