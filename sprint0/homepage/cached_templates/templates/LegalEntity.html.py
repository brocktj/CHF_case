# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422474479.516859
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/LegalEntity.html'
_template_uri = 'LegalEntity.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        Bob = context.get('Bob', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n<p>')
        __M_writer(str( Bob.givenName ))
        __M_writer('</p>\n<p>')
        __M_writer(str(Bob.creationDate))
        __M_writer('</p>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/homepage/templates/LegalEntity.html", "line_map": {"16": 0, "32": 26, "22": 1, "23": 8, "24": 8, "25": 9, "26": 9}, "uri": "LegalEntity.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
