# -*- coding: utf-8 -*-
import unittest
from . enums import *
from  . customer import CustomerSoap
from . entities.customer import Customer, Address


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.cs = CustomerSoap(api_key="440012D7-6E0F-4894-AF32-E506FBBB90EB")

        address = Address()
        address.Logradouro = "Rua 2 Professora Osvaldina Ferreira da Silva"
        address.NumeroLogradouro = "464"
        address.Complemento = ""
        address.Bairro = u"Marabaixo"
        address.Municipio = u"Macapá"
        address.Estado = "AP"
        address.Cep = u"68906-452"
        address.TipoLocal = "Residencial"
        address.Referencia = ""
        address.Pais = "Brasil"
        address.EndCodigoIBGE = ""

        c = Customer()
        c.EMail = u"ciclano2@gmail.com"
        c.CPFouCNPJ = u"194.712.270-34"
        c.Codigo = u"100000012"
        c.TipoPessoa = TipoPessoaEnum.tpeJuridica
        c.Documento = "4198837484"
        c.InscricaoEstadual = "333333333"
        c.InscricaoMunicipal = "44444444"
        c.Classificacao = "CONSUMIDOR"
        c.Nome = "Joao Fulano"
        c.NomeReduzido = "Joao"
        c.Sexo = TipoSexoEnum.tseMasculino
        c.DataNascimento = "1984/12/03"
        c.Profissao = "Web Developer"
        c.Site = ""
        c.Telefone = "(16) 99101-1851"
        c.Fax = ""
        c.Celular = "(16) 99101-1851"
        c.DataCadastro = ""
        c.TipoContribuinte = ""
        c.Endereco = address
        self.customer = c

    # def test_empty_field_EMail(self):
    #     self.customer.EMail = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreErroDataBase)

    # def test_empty_field_CPFouCNPJ(self):
    #     self.customer.CPFouCNPJ = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Codigo(self):
    #     self.customer.Codigo = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Codigo_and_CPFouCNPJ(self):
    #     self.customer.Codigo = ""
    #     self.customer.CPFouCNPJ = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Nome(self):
    #     self.customer.Nome = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreErroDataBase)

    # def test_empty_field_Sexo(self):
    #     self.customer.Sexo = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Endereco(self):
    #     self.customer.Endereco = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Endereco__Logradouro(self):
    #     self.customer.Endereco.Logradouro = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreErroDataBase)

    # def test_empty_field_Endereco__NumeroLogradouro(self):
    #     self.customer.Endereco.NumeroLogradouro = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Endereco__Bairro(self):
    #     self.customer.Endereco.Bairro = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Endereco__Municipio(self):
    #     self.customer.Endereco.Municipio = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreErroDataBase)

    # def test_empty_field_Endereco__Estado(self):
    #     self.customer.Endereco.Estado = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreErroDataBase)

    # def test_empty_field_Endereco__Cep(self):
    #     self.customer.Endereco.Cep = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreErroDataBase)

    # def test_empty_field_Endereco__TipoLocal(self):
    #     self.customer.Endereco.TipoLocal = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Endereco__Pais(self):
    #     self.customer.Endereco.Pais = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    # def test_empty_field_Endereco__EndCodigoIBGE(self):
    #     self.customer.Endereco.EndCodigoIBGE = ""
    #     r = self.cs.add_customer(self.customer)
    #     self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)

    def test_create_customer(self):
        r = self.cs.add_customer(self.customer)
        print(r)
        # self.assertEqual(r["result"]["type"], enums.TipoEnum.tdreSucesso)
