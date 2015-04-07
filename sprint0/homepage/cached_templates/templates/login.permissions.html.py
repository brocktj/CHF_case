# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423356121.937597
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/login.permissions.html'
_template_uri = 'login.permissions.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<form method="POST">\n    <h1>You are not authorized to view this page, please login as an administrator or speak to an administrator</h1>\n    <table>\n    ')
        __M_writer(str( form ))
        __M_writer('\n    </table>\n<input type="submit"/>\n</form>\n<body>\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/brock/sprint0/homepage/templates/login.permissions.html", "line_map": {"16": 0, "24": 10, "30": 24, "22": 1, "23": 10}, "uri": "login.permissions.html"}
__M_END_METADATA
"""
