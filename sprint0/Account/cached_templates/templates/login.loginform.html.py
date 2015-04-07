# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428375475.59105
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Account\\templates/login.loginform.html'
_template_uri = 'login.loginform.html'
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<form id="loginform" method="POST" action="/Account/login.loginform/">\n            <table>\n\n                ')
        __M_writer(str( form ))
        __M_writer('\n                <tr>\n                    <td>\n                        <input type="submit" class="btn btn-primary"></input>\n                    </td>\n                </tr>\n\n            </table>\n        </form>\n    <a href="/password_reset/">Forgot your Password?</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Account\\templates/login.loginform.html", "uri": "login.loginform.html", "line_map": {"35": 1, "53": 2, "54": 6, "55": 6, "40": 16, "27": 0, "61": 55, "46": 2}}
__M_END_METADATA
"""
