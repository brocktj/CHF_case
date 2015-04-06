# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425785212.067729
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/styles/StoreView.cssm'
_template_uri = 'StoreView.cssm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('.item_container {\n    margin: 12px;\n    display: inline-block;\n}\n\n.item_container > img {\n    max-height: 150px;\n    margin: 12px;\n\n\n}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "27": 21, "21": 1}, "filename": "/Users/brock/sprint0/Store/styles/StoreView.cssm", "uri": "StoreView.cssm", "source_encoding": "ascii"}
__M_END_METADATA
"""
