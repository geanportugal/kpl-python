# -*- coding: utf-8 -*-


class TipoEnum:
    tdreSucesso = 'tdreSucesso'  # Sucesso na execução do Método invocado.
    tdreSucessoSemDados = 'tdreSucessoSemDados'  # Sucesso na execução do Método invocado, porém sem retorno de dados.
    tdreAlerta = 'tdreAlerta'  # Alerta na execução do Método invocado.
    tdreErroAplicacao = 'tdreErroAplicacao'  # Erro no Web Service durante a execução do Método invocado.
    tdreErroDataBase = 'tdreErroDataBase'  # Erro no Banco de dados durante a execução do Método invocado.
    tdreErroDados = 'tdreErroDados'  # Erro nos dados durante a execução do Método invocado.
    tdreErroGeral = 'tdreErroGeral'  # Erro Geral durante a execução do Método invocado.
    tdreMensagem = 'tdreMensagem'  # Uma mensagem não relacionada a um erro. Serve para enviar mensagens


TipoDeResultadoEnumSuccessList = [
    TipoEnum.tdreSucesso,
    TipoEnum.tdreSucessoSemDados,
    TipoEnum.tdreAlerta,
]


TipoDeResultadoEnumErrorList = [
    TipoEnum.tdreErroAplicacao,
    TipoEnum.tdreErroDataBase,
    TipoEnum.tdreErroDados,
    TipoEnum.tdreErroGeral,
]


class TipoSexoEnum:
    tseIndefinido = 'tseIndefinido'
    tseFeminino = 'tseFeminino'
    tseMasculino = 'tseMasculino'
    tseEmpresa = 'tseEmpresa'


class TipoPessoaEnum:
    tpeFisica = 'tpeFisica'
    tpeJuridica = 'tpeJuridica'


class TBooleanNullEnum:
    tbneNao = 'tbneNao'


class OptouNFPaulistaEnum:
    tbneSim = "tbneSim"
    tbneNao = "tbneNao"


class TipoLocalEntregaEnum:
    tleeDesconhecido = "tleeDesconhecido"
    tleeResidencial = "tleeResidencial"
    tleeComercial = "tleeComercial"


class StatusPagamentoEnum:
    speNenhum = 'speNenhum'
    speRecusado = 'speRecusado'
    speConfirmado = 'speConfirmado'
