# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428430017.271446
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/ShoppingCart.html'
_template_uri = 'ShoppingCart.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        y = context.get('y', UNDEFINED)
        warnings = context.get('warnings', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        x = context.get('x', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n<head lang="en">\r\n    <meta charset="UTF-8">\r\n    <title></title>\r\n</head>\r\n<body>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        y = context.get('y', UNDEFINED)
        warnings = context.get('warnings', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        def content():
            return render_content(context)
        x = context.get('x', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div>')
        __M_writer(str( warnings or " " ))
        __M_writer('</div>\r\n')
        for k in x:
            __M_writer('    ')
            item = hmod.BulkProduct.objects.get(id=k) 
            
            __M_writer('\r\n    ')
            qty = x.get(k) 
            
            __M_writer('\r\n\r\n<div>\r\n        <div>\r\n            ')
            __M_writer(str( item.name ))
            __M_writer('\r\n        </div>\r\n        <div>\r\n            ')
            __M_writer(str( item.current_price ))
            __M_writer('\r\n        </div>\r\n        <div>\r\n           ')
            __M_writer(str( qty ))
            __M_writer('\r\n        </div>\r\n    </div>\r\n')
        __M_writer('\r\n')
        for i in y:
            __M_writer('    ')
            item = hmod.WardrobeItem.objects.get(id=i) 
            
            __M_writer('\r\n\r\n<div>\r\n        <div>\r\n            ')
            __M_writer(str( item.name ))
            __M_writer('\r\n        </div>\r\n        <div>\r\n            ')
            __M_writer(str( item.standard_rental_value ))
            __M_writer('\r\n        </div>\r\n        <div>\r\n           1\r\n        </div>\r\n    </div>\r\n')
        __M_writer('\r\n   ')
        __M_writer(str( current_cart ))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "ShoppingCart.html", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/ShoppingCart.html", "line_map": {"64": 11, "65": 12, "66": 13, "67": 13, "69": 13, "70": 14, "97": 91, "72": 14, "73": 18, "74": 18, "75": 21, "76": 21, "77": 24, "78": 24, "79": 28, "16": 2, "81": 30, "82": 30, "84": 30, "85": 34, "86": 34, "87": 37, "88": 37, "89": 44, "90": 45, "91": 45, "29": 0, "80": 29, "40": 1, "41": 2, "46": 46, "52": 10, "62": 10, "63": 11}, "source_encoding": "ascii"}
__M_END_METADATA
"""
