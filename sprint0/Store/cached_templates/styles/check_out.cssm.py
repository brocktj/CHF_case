# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425775290.693633
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/styles/check_out.cssm'
_template_uri = 'check_out.cssm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('.item_container {\n    margin: 12px;\n    display: inline-block;\n}\n\n.item_container > img {\n\n    max-height: 150px;\n    max-width:150px;\n    margin: 12px;\n\n\n}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "27": 21, "21": 1}, "uri": "check_out.cssm", "source_encoding": "ascii", "filename": "/Users/brock/sprint0/Store/styles/check_out.cssm"}
__M_END_METADATA
"""
