# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426621337.305345
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Account/templates/UpdatePassword.html'
_template_uri = 'UpdatePassword.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        warnings = context.get('warnings', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        warnings = context.get('warnings', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<h1>Login page</h1>\n')
        if warnings == None:
            __M_writer('\n')
        else:
            __M_writer('<h2>')
            __M_writer(str( warnings ))
            __M_writer('</h2>\n')
        __M_writer('\n<table>\n    <form method="POST">\n        ')
        __M_writer(str( form ))
        __M_writer('\n        <tr>\n            <td><button type="submit" class="btn btn-primary">Submit</button><a class="btn btn-default" href="/Account/Account">Cancel</a></td>\n        </tr>\n    </form>\n</table>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/Account/templates/UpdatePassword.html", "line_map": {"64": 19, "27": 0, "36": 1, "70": 64, "41": 27, "47": 9, "55": 9, "56": 11, "57": 12, "58": 13, "59": 14, "60": 14, "61": 14, "62": 16, "63": 19}, "uri": "UpdatePassword.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
