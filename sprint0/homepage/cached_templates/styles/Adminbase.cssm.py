# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423364028.415776
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/styles/Adminbase.cssm'
_template_uri = 'Adminbase.cssm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('html, body {\n    margin: 0px;\n    padding: 0px;\n    alignment: center;\n    \n    \n}\n\n.jimbob{\n    padding: 20px;\n    font-size: 1em;\n    position: absolute;\n    bottom: 0px;\n}')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "27": 21, "21": 1}, "filename": "/Users/brock/sprint0/homepage/styles/Adminbase.cssm", "source_encoding": "ascii", "uri": "Adminbase.cssm"}
__M_END_METADATA
"""
