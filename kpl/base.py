# -*- coding: utf-8 -*-
import urllib.error
import urllib.request
from .enums import *
from suds.client import Client
from suds.transport.https import HttpAuthenticated
from suds.transport import TransportError


# COMMERCE_ABACOS_WSDL_URL = "http://mboenterprise.ws.kpl.com.br/AbacosWsPlataforma.asmx?wsdl"  # antigo, de quando era do mercado livre
COMMERCE_ABACOS_WSDL_URL = "http://ws.kpl.onclick.com.br/AbacosWsPlataforma.asmx?wsdl"


class HttpHeaderModify(HttpAuthenticated):
    # precisou fazer isso pois começou a retornar um erro 403 Forbiden, depois que o pessoal
    # da ONCLIK mudou algumas coisas na infra deles. portanto foi preciso colocar essa
    # modificação aqui, que foi encontrada aqui neste link.
    # https://stackoverflow.com/questions/25083855/403-when-retrieving-a-wsdl-via-python-suds
    def open(self, request):
        try:
            url = request.url
            u2request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
            self.proxy = self.options.proxy
            return self.u2open(u2request)
        except urllib.error.HTTPError as e:
            raise TransportError(str(e), e.code, e.fp)


class ClientSoap(object):

    def __init__(self, api_key, timeout=120):
        # import logging
        # logging.basicConfig(level=logging.INFO)
        # logging.getLogger('suds.client').setLevel(logging.DEBUG)
        # logging.getLogger('suds.transport').setLevel(logging.DEBUG)
        # logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
        # logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)

        self.client = Client(
            COMMERCE_ABACOS_WSDL_URL,
            transport=HttpHeaderModify(),  # ver explicação na propria classe
            location=COMMERCE_ABACOS_WSDL_URL.replace('?wsdl', ''),
            timeout=timeout
        )
        self.client.set_options(headers={'User-Agent': 'Mozilla'})
        self.api_key = api_key

    def client_last_sent(self):
        return self.client.last_sent()

    def client_last_received(self):
        return self.client.last_received()

    def parse_response(self, response):
        code = response.ResultadoOperacao.Codigo
        description = str(response.ResultadoOperacao.Descricao)
        response_type = str(response.ResultadoOperacao.Tipo)

        exception_message = u''
        if response_type not in TipoDeResultadoEnumSuccessList:
            exception_message = getattr(response.ResultadoOperacao, 'ExceptionMessage', u'')
            exception_message = str(exception_message)
        return code, description, response_type, exception_message
