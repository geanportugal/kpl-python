# coding: utf-8
import re
import enums
from utils import get_aware_text
from base import ClientSoap


class CustomerSoap(ClientSoap):

    COMPANY, INDIVIDUAL = 'pj', 'pf'
    MALE, FEMALE = 'male', 'female'
    CUSTOMER_ADDRESS, SHIPPING_ADDRESS, BILLING_ADDRESS = 1, 2, 3
    HOME, MOBILE = 1, 2

    def _address_factory(self, customer):
        TTipoLocalEntregaEnum = self.client.factory.create('TTipoLocalEntregaEnum')
        address = self.client.factory.create('DadosEndereco')
        if customer.Endereco.Logradouro:
            address.Logradouro = get_aware_text(customer.Endereco.Logradouro)
        if customer.Endereco.NumeroLogradouro:
            address.NumeroLogradouro = get_aware_text(customer.Endereco.NumeroLogradouro)
        if customer.Endereco.Complemento:
            address.Complemento = get_aware_text(customer.Endereco.Complemento)
        if customer.Endereco.Bairro:
            address.Bairro = get_aware_text(customer.Endereco.Bairro)
        if customer.Endereco.Municipio:
            address.Municipio = get_aware_text(customer.Endereco.Municipio)
        if customer.Endereco.Estado:
            address.Estado = get_aware_text(customer.Endereco.Estado)
        if customer.Endereco.Cep:
            address.Cep = re.sub(r'[^\d]+', '', get_aware_text(customer.Endereco.Cep))
        if customer.Endereco.Referencia:
            address.Referencia = get_aware_text(customer.Endereco.Referencia)
        if customer.Endereco.EndCodigoIBGE:
            address.EndCodigoIBGE = get_aware_text(customer.Endereco.EndCodigoIBGE)
        address.TipoLocal = TTipoLocalEntregaEnum.tleeResidencial
        address.Pais = None  # precisa setar None, para o Nó não ser criado no XML (Nao pode setar False - Validacao de Negocio)

        return address

    def _customer_factory(self, customer):
        c = self.client.factory.create('DadosClientes')
        # TipoPessoaEnum = self.client.factory.create('TipoPessoaEnum')
        c.TipoPessoa = customer.TipoPessoa
        if customer.TipoPessoa == enums.TipoPessoaEnum.tpeFisica:
            c.Sexo = customer.Sexo
            if customer.DataNascimento:
                c.DataNascimento = customer.DataNascimento.strftime('%d%m%Y')
        else:
            c.Sexo = enums.TipoSexoEnum.tseEmpresa

        c.EMail = get_aware_text(customer.EMail)
        c.CPFouCNPJ = re.sub(r'[^\d]+', '', get_aware_text(customer.CPFouCNPJ))
        c.Codigo = get_aware_text(customer.Codigo)
        c.Nome = get_aware_text(customer.Nome)
        c.NomeReduzido = get_aware_text(customer.NomeReduzido)

        c.Telefone = customer.Telefone
        c.Celular = customer.Celular
        if customer.DataCadastro:
            c.DataCadastro = customer.DataCadastro.strftime('%d%m%Y %H:%M:%S.%f')
        if customer.Endereco:
            c.Endereco = self._address_factory(customer)
        # c.EndEntrega = self._address_factory(customer, CustomerSoap.SHIPPING_ADDRESS)
        c.ClienteEstrangeiro = None  # precisa setar None, para o Nó não ser criado no XML (Nao pode setar False - Validacao de Negocio)
        c.ResultadoOperacao = None  # precisa setar None, para o Nó não ser criado no XML
        # c.EndCobranca = None  # precisa setar None, para o Nó não ser criado no XML

        return c

    def add_customer(self, customer):
        ArrayOfDadosClientes = self.client.factory.create('ArrayOfDadosClientes')
        ArrayOfDadosClientes.DadosClientes = [self._customer_factory(customer)]

        response = self.client.service.CadastrarCliente(ChaveIdentificacao=self.api_key, ListaDeClientes=ArrayOfDadosClientes)
        code, description, response_type, exception_message = self.parse_response(response)
        # print "response: ", response
        # print "code: ", code
        # print "description: ", description
        # print "response_type: ", response_type
        # print "exception_message: ", exception_message

        success = False
        if response_type in enums.TipoDeResultadoEnumSuccessList:
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
            # 'request_body': ArrayOfDadosClientes,
            'request_body': self.client_last_sent()
        }
