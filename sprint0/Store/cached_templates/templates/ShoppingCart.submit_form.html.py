# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425764869.646279
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/ShoppingCart.submit_form.html'
_template_uri = 'ShoppingCart.submit_form.html'
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
        __M_writer('\n<form id="checkout_form" method="POST" action="/Store/ShoppingCart.submit_form">\n    <table>\n        ')
        __M_writer(str( form ))
        __M_writer('\n\n    </table>\n    <button type="submit" class="submit_form">Submit Payment</button>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/Store/templates/ShoppingCart.submit_form.html", "line_map": {"35": 1, "53": 2, "54": 5, "55": 5, "40": 10, "27": 0, "61": 55, "46": 2}, "source_encoding": "ascii", "uri": "ShoppingCart.submit_form.html"}
__M_END_METADATA
"""
