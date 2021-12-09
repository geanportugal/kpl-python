# -*- coding: utf-8 -*-

"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:abac="http://www.kplsolucoes.com.br/ABACOSWebService">
    <soap:Header/>
    <soap:Body>
        <abac:CadastrarCliente>
            <abac:ChaveIdentificacao>4B836E1E-F6F6-4103-825B-5B03CDA726E4</abac:ChaveIdentificacao>
            <abac:ListaDeClientes>
                <abac:DadosClientes>
                    <abac:EMail>KPL@kpl.com.br</abac:EMail>
                    <abac:CPFouCNPJ>05521031000101</abac:CPFouCNPJ>
                    <abac:Codigo>1712</abac:Codigo>
                    <abac:TipoPessoa>tpeFisica</abac:TipoPessoa>
                    <abac:Documento>111111111</abac:Documento>
                    <abac:InscricaoEstadual>333333333</abac:InscricaoEstadual>
                    <abac:InscricaoMunicipal>44444444</abac:InscricaoMunicipal>
                    <abac:Classificacao>CONSUMIDOR</abac:Classificacao>
                    <abac:Nome>TESTE INTEGRACAO KPL</abac:Nome>
                    <abac:NomeReduzido>INTEGRACAO KPL</abac:NomeReduzido>
                    <abac:Sexo>tseFeminino</abac:Sexo>
                    <abac:DataNascimento>17122015</abac:DataNascimento>
                    <abac:Profissao>E-commerce</abac:Profissao>
                    <abac:Site>www.kplsolucoes.com.br</abac:Site>
                    <abac:Telefone>11 24247380</abac:Telefone>
                    <abac:Fax>11 24247380</abac:Fax>
                    <abac:Celular>11 24247380</abac:Celular>
                    <abac:DataCadastro>17122015</abac:DataCadastro>
                    <abac:TipoContribuinte>tctrNaoContribuinte</abac:TipoContribuinte>
                    <abac:Endereco>
                        <abac:Logradouro>Alameda Cauaxi</abac:Logradouro>
                        <abac:NumeroLogradouro>350</abac:NumeroLogradouro>
                        <abac:Complemento>Complemento</abac:Complemento>
                        <abac:Bairro>Alphaville Industrial</abac:Bairro>
                        <abac:Municipio>Barueri</abac:Municipio>
                        <abac:Estado>SP</abac:Estado>
                        <abac:Cep>06454020</abac:Cep>
                        <abac:TipoLocal>Residencial</abac:TipoLocal>
                        <abac:Referencia>Referencia endereco</abac:Referencia>
                        <abac:Pais>Brasil</abac:Pais>
                        <abac:EndCodigoIBGE/>
                    </abac:Endereco>
                    <abac:SubRegiao>Suldeste</abac:SubRegiao>
                    <abac:GrupoCliente>Cliente</abac:GrupoCliente>
                </abac:DadosClientes>
            </abac:ListaDeClientes>
        </abac:CadastrarCliente>
    </soap:Body>
</soap:Envelope>
"""


class Customer(object):
    EMail = None
    CPFouCNPJ = None
    Codigo = None
    TipoPessoa = None
    Documento = None
    InscricaoEstadual = None
    InscricaoMunicipal = None
    Classificacao = None
    Nome = None
    NomeReduzido = None
    Sexo = None
    DataNascimento = None
    Profissao = None
    Site = None
    Telefone = None
    Fax = None
    Celular = None
    DataCadastro = None
    TipoContribuinte = None
    Endereco = None  # Address instance


class Address(object):
    Logradouro = None
    NumeroLogradouro = None
    Complemento = None
    Bairro = None
    Municipio = None
    Estado = None
    Cep = None
    TipoLocal = None
    Referencia = None
    Pais = None
    EndCodigoIBGE = None
