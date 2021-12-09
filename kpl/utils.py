# -*- coding: utf-8 -*-
from . enums import *


def smart_decode(text):
    if isinstance(text, bytes):
        return text.decode('utf-8')
    return text


def smart_encode(text):
    if text and isinstance(text, bytes):
        return text.encode('utf-8')
    if text and not isinstance(text, bytes):
        return text
    return ""


def parse_bool(text):
    return text == "true"


def get_text_or_none(text):
    return text or None


def get_aware_text(text):
    return get_text_or_none(smart_decode(text))


def parse_response_confirm_integration(response, protocol):
    code = response.Codigo
    description = response.Descricao
    response_type = response.Tipo
    exception_message = ''
    success = True

    if response_type not in TipoDeResultadoEnumSuccessList:
        success = False
        exception_message = response.ExceptionMessage

    return {
        'result': {
            'original': response,
            'code': code,
            'message': smart_encode(description),
            'type': smart_encode(response_type),
            'exception_message': smart_encode(exception_message),
            'protocol': smart_encode(protocol),
            'success': success
        }
    }
