# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427225736.410409
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/ShoppingCart.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        warnings = context.get('warnings', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        x = context.get('x', UNDEFINED)
        y = context.get('y', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
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
        def content():
            return render_content(context)
        warnings = context.get('warnings', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        x = context.get('x', UNDEFINED)
        y = context.get('y', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div>')
        __M_writer(str( warnings or " " ))
        __M_writer('</div>\n')
        for k in x:
            __M_writer('    ')
            item = hmod.BulkProduct.objects.get(id=k) 
            
            __M_writer('\n    ')
            qty = x.get(k) 
            
            __M_writer('\n\n<div>\n        <div>\n            ')
            __M_writer(str( item.name ))
            __M_writer('\n        </div>\n        <div>\n            ')
            __M_writer(str( item.current_price ))
            __M_writer('\n        </div>\n        <div>\n           ')
            __M_writer(str( qty ))
            __M_writer('\n        </div>\n    </div>\n')
        __M_writer('\n')
        for i in y:
            __M_writer('    ')
            item = hmod.WardrobeItem.objects.get(id=i) 
            
            __M_writer('\n\n<div>\n        <div>\n            ')
            __M_writer(str( item.name ))
            __M_writer('\n        </div>\n        <div>\n            ')
            __M_writer(str( item.standard_rental_value ))
            __M_writer('\n        </div>\n        <div>\n           1\n        </div>\n    </div>\n')
        __M_writer('\n   ')
        __M_writer(str( current_cart ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/brock/sprint0/Store/templates/ShoppingCart.html", "uri": "ShoppingCart.html", "line_map": {"64": 11, "65": 12, "66": 13, "67": 13, "69": 13, "70": 14, "97": 91, "72": 14, "73": 18, "74": 18, "75": 21, "76": 21, "77": 24, "78": 24, "79": 28, "16": 2, "81": 30, "82": 30, "84": 30, "85": 34, "86": 34, "87": 37, "88": 37, "89": 44, "90": 45, "91": 45, "29": 0, "80": 29, "40": 1, "41": 2, "46": 46, "52": 10, "62": 10, "63": 11}}
__M_END_METADATA
"""
