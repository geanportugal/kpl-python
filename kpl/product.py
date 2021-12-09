# -*- coding: utf-8 -*-
# import re
from . enums import *
from . utils import smart_encode, parse_bool, parse_response_confirm_integration
from . base import ClientSoap


class ProductSoap(ClientSoap):

    def parse_response(self, response, callback):
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

    def get_product_list(self):
        """
        Busca sempre uma lista de produtos novos inseridos na KPL
        """
        response = self.client.service.ProdutosDisponiveis(ChaveIdentificacao=self.api_key)

        def callback_product_list_parser(response):
            product_list_parsed = []
            if hasattr(response, "Rows"):
                product_list = response.Rows.DadosProdutos
                for p in product_list:
                    product_parsed = {
                        'is_gift': parse_bool(p.PodeSerBrinde),
                        'protocol_product': smart_encode(p.ProtocoloProduto),
                        'sku': smart_encode(p.CodigoProduto),
                        'parent_sku': smart_encode(p.CodigoProdutoPai),
                        'gtin': smart_encode(p.CodigoBarras),
                        'brand': smart_encode(p.DescricaoMarca),
                        'name': smart_encode(p.NomeProduto),
                        'description': {
                            'short': smart_encode(p.NomeProduto),
                            'long': smart_encode(p.Descricao),
                        },
                        'stock': {
                            "quantity_min": p.QtdeMinimaEstoque
                        },
                        # 'price': {  # nao trazemos o preço aqui, pq ele sempre vem zerado, pois o preço vem pela integração de preço
                        #     'default': p.PrecoTabela1,
                        #     'offer': p.PrecoTabela1
                        # },
                        'weight': p.Peso * 1000,  # converte em gramas
                        'height': p.Altura,
                        'width': p.Largura,
                        'length': p.Profundidade,
                        'has_variants': parse_bool(p.ProdutoTemFilhos),
                        'action': smart_encode(p.Acao),
                    }
                    product_list_parsed.append(product_parsed)
            return product_list_parsed

        code, description, response_type, success, exception_message, data = \
            self.parse_response(response, callback_product_list_parser)

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

    def get_product_list_stock(self):
        """
        Busca sempre uma lista dos estoques lançados na KPL e que estão na fila
        de integração da KPL
        """
        response = self.client.service.EstoquesDisponiveis(ChaveIdentificacao=self.api_key)

        def callback_product_stock_list_parser(self):
            product_stock_list_parsed = []
            if getattr(response, 'Rows', None):

                for item_stock in response.Rows.DadosEstoque:
                    product_stock_list_parsed.append({
                        'sku': smart_encode(item_stock.CodigoProduto),
                        'parent_sku': smart_encode(item_stock.CodigoProdutoPai),
                        'stock': {
                            'quantity': item_stock.SaldoDisponivel,
                            'quantity_min': item_stock.SaldoMinimo,
                        },
                        'abacos_code': item_stock.CodigoProdutoAbacos,
                        'origin_warehouse': item_stock.NomeAlmoxarifadoOrigem,
                        'identifier': item_stock.IdentificadorProduto,
                        'partner_code': item_stock.CodigoProdutoParceiro,
                        'protocol_stock': item_stock.ProtocoloEstoque,
                    })

            return product_stock_list_parsed

        code, description, response_type, success, exception_message, data = \
            self.parse_response(response, callback_product_stock_list_parser)

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

    def get_product_list_prices(self):
        """
        Busca sempre uma lista dos preços lançados na KPL e que estão na fila
        de integração da KPL
        """
        response = self.client.service.PrecosDisponiveis(ChaveIdentificacao=self.api_key)

        def callback_product_price_list_parser(self):
            product_price_list_parsed = []
            if getattr(response, 'Rows', None):
                product_price_added_list = set()
                for price in response.Rows.DadosPreco:

                    code = price.CodigoProduto or price.CodigoProdutoPai
                    if code not in product_price_added_list:
                        product_price_list_parsed.append({
                            'sku': smart_encode(price.CodigoProduto),
                            'parent_sku': smart_encode(price.CodigoProdutoPai),
                            'abacos_code': price.CodigoProdutoAbacos,
                            'price': {
                                'offer': price.PrecoTabela,
                                'promotional': price.PrecoPromocional,
                            },
                            # 'list_name_price': smart_encode(price.NomeLista),
                            # 'start_promotion_price': smart_encode(price.DataInicioPromocao),
                            # 'end_promotion_price': smart_encode(price.DataTerminoPromocao),
                            # 'max_product_discount': price.DescontoMaximoProduto,
                            'partner_product_code': smart_encode(price.CodigoProdutoParceiro),
                            'protocol_price': smart_encode(price.ProtocoloPreco),
                        })
                        product_price_added_list.add(code)

            return product_price_list_parsed

        code, description, response_type, success, exception_message, data = \
            self.parse_response(response, callback_product_price_list_parser)

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

    def confirm_integration_product(self, protocol_product):
        response = self.client.service.ConfirmarRecebimentoProduto(ProtocoloProduto=protocol_product)
        return parse_response_confirm_integration(response, protocol_product)

    def confirm_integration_stock(self, protocol_stock):
        response = self.client.service.ConfirmarRecebimentoEstoque(ProtocoloEstoque=protocol_stock)
        return parse_response_confirm_integration(response, protocol_stock)

    def confirm_integration_price(self, protocol_price):
        response = self.client.service.ConfirmarRecebimentoPreco(ProtocoloPreco=protocol_price)
        return parse_response_confirm_integration(response, protocol_price)
