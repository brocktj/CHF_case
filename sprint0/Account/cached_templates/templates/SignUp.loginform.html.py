# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425714858.800416
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Account/templates/SignUp.loginform.html'
_template_uri = 'SignUp.loginform.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<form id ="sign_up_form" method="POST" action="/Account/SignUp.loginform/')
        __M_writer(str( request.urlparams[0] ))
        __M_writer('">\n<table>\n        ')
        __M_writer(str( form ))
        __M_writer('\n        <tr>\n            <td><button type="submit" class="btn btn-primary">Submit</button></td>\n        </tr>\n</table>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "SignUp.loginform.html", "line_map": {"65": 59, "59": 7, "36": 1, "57": 5, "55": 3, "56": 5, "41": 13, "58": 7, "27": 0, "47": 3}, "filename": "/Users/brock/sprint0/Account/templates/SignUp.loginform.html"}
__M_END_METADATA
"""
