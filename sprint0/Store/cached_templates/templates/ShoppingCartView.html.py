# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428430011.252115
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/ShoppingCartView.html'
_template_uri = 'ShoppingCartView.html'
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
        y = context.get('y', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        x = context.get('x', UNDEFINED)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n<head lang="en">\r\n    <meta charset="UTF-8">\r\n    <title></title>\r\n</head>\r\n<body>\r\n\r\n')
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
        def content():
            return render_content(context)
        x = context.get('x', UNDEFINED)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<table class="table table-striped">\r\n    <tr>\r\n        <td>item</td>\r\n        <td></td>\r\n        <td>quantity</td>\r\n        <td>price</td>\r\n\r\n\r\n    </tr>\r\n    ')
        total = 0 
        
        __M_writer('\r\n')
        for k in x:
            __M_writer('    <tr>\r\n\r\n        ')
            item = hmod.BulkProduct.objects.get(id=k) 
            
            __M_writer('\r\n        ')
            qty = x.get(k) 
            
            __M_writer('\r\n\r\n        <td>\r\n            ')
            __M_writer(str( item.name ))
            __M_writer('\r\n        </td>\r\n        <td>\r\n            <a class="btn btn-warning" href="/Store/ShoppingCart.delete_item/')
            __M_writer(str( item.id ))
            __M_writer('">Remove</a>\r\n        </td>\r\n        <td>\r\n            ')
            __M_writer(str( qty ))
            __M_writer('\r\n        </td>\r\n        <td>\r\n            $')
            __M_writer(str( item.current_price ))
            __M_writer('\r\n\r\n        </td>\r\n        ')
            total += (int(qty) * item.current_price) 
            
            __M_writer('\r\n    </tr>\r\n\r\n')
        for i in y:
            __M_writer('    ')
            item = hmod.WardrobeItem.objects.get(id=i) 
            
            __M_writer('\r\n\r\n<tr>\r\n        <td>\r\n            ')
            __M_writer(str( item.name ))
            __M_writer('\r\n        </td>\r\n        <td>\r\n            <a class="btn btn-warning" href="/Store/ShoppingCart.delete_rental_item/')
            __M_writer(str( item.id ))
            __M_writer('">Remove</a>\r\n        </td>\r\n        <td>\r\n            1\r\n        </td>\r\n        <td>\r\n           $')
            __M_writer(str( item.standard_rental_value ))
            __M_writer('\r\n        </td>\r\n    ')
            total += item.standard_rental_value 
            
            __M_writer('\r\n    </tr>\r\n')
        __M_writer('    <tr>\r\n        <td></td>\r\n        <td></td>\r\n        <td>Total:</td>\r\n        <td>$')
        __M_writer(str( total ))
        __M_writer('</td>\r\n\r\n\r\n    </tr>\r\n\r\n</table>\r\n<div><a class="btn btn-success" href="/Store/ShoppingCart.check_out/')
        __M_writer(str( total ))
        __M_writer('">Checkout</a> </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "ShoppingCartView.html", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/ShoppingCartView.html", "line_map": {"64": 22, "65": 23, "66": 25, "68": 25, "69": 26, "71": 26, "72": 29, "73": 29, "74": 32, "75": 32, "76": 35, "77": 35, "78": 38, "79": 38, "16": 2, "82": 41, "83": 45, "84": 46, "85": 46, "87": 46, "88": 50, "89": 50, "90": 53, "91": 53, "92": 59, "29": 0, "94": 61, "96": 61, "80": 41, "98": 68, "99": 68, "100": 74, "101": 74, "39": 1, "40": 2, "97": 64, "107": 101, "45": 75, "93": 59, "51": 11, "60": 11, "61": 21, "63": 21}, "source_encoding": "ascii"}
__M_END_METADATA
"""
