# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422414883.645534
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/SaleItem.html'
_template_uri = 'SaleItem.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\nsaleitem page\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "SaleItem.html", "filename": "/Users/brock/sprint0/homepage/templates/SaleItem.html", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii"}
__M_END_METADATA
"""
