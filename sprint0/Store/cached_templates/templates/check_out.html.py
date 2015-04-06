# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428023881.155611
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/check_out.html'
_template_uri = 'check_out.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


import homepage.models as hmod 

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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        form1 = context.get('form1', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        form1 = context.get('form1', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div>\n    your order total is $')
        __M_writer(str( request.urlparams[0] ))
        __M_writer('\n</div>\n<table>\n    <tr>\n        <td class="item_container"></td>\n        <td class="item_container"></td>\n    </tr>\n    <tr>\n        <td class="item_container">\n            Address Information\n            <div>\n                <form>\n                    <table>\n                        ')
        __M_writer(str( form1 ))
        __M_writer('\n\n                    </table>\n                </form>\n\n            </div>\n        </td>\n        <td class="item_container">\n            Credit Card Information\n            <div id="form_container" class="form_container">\n                <form id="checkout_form" method="POST" action="/Store/ShoppingCart.submit_form/')
        __M_writer(str( request.urlparams[0] ))
        __M_writer('">\n\n                    <table>\n                        ')
        __M_writer(str( form ))
        __M_writer('\n                    </table>\n')
        if user.is_authenticated:
            __M_writer('                    <button type="submit" class="submit_form">Submit Payment</button>\n                </form>\n            </div>\n        </td>\n    </tr>\n</table>\n')
        else:
            __M_writer('<div>Please <a href="#">Log in</a> to check out</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "check_out.html", "filename": "/Users/brock/sprint0/Store/templates/check_out.html", "line_map": {"64": 16, "65": 29, "66": 29, "67": 39, "68": 39, "69": 42, "70": 42, "71": 44, "40": 1, "41": 2, "74": 52, "46": 54, "16": 2, "72": 45, "52": 14, "80": 74, "73": 51, "29": 0, "62": 14, "63": 16}, "source_encoding": "ascii"}
__M_END_METADATA
"""
